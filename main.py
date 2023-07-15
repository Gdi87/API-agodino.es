from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from requests import get

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

@app.route("/")
def home():
    return "Home"

@app.route("/users")
def users():
    users = User.query.all()
    return jsonify(users)

@app.route("/users/<id>")
def user(id):
    user = User.query.get(id)
    return jsonify(user)

@app.route("/users/create", methods=["POST"])
def create_user():
    name = request.json["name"]
    email = request.json["email"]
    password = request.json["password"]
    user = User(name, email, password)
    db.session.add(user)
    db.session.commit()
    return jsonify(user)

@app.route("/users/<id>/update", methods=["PUT"])
def update_user(id):
    user = User.query.get(id)
    user.name = request.json["name"]
    user.email = request.json["email"]
    user.password = request.json["password"]
    db.session.commit()
    return jsonify(user)

@app.route("/users/<id>/delete", methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user)

@app.route("/login", methods=["POST"])
def login():
    email = request.json["email"]
    password = request.json["password"]
    user = User.query.filter_by(email=email).first()
    if user is None or user.password != password:
        return jsonify({"error": "Invalid credentials"})
    login_user(user)
    return jsonify({"success": True})

@app.route("/logout", methods=["POST"])
def logout():
    logout_user()
    return jsonify({"success": True})

@app.route("/weather")
def weather():
    city = request.args.get('city', 'Alicante')
    url = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={your_api_key}&units=metric'.format(city=city, your_api_key=your_api_key)
    response = get(url)
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'error': response.status_code})

if __name__ == "__main__":
    app.run(debug=True)
