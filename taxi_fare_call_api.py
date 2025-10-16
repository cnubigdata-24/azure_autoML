import requests
import json

url = '<your REST API url>'
api_key = '<your key>'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

data = {
    "input_data": {
        "columns": [
            "pickup_datetime",
            "pickup_longitude",
            "pickup_latitude",
            "dropoff_longitude",
            "dropoff_latitude",
            "passenger_count"
        ],
        "index": [0],
        "data": [
            [
                "2011-01-24 18:05:00 UTC",
                -73.983768,
                40.738037,
                -73.982185,
                40.757298,
                1
            ]
        ]
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
