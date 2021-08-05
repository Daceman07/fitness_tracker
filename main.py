import requests
from datetime import datetime

NUTRITION_ID = "***"

NUTRITION_KEY = "***"

NUTRITION_ENDPOING = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = "***"
WEIGHT_KG = "***"
HEIGHT_CM = "***"
AGE = "***"

APP_ID = NUTRITION_ID
API_KEY = NUTRITION_KEY

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(NUTRITION_ENDPOING, json=parameters, headers=headers)
result = response.json()

date = datetime.now()
today = date.strftime("%m-%d-%y")
time = date.strftime("%H:%M")


POST_END_POINT = "https://api.sheety.co/2a63cd69c29c6e6da33ba183dd4bc519/myWorkouts/workouts"

sheet_inputs = {}
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

USER_NAME = "***"
PASSWORD = "***"


sheet_response = requests.post(
    POST_END_POINT,
    json=sheet_inputs,
    auth=(
        USER_NAME,
        PASSWORD,
    )

)

