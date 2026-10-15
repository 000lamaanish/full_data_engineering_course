# import logging


# def extract_data():
#     data = [
#         {"order_id": 101, "amount": 500},
#         {"order_id": 102, "amount": 750},
#         {"order_id": 103, "amount": -200}
#     ]

#     return data


# def transform_data(datas):
#     for row in datas:
#         row['amount'] = float(row['amount'])

#     return datas


# def validate(datas):
#     valid_orders = []
#     invalid_orders = []

#     for row in datas:
#         if row['amount'] is not None and row['amount'] < 0:
#             invalid_orders.append(row)
#         else:
#             valid_orders.append(row)

#     return invalid_orders, valid_orders


# def load(data):
#     print(f'{len(data)} are valid orders')

#     for order in data:
#         print(f"Loading order {order['order_id']}")


# def run_pipeline():
#     try:
#         data = extract_data()
#         data = transform_data(data)

#         invalid_orders, valid_orders = validate(data)

#         load(valid_orders)

#         logging.info('Pipeline completed')

#     except Exception as e:
#         print(f'Pipeline failed: {e}')


# run_pipeline()


import logging
import os


def extract_data():
    data = [
        {"order_id": 101, "amount": 500},
        {"order_id": 102, "amount": 750},
        {"order_id": 103, "amount": -200}
    ]
    return data


def transform_data(datas):
    for row in datas:
        row["amount"] = float(row["amount"])
    return datas


def validate(datas):
    valid_orders = []
    invalid_orders = []

    for row in datas:
        if row["amount"] is not None and row["amount"] < 0:
            invalid_orders.append(row)
        else:
            valid_orders.append(row)

    return valid_orders, invalid_orders


def load(data):
    print(f"{len(data)} valid orders")

    for order in data:
        print(f"Loading order {order['order_id']}")


def run_pipeline():
    pipeline_name = os.getenv("PIPELINE_NAME", "Sales ETL")

    logging.info("Starting pipeline: %s", pipeline_name)

    try:
        data = extract_data()
        data = transform_data(data)

        valid_orders, invalid_orders = validate(data)

        load(valid_orders)

        print(f"Rejected orders: {len(invalid_orders)}")
        logging.info("Pipeline completed successfully")

    except Exception:
        logging.exception("Pipeline failed")
        raise


if __name__ == "__main__":
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()

    logging.basicConfig(
        level=getattr(logging, log_level, logging.INFO),
        format="%(asctime)s %(levelname)s: %(message)s"
    )

    run_pipeline()
