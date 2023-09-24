from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import time

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user_data.db"  # SQLite database file
db = SQLAlchemy(app)


class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.Integer, nullable=False)


class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.Integer, nullable=False)


@app.route("/join", methods=["POST"])
def join_website():
    data = request.get_json()
    if "name" in data:
        product_name = data["name"]
        visitor = UserData(
            product_name=product_name,
            timestamp=int(time.time()),
        )
        db.session.add(visitor)
        db.session.commit()
        return jsonify({"message": "Data submitted successfully"})
    else:
        return jsonify({"error": "wtf"}), 400


@app.route("/users", methods=["GET"])
def get_users():
    users = UserData.query.all()
    user_list = []

    for user in users:
        user_data = {
            "id": user.id,
            "name": user.product_name,
            "email": user.email,
            "timestamp": user.timestamp,
        }
        user_list.append(user_data)

    return jsonify(user_list)


@app.route("/submit", methods=["POST"])
def submit_data():
    data = request.get_json()

    if "name" in data and "email" in data:
        product_name = data["name"]
        email = data["email"]
        user = UserData(
            product_name=product_name,
            email=email,
            timestamp=int(time.time()),
        )
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "Data submitted successfully"})
    else:
        return jsonify({"error": "Email is a required field"}), 400


if __name__ == "__main__":
    app.run(port=1337)
