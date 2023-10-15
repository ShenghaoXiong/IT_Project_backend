from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_marshmallow import Marshmallow
from werkzeug.security import check_password_hash, generate_password_hash
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


HOSTNAME = "34.129.71.70"
PORT = 3306
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "farmbot"

app.config['SQLALCHEMY_DATABASE_URI'] = (f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:"
                                         f"{PORT}/{DATABASE}?charset=utf8")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking

app.config['SECRET_KEY'] = 'qwqw.123'

db = SQLAlchemy(app)
ma = Marshmallow(app)

with app.app_context():
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
USERID = 1

# routes

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# ----------- Garden ------------

# Get garden information for a specific user
@app.route('/garden', methods=['GET'])
def get_garden():
    user_id = USERID           # session.get('user_id')
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
@app.route('/garden', methods=['PUT'])
def update_garden():
    user_id = USERID #session.get('user_id')
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
    user_id = USERID  #session.get('user_id')
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
    user_id = USERID #session.get('user_id')
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
    user_id = USERID #session.get('user_id')
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
    user_id = USERID #session.get('user_id')
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


# ----------- Resource ------------

# Get all resource information for a specific user:

@app.route('/resource', methods=['GET'])
def get_resources():
    all_resources = Resource.query.all()
    resources_schema = ResourceSchema(many=True)
    result = resources_schema.dump(all_resources)
    return jsonify(result)

# Add new resource

@app.route('/resource', methods=['POST'])
def add_resource():
    data = request.get_json()
    new_resource = Resource(
        electricityUsed=data['electricityUsed'],
        waterUsed=data['waterUsed'],
        fertiliserused=data['fertiliserused'],
        date=data['date'],
        landid=data['landid']
    )
    db.session.add(new_resource)
    db.session.commit()
    resource_schema = ResourceSchema(many=True)

    return resource_schema.jsonify(new_resource)


# Update new resource
@app.route('/resource/<id>', methods=['PUT'])
def update_resource(id):
    resource = Resource.query.get(id)
    resource_schema = ResourceSchema(many=True)
    if resource:
        data = request.get_json()
        resource.electricityUsed = data['electricityUsed']
        resource.waterUsed = data['waterUsed']
        resource.fertiliserused = data['fertiliserused']
        resource.date = data['date']
        resource.landid = data['landid']
        db.session.commit()
        return resource_schema.jsonify(resource)
    else:
        return jsonify({"message": "Resource not found"}), 404


# Delete resource
@app.route('/resource/<id>', methods=['DELETE'])
def delete_resource(id):
    resource = Resource.query.get(id)
    if resource:
        db.session.delete(resource)
        db.session.commit()
        return jsonify({"message": "Resource deleted successfully"})
    else:
        return jsonify({"message": "Resource not found"}), 404


# ----------- Weeds ------------

# Get all weeds information for a specific user:
@app.route('/weeds', methods=['GET'])
def get_all_weeds():
    all_weeds = Weeds.query.all()
    weeds_schema = WeedsSchema(many=True)
    result = weeds_schema.dump(all_weeds)
    return jsonify(result)


# Add new weeds
@app.route('/weeds', methods=['POST'])
def add_weeds():
    data = request.get_json()
    new_weeds = Weeds(
        weedXpoint=data['weedXpoint'],
        weedYpoint=data['weedYpoint'],
        weedSize=data['weedSize'],
        idLand=data['idLand']
    )
    db.session.add(new_weeds)
    db.session.commit()
    weeds_schema = WeedsSchema(many=True)
    return weeds_schema.jsonify(new_weeds)


# Update new weeds
@app.route('/weeds/<id>', methods=['PUT'])
def update_weeds(id):
    weeds = Weeds.query.get(id)
    if weeds:
        data = request.get_json()
        weeds.weedXpoint = data['weedXpoint']
        weeds.weedYpoint = data['weedYpoint']
        weeds.weedSize = data['weedSize']
        weeds.idLand = data['idLand']
        db.session.commit()
        weeds_schema = WeedsSchema(many=True)
        return weeds_schema.jsonify(weeds)
    else:
        return jsonify({"message": "Weed not found"}), 404


# Delete a weed
@app.route('/weeds/<id>', methods=['DELETE'])
def delete_weeds(id):
    weeds = Weeds.query.get(id)
    if weeds:
        db.session.delete(weeds)
        db.session.commit()
        return jsonify({"message": "Weed deleted successfully"})
    else:
        return jsonify({"message": "Weed not found"}), 404





if __name__ == '__main__':
    app.run()
