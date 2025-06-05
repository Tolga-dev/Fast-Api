import os

from django.db.models.expressions import result
from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from sqlalchemy import Integer, Column, String
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['JWT_SECRET_KEY'] = 'super-secret'
 
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

@app.cli.command('create_db')
def create_db():
    db.create_all()
    print("Database created")

@app.cli.command('drop_db')
def drop_db():
    db.drop_all()
    print("Database dropped")

@app.cli.command('db_seed')
def seed_db():
    mercury = Planet(
        name='Mercury',
        type='Class D',
        star='Sun',
        mass = 1,
        radius = 2,
        distance = 1
    )
 
    venus = Planet(
        name='venus',
        type='Class K',
        star='Sun',
        mass = 1,
        radius = 2,
        distance = 1
    )
    db.session.add(mercury)
    db.session.add(venus)
    
    user_a = User(first_name='A', last_name='A', email='1@1.com', password='1')
    
    db.session.add(user_a)
    db.session.commit()
    print("seed ok")
    
    
@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    test = User.query.filter_by(email=email).first()
    if test:
        return jsonify(message= "That email is already in use."), 409
    else:
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password')
        user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        
        db.session.add(user)
        db.session.commit()
        return jsonify(message= "New User Created!"), 201

@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
        email = request.json['email']
        password = request.json['password']
    else:
        email = request.form.get('email')
        password = request.form.get('password')
    
    print(email)
    print(password)
    test = User.query.filter_by(email=email, password=password).first()
    if test:
        access_token = create_access_token(email)
        return jsonify(message=access_token), 200
    else:
        return jsonify(message="Incorrect email or password"), 401
    
   
    
@app.route('/')
def index():
    return "<h1> Hello World! </h1>"


@app.route('/api')
def api():
    return "<h1> i am api </h1>", 200

@app.route('/jsonify')
def jsonify_api():
    return jsonify(message="Hello World! jsonify"), 200

@app.route('/not_found')
def not_found_api():
    return jsonify(message="not_found"), 404

@app.route('/parameters')
def parameters_api():
    name = request.args.get("name")
    if name:
        return jsonify(name=name), 200
    else:
        return jsonify(name="enter your name!"), 400


@app.route('/url_var/<string:name>/<int:age>')
def url_var(name, age):
    if name or age:
        return jsonify(name=name + " " + str(age)), 200
    else:
        return jsonify(name="enter your name!"), 400

@app.route('/planets', methods=['GET'])
def planets():
    planets_list = Planet.query.all()
    res = planets_schema.dump(planets_list)
    return jsonify(res)

@app.route('/planet_details/<int:planet_id>', methods=['GET'])
def planet(planet_id: int):
    print(planet_id)
    
    found_planet = Planet.query.filter_by(planet_id=planet_id).first()
    if found_planet:
        res = planet_schema.dump(found_planet)
        print(res)
        return jsonify(res)
    else:
        return jsonify(name="Not Found!!"), 400


@app.route('/add_planet', methods=['POST'])
@jwt_required()
def add_planet():
    planet_name = request.form['name']
    test = Planet.query.filter_by(name=planet_name).first()
    
    print(test)    
    if test:
        return jsonify(message="That planet is already in use."), 409
    else:
        print(test)
        print(planet_name)
        
        type = request.form.get('type')
        star = request.form.get('star')
        mass = request.form.get('mass')
        radius = request.form.get('radius')
        distance = request.form.get('distance')
        new_planet = Planet(name=planet_name, type=type, star=star, mass=mass, radius=radius, distance=distance)
        
        db.session.add(new_planet)
        db.session.commit()
        return jsonify(message="New planet created!"), 201


@app.route('/update_planet', methods=['PUT'])
@jwt_required()
def update_planet():
    planet_id = int(request.form['planet_id'])
    planet = Planet.query.filter_by(id=planet_id).first()
    
    if planet:
        planet.name = request.form['name']
        planet.type = request.form['type']
        planet.star = request.form['star']
        planet.mass = request.form['mass']
        planet.radius = request.form['radius']
        planet.distance = request.form['distance']
        db.session.commit()
        return jsonify(message="Updated planet."), 200
    else:
        return jsonify(name="Not Found!!"), 404
    

@app.route('/delete_planet/<int:planet_id>', methods=['DELETE'])
@jwt_required()
def delete_planet(planet_id: int):
    planet = Planet.query.filter_by(planet_id=planet_id).first()
    
    if planet:
        db.session.delete(planet)
        db.session.commit()
        return jsonify(message="Deleted planet."), 200
    else:
        return jsonify(name="Not Found!!"), 404

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    
class Planet(db.Model):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    star = Column(String)
    mass = Column(String)
    radius = Column(String)
    distance = Column(String)

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    first_name = ma.auto_field()
    last_name = ma.auto_field()
    email = ma.auto_field()
    password = ma.auto_field()

class PlanetSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Planet

    planet_id = ma.auto_field()
    name = ma.auto_field()
    type = ma.auto_field()
    star = ma.auto_field()
    mass = ma.auto_field()
    radius = ma.auto_field()
    distance = ma.auto_field()


user_schema = UserSchema()
users_schema = UserSchema(many=True)

planet_schema = PlanetSchema()
planets_schema = PlanetSchema(many=True)

# if __name__ == "__main__":
#     app.run()

# if __name__ == "__main__":
app.run()