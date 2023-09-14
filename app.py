from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_marshmallow import Marshmallow
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "qwqw.123"
DATABASE = "farmbot_database"

app.config['SQLALCHEMY_DATABASE_URI'] = (f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:"
                                         f"{PORT}/{DATABASE}?charset=utf8")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking

app.config['SECRET_KEY'] = 'qwqw.123'

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Reflect the existing database tables
db.Model.metadata.reflect(db.engine)


# Map the existing tables
class User(db.Model):
    __table__ = db.Model.metadata.tables['user']


class Garden(db.Model):
    __table__ = db.Model.metadata.tables['garden']


class Plants(db.Model):
    __table__ = db.Model.metadata.tables['plants']


class Resource(db.Model):
    __table__ = db.Model.metadata.tables['resource']


class Weeds(db.Model):
    __table__ = db.Model.metadata.tables['weeds']


# Define Schemas
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True


class GardenSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Garden
        load_instance = True


class PlantsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Plants
        load_instance = True


class WeedsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Weeds
        load_instance = True


class ResourceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Resource
        load_instance = True


# ... Continue with other schemas ...


# routes

# Login and register
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(userName=data['userName'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(userName=data['userName']).first()

    if not user:
        return jsonify({"message": "Username not found!"}), 404

    if check_password_hash(user.password, data['password']):
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Wrong password!"}), 401


# ----------- Garden ------------

# Get garden information for a specific user
@app.route('/garden', methods=['GET'])
def get_garden():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Please log in first!"}), 401

    garden = Garden.query.filter_by(userId=user_id).first()
    if not garden:
        return jsonify({"message": "Garden not found!"}), 404

    garden_data = {
        "idgarden": garden.idgarden,
        "landWidtth": garden.landWidtth,
        "landLong": garden.landLong,
        "userId": garden.userId
    }

    return jsonify(garden_data), 200


# Update garden information
@app.route('/garden', methods=['PUT'])2
def update_garden():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Please log in first!"}), 401

    garden = Garden.query.filter_by(userId=user_id).first()
    if not garden:
        return jsonify({"message": "Garden not found!"}), 404

    data = request.get_json()

    if 'landWidtth' in data:
        garden.landWidtth = data['landWidtth']

    if 'landLong' in data:
        garden.landLong = data['landLong']

    db.session.commit()

    return jsonify({"message": "Garden updated successfully!"}), 200


# ----------- Plants ------------

# Get all plant information for a specific user:
@app.route('/plants', methods=['GET'])
def get_plants():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Please log in first!"}), 401

    # Get the gardens of the user
    gardens = Garden.query.filter_by(userId=user_id).all()
    garden_ids = [garden.idgarden for garden in gardens]

    plants = Plants.query.filter(Plants.idGarden.in_(garden_ids)).all()
    plants_schema = PlantsSchema(many=True)
    return jsonify(plants_schema.dump(plants))


# Add new plant
@app.route('/plants', methods=['POST'])
def add_plant():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Please log in first!"}), 401

    data = request.get_json()
    garden_id = data.get('idGarden')

    # Check if the garden belongs to the user
    garden = Garden.query.filter_by(idgarden=garden_id, userId=user_id).first()
    if not garden:
        return jsonify({"message": "Invalid garden ID or garden not associated with user!"}), 400

    new_plant = Plants(
        idGarden=garden_id,
        plantsName=data['plantsName'],
        plantType=data['plantType'],
        plantDay=data['plantDay'],
        plantXpoint=data['plantXpoint'],
        plantYpoint=data['plantYpoint'],
        radius=data['radius']
    )
    db.session.add(new_plant)
    db.session.commit()
    return jsonify({"message": "Plant added successfully!"}), 200


# Update plant information
@app.route('/plants/<int:plant_id>', methods=['PUT'])
def update_plant(plant_id):
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Please log in first!"}), 401

    plant = Plants.query.get(plant_id)
    if not plant:
        return jsonify({"message": "Plant not found!"}), 404

    garden = Garden.query.filter_by(idgarden=plant.idGarden, userId=user_id).first()
    if not garden:
        return jsonify({"message": "You don't have permission to modify this plant!"}), 403

    data = request.get_json()
    if 'plantsName' in data:
        plant.plantsName = data['plantsName']

    if 'plantType' in data:
        plant.plantType = data['plantType']

    if 'plantDay' in data:
        plant.plantDay = data['plantDay']

    if 'plantXpoint' in data:
        plant.plantXpoint = data['plantXpoint']

    if 'plantYpoint' in data:
        plant.plantYpoint = data['plantYpoint']

    if 'radius' in data:
        plant.radius = data['radius']

    db.session.commit()
    return jsonify({"message": "Plant updated successfully!"}), 200


# Delete a plant
@app.route('/plants/<int:plant_id>', methods=['DELETE'])
def delete_plant(plant_id):
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Please log in first!"}), 401

    plant = Plants.query.get(plant_id)
    if not plant:
        return jsonify({"message": "Plant not found!"}), 404

    garden = Garden.query.filter_by(idgarden=plant.idGarden, userId=user_id).first()
    if not garden:
        return jsonify({"message": "You don't have permission to delete this plant!"}), 403

    db.session.delete(plant)
    db.session.commit()
    return jsonify({"message": "Plant deleted successfully!"}), 200


if __name__ == '__main__':
    app.run()
