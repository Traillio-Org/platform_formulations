import requests as req
import os
from dotenv import load_dotenv, dotenv_values
from utils.error import handle_request_error

load_dotenv()

def get_user_ranking(handle="nkca122"):
    url = os.getenv("ALFA_LEETCODE_API")
    try:
        res = req.get(f"{url}/{handle}")
        res.raise_for_status()  

        res_json = res.json()
        return res_json.get("ranking", None)

    except req.exceptions.RequestException as err:
        handle_request_error(err)

    return None