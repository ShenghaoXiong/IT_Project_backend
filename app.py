from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

HOSTNAME = "127.0.0.1"

PORT = 3306

USERNAME = "root"

PASSWORD = "qwqw.123"

DATABASE = "farmbot_database"

app.config['SQLALCHEMY_DATABASE_URI'] = (f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:"
                                         f"{PORT}/{DATABASE}?charset=utf8")

db = SQLAlchemy(app)

with app.app_context():
    with db.engine.connect() as conn:
        rs = conn.execute(text("select 1"))
        print(rs.fetchone())


# 假设有一个简单的users列表，仅为示例
users = [
    {'id': 1, 'username': 'user1', 'password': 'password1', 'info': '登录info1'},
    {'id': 2, 'username': 'user2', 'password': 'password2', 'info': '登录info2'}
]

@app.route('/users', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    for user in users:
        if user['username'] == username and user['password'] == password:
            return jsonify(user)
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/tokens', methods=['GET'])
def get_tokens():
    # 示例，返回一个简单的token
    return jsonify({'token': 'example_token'})

@app.route('/point', methods=['GET'])
def get_point():
    # 示例，返回一个简单的坐标
    return jsonify({'x': 1.0, 'y': 1.0})

@app.route('/point_groups', methods=['GET'])
def get_point_groups():
    # 示例，返回一组坐标
    return jsonify({
        'weeds': [{'x': 1.0, 'y': 1.0}, {'x': 2.0, 'y': 2.0}]
    })

@app.route('/saved_gardens', methods=['GET'])
def get_saved_gardens():
    # 示例，返回一个garden中的植物配置
    return jsonify({
        'garden1': ['plant1', 'plant2']
    })

@app.route('/sensor_readings', methods=['GET'])
def get_sensor_readings():
    # 示例，返回传感器数据
    return jsonify({
        'humidity': '70%',
        'temperature': '25C'
    })

@app.route('/plant_templates', methods=['GET'])
def get_plant_templates():
    # 示例，返回单个植物的信息
    return jsonify({
        'plant_name': 'Rose',
        'plant_info': 'Needs full sun and regular watering.'
    })


if __name__ == '__main__':
    app.run()
