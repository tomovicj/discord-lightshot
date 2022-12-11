import json
import requests
import random
import string
import time


with open("settings.json", "r") as f:
    settings = json.load(f)


def getID():
    characters = list(string.ascii_lowercase + string.digits)
    id = ""
    while len(id) < settings["ID length"]:    
        id += random.choice(characters)
    return id


def send():
    data = {"content": f"https://prnt.sc/{getID()}", "embeds": None, "attachments": []}
    x = requests.post(settings["Webhook URL"], json = data)
    print(x)


if __name__ == "__main__":
    if settings["Webhook URL"] == "":
        print("Please enter your Discord Webhook URL in settings.json")
        exit()
    while True:
        send()
        time.sleep(settings["Cooldown"])