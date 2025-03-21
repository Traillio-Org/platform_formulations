import requests as req
import os
from dotenv import load_dotenv, dotenv_values
from utils.error import handle_request_error

def get_user_solved(handle="nkca122"):
    url = os.getenv("ALFA_LEETCODE_API")

    try:
        res = req.get(f"{url}/{handle}/solved")
        res.raise_for_status()

        res_json = res.json()
        return res_json.get("easySolved", None), res_json.get("mediumSolved", None), res_json.get("hardSolved", None)
    except req.exceptions.RequestException:
        handle_request_error(err)
    
    return None