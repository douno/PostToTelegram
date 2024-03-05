import json
from time import sleep, time

import requests

from utils import get_the_soup

BOT_API_KEY = "YOUR_API_KEY_HERE"
CHAT_ID = "YOUR_CHAT_ID_HERE"

def load_items():
    with open("items.json", "r") as myfile:
        data = myfile.read()

    items_dict = json.loads(data)
    return items_dict


def post_to_telegram(items):

    updated_list = []

    for item in items:
        if item["sent"] == "false":
            item_title = job["item_title"]
            item_url = job["item_url"]

            text = "{} {}".format(item_title, item_url)

            url = (
                "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(
                    BOT_API_KEY, CHAT_ID, text
                )
            )
            r = requests.get(url)
            if r.status_code == 200:
                item["sent"] = "true"
            print(r.status_code)
            sleep(60 - time() % 60)
        else:
            print("already sent")
        updated_list.append(job)

        with open("items.json", "w") as outfile:
            json.dump(updated_list, outfile)

post_to_telegram(load_items())
