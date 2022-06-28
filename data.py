import requests

parameters = {
    "amount": 50,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
data = response.json()
question_data = data["results"]

