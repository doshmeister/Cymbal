import requests
import json
import mysql.connector

# API endpoint and parameters
url = 'https://api.aistream.com/positionreport'
params = {'key': 'your_api_key', 'ship_id': '12345'}

# Get positionreport data from API
response = requests.get(url, params=params)
data = json.loads(response.text)

# Connect to MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
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
url = 'https://api.aistream.com/shipstatic'
params = {'key': 'your_api_key', 'ship_id': '12345'}

# Get shipstatic data from API
response = requests.get(url, params=params)
data = json.loads(response.text)

# Connect to MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
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