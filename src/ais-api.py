import requests

# Setup API to connect to AIS with Token
api_url = "https://data.aishub.net/ws.php?username=A&format=B&output=C&compress=D&latmin=E&latmax=F&lonmin=G&lonmax=H&mmsi=I&imo=J&interval=K"
api_key = "your-api-key"
mmsi = "123456789"

# Make a GET request to the API endpoint with parameters
params = {
    "A": "username",
    "B": 1,
    "C": "json",
    "D": 0,
}
response = requests.get(api_url, params=params)

# Check the response status code
if response.status_code == 200:
    # Parse the response JSON data
    data = response.json()
    # Do something with the data
    print(data)
else:
    # Handle the error
    print("Error: API request failed with status code", response.status_code)