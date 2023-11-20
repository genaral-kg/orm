import psycopg2

connection = psycopg2.connect(
    database='db_kg',
    user='kutman',
    password="1221",
    host='localhost',
    port='5432'
)
print("Database successfully opened")

cursor = connection.cursor()

cursor.execute(
    '''CREATE TABLE company(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        city VARCHAR(50) NOT NULL
    )
    '''
)
print("created table")
connection.commit()
connection.close()
