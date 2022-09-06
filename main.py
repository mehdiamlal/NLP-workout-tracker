import requests
import os

ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NTX_KEY = os.environ.get("NUTRITIONIX_KEY")
NTX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NTX_HEADERS = {
    "x-app-id": NTX_APP_ID,
    "x-app-key": NTX_KEY,
}


natural_language_sentence = input("What exercise have you done today?\n> ")

query = {
    "query": natural_language_sentence,
    "gender": "male",
    "weight_kg": 83.2,
    "height_cm": 191,
    "age": 21
}

data = requests.post(url=ENDPOINT, headers=NTX_HEADERS, json=query).json()

for exercise in data["exercises"]:
    ex_name = exercise["name"].title()
    ex_duration = exercise["duration_min"]
    burned_calories = exercise["nf_calories"]
    print(f"Exercise: {ex_name}\nDuration: {ex_duration} min\nCalories Burned: {burned_calories} cal\n")