import requests as req
import os
from dotenv import load_dotenv, dotenv_values
from utils.error import handle_request_error
import datetime
from datetime import datetime as date_time

load_dotenv()

def get_user_rating(handle="Nkca122"):
    url = f"{os.getenv("CODEFORCES_API")}/user.info?handles={handle}"
    
    try:
        res = req.get(url)
        res.raise_for_status()

        res_json = res.json()
        if res_json.get("status", None) == "OK":
            return res_json["result"][0].get("rating", None)
        else:
            return None
    except requests.exceptions.RequestException as err:
       handle_request_error(err)
    return None