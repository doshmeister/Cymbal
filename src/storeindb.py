import requests
import json
import mysql.connector


# Connect to MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Jdoshi123*",
  database="MySQL80"
)

# Prepare SQL statement
cursor = db.cursor()
sql = "INSERT INTO positionreport (ship_id, timestamp, latitude, longitude, speed, course) VALUES (%s, %s, %s, %s, %s, %s)"

# Insert data into database
for position in data:
    ship_id = position['id']
    timestamp = position['timestamp']
    latitude = position['latitude']
    longitude = position['longitude']
    speed = position['speed']
    course = position['course']
    values = (ship_id, timestamp, latitude, longitude, speed, course)
    cursor.execute(sql, values)
    db.commit()

# Close database connection
db.close()

# API endpoint and parameters

# Connect to MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Jdoshi123*",
  database="MySQL80"
)

# Prepare SQL statement
cursor = db.cursor()
sql = "INSERT INTO shipstatic (ship_id, name, type, length, width) VALUES (%s, %s, %s, %s, %s)"

# Insert data into database
for ship in data:
    ship_id = ship['id']
    name = ship['name']
    ship_type = ship['type']
    length = ship['length']
    width = ship['width']
    values = (ship_id, name, ship_type, length, width)
    cursor.execute(sql, values)
    db.commit()

# Close database connection
db.close()