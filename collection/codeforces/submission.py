import requests as req
import os
from dotenv import load_dotenv, dotenv_values
from utils.error import handle_request_error
import datetime
from datetime import datetime as date_time

load_dotenv()

def get_user_acceptance(handle="Nkca122", count=20):
    url = f"{os.getenv("CODEFORCES_API")}/user.status?handle={handle}&from=1&count={count}"

    try:
        res = req.get(url)
        res.raise_for_status()

        res_json = res.json()

        if res_json.get("status", None) != "OK":
            return None

        total_submissions = len(res_json.get("result", []))
        accepted_submissions = sum(True for sub in res_json.get("result", []) if sub["verdict"] == "OK")

        return round((accepted_submissions / total_submissions) * 100, 2) if total_submissions else 0
    except req.exceptions.RequestException as err:
        handle_request_error(err)
    
    return None
