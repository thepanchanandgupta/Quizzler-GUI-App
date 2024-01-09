import requests

parameter = {
    "amount": 15,
    "category": 23,
    "difficulty": "easy",
    "type": "boolean"
}
response = requests.get("https://opentdb.com/api.php", params=parameter)
response.raise_for_status()
data = response.json()
question_data = data["results"]
