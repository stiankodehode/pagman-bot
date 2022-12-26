import os
clear = lambda: os.system('cls')
import requests

api_url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=religious,racist,sexist"


def get_joke():
    response = requests.get(api_url)
    data = response.json()

    if data["type"] == "single":
        joke_data = {
            "text": data["joke"]
        }
    else: joke_data = {
        "setup": data["setup"],
        "delivery": data["delivery"]
    }
    return joke_data
    


    
    

      

