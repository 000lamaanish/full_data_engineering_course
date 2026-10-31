from flask import Flask
import pymysql

app= Flask(__name__)

@app.route("/")
def home():
    return "hello world"


@app.route("/insert_data")
def insert_data():

    connection = pymysql.connect(
        host='mysql_container',
        user='root',
        password="demopass",
        database="demodb"
    )
        
    #create a cursor object
    cursor = connection.cursor()

    insert_query = "INSERT INTO users(city, temperature) VALUES(%s , %s)"

    data=('New york', 25)

    cursor.execute(insert_query, data)
    connection.commit()
    cursor.close()
    connection.close()

    return 'data inserted successfully'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

