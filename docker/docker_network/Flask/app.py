
import os
import time
import pymysql
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database configuration
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppassword")
DB_NAME = os.getenv("DB_NAME", "flask_db")


def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )


def initialize_database():
    # Create the users table
    for attempt in range(10):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        email VARCHAR(150) NOT NULL UNIQUE
                    )
                """)

            connection.commit()
            connection.close()

            print("Database initialized successfully")
            return

        except pymysql.MySQLError as error:
            print(f"Database connection attempt {attempt + 1}: {error}")
            time.sleep(3)

    raise RuntimeError("Could not connect to MySQL")


@app.route("/")
def home():
    return jsonify({
        "message": "Flask and MySQL application is running"
    })


@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()

    if not data or not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and email are required"}), 400

    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (%s, %s)",
                (data["name"], data["email"])
            )

        connection.commit()

        return jsonify({
            "message": "User added successfully"
        }), 201

    except pymysql.MySQLError as error:
        connection.rollback()
        return jsonify({"error": str(error)}), 400

    finally:
        connection.close()


@app.route("/users", methods=["GET"])
def get_users():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users ORDER BY id")
            users = cursor.fetchall()

        return jsonify(users)

    finally:
        connection.close()


if __name__ == "__main__":
    initialize_database()
    app.run(host="0.0.0.0", port=5000)
