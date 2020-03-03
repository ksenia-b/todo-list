from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)


app.config['SECRET_KEY'] = 'SOMESECRETKEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)


@app.route('/user', methods=['GET'])
def get_all_users():
    return ''


@app.route('/user/<user_id>', methods=['GET'])
def get_one_user():
    return ''


@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    print("data = ", data)
    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_password, admin=False)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "new user created"})


@app.route('/user/<user_id>', methods=['PUT'])
def promote_user():
    return ''


@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user():
    return ''


if __name__ == '__main__':
    manager.run()
    # app.run(debug=True)

