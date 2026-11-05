
import csv
import pymysql
import os

def get_connection():

    connection = pymysql.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "3309")),
        user=os.getenv("DB_USER", "etl_user"),
        password=os.getenv("DB_PASSWORD", "etl_password"),
        database=os.getenv("DB_NAME", "etl_database")
    )

    return connection

def extract_data():
    data = []

    with open("../data/orders.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    return data

def transform_data(data):
    transformed_data = []

    for row in data:
        cleaned_row = {
            "order_id": int(row["order_id"]),
            "customer_name": row["customer_name"].strip(),
            "email": row["email"].strip().lower(),
            "amount": int(row["amount"]),
            "order_date": row["order_date"].strip(),
            "status": row["status"].strip().lower()
        }

        transformed_data.append(cleaned_row)

    return transformed_data

def transform_data(data):
    transformed_data = []

    for row in data:
        cleaned_row = {
            "order_id": int(row["order_id"]),
            "customer_name": row["customer_name"].strip(),
            "email": row["email"].strip().lower(),
            "amount": int(row["amount"]),
            "order_date": row["order_date"].strip(),
            "status": row["status"].strip().lower()
        }

        transformed_data.append(cleaned_row)

    return transformed_data


def validate_data(data):
    valid_orders = []
    rejected_orders = []

    for row in data:

        if (
            not row["order_id"]
            or not row["customer_name"]
            or not row["email"]
            or row["amount"] < 0
            or not row["order_date"]
            or not row["status"]
        ):
            rejected_orders.append(row)

        else:
            valid_orders.append(row)

    return valid_orders, rejected_orders


def load_data(data):

    connection = get_connection()

    try:
        with connection.cursor() as cursor:

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS orders (
                    order_id INT PRIMARY KEY,
                    customer_name VARCHAR(100) NOT NULL,
                    email VARCHAR(150) NOT NULL,
                    amount DECIMAL(10,2) NOT NULL,
                    order_date DATE NOT NULL,
                    status VARCHAR(30) NOT NULL
                )
            """)

            insert_query = """
                INSERT INTO orders (
                    order_id,
                    customer_name,
                    email,
                    amount,
                    order_date,
                    status
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    customer_name = VALUES(customer_name),
                    email = VALUES(email),
                    amount = VALUES(amount),
                    order_date = VALUES(order_date),
                    status = VALUES(status)
            """

            values = [
                (
                    row["order_id"],
                    row["customer_name"],
                    row["email"],
                    row["amount"],
                    row["order_date"],
                    row["status"]
                )
                for row in data
            ]

            cursor.executemany(insert_query, values)

        connection.commit()

        print(f"Successfully loaded {len(data)} orders into MySQL.")

    except Exception as error:
        connection.rollback()
        print("Error loading data:", error)
        raise

    finally:
        connection.close()

        
if __name__ == "__main__":

    print("Starting ETL pipeline...")

    # 1. Extract
    orders = extract_data()
    print(f"Extracted {len(orders)} orders.")

    # 2. Transform
    transformed_orders = transform_data(orders)
    print("Transformation completed.")

    # 3. Validate
    valid_orders, rejected_orders = validate_data(transformed_orders)

    print(f"Valid orders: {len(valid_orders)}")
    print(f"Rejected orders: {len(rejected_orders)}")

    # 4. Load
    load_data(valid_orders)

    print("ETL pipeline completed successfully!")