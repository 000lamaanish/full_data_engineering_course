FROM python:3.12-slim

WORKDIR /app

COPY etl/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY etl/etl.py .

COPY data/orders.csv /data/orders.csv

CMD ["python", "etl.py"]