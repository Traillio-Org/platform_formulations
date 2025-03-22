import requests as req
import os
from dotenv import load_dotenv, dotenv_values
from utils.error import handle_request_error


def get_user_acceptance(handle="nkca122", count=20):
    url = os.getenv("ALFA_LEETCODE_API")
    try:
        res = req.get(f"{url}/{handle}/submission?limit={count}")
        res.raise_for_status()

        res_json = res.json()
        if res_json.get("count", None) is not None:
            submissions = res_json.get("submission", [])
            return round(sum(
                True
                for submission in submissions
                if submission["statusDisplay"]
                == "Accepted"
            ) / res_json.get("count", None)*100, 2) if res_json.get("count", None) else 0
        else:
            return None
    except req.exceptions.RequestException as err:
        handle_request_error(err)

    return None
