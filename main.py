from urllib import response
import requests
import os

NTX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NTX_KEY = os.environ.get("NUTRITIONIX_KEY")
NTX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NTX_HEADERS = {
    "x-app-id": NTX_APP_ID,
    "x-app-key": NTX_KEY,
}

SHEETY_ENDPOINT = "https://api.sheety.co/58e062f93ad029aa35ddb4a64278ea1e/workoutTracker/workouts"


natural_language_sentence = input("What exercise have you done today?\n> ")

query = {
    "query": natural_language_sentence,
    "gender": "male",
    "weight_kg": 83.2,
    "height_cm": 191,
    "age": 21
}

workout = requests.post(url=NTX_ENDPOINT, headers=NTX_HEADERS, json=query).json()

for exercise in workout["exercises"]:
    ex_name = exercise["name"].title()
    ex_duration = exercise["duration_min"]
    burned_calories = exercise["nf_calories"]
    data = {
        "workout": {
            "exercise": ex_name,
            "duration": ex_duration,
            "caloriesBurned": burned_calories
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=data)
    print(response.text)