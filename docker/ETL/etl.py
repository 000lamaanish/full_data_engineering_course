import logging


def extract_data():
    data = [
        {"order_id": 101, "amount": 500},
        {"order_id": 102, "amount": 750},
        {"order_id": 103, "amount": -200}
    ]

    return data


def transform_data(datas):
    for row in datas:
        row['amount'] = float(row['amount'])

    return datas


def validate(datas):
    valid_orders = []
    invalid_orders = []

    for row in datas:
        if row['amount'] is not None and row['amount'] < 0:
            invalid_orders.append(row)
        else:
            valid_orders.append(row)

    return invalid_orders, valid_orders


def load(data):
    print(f'{len(data)} are valid orders')

    for order in data:
        print(f"Loading order {order['order_id']}")


def run_pipeline():
    try:
        data = extract_data()
        data = transform_data(data)

        invalid_orders, valid_orders = validate(data)

        load(valid_orders)

        logging.info('Pipeline completed')

    except Exception as e:
        print(f'Pipeline failed: {e}')


run_pipeline()