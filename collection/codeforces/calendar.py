import requests as req
import os
from dotenv import load_dotenv, dotenv_values
from utils.error import handle_request_error
import datetime
from datetime import datetime as date_time

load_dotenv()


def get_user_weekly_submissions(handle):
    url = f"{os.getenv("CODEFORCES_API")}/user.status?handle={handle}&from=1&count=100"

    try:
        res = req.get(url)
        res.raise_for_status()

        res_json = res.json()

        if res_json.get("status", None) != "OK":
            return None

        week_ago = (int)((date_time.now() - datetime.timedelta(days=7)).timestamp())
        solved_problems = set()
        for submission in res_json.get("result", []):
            if submission["creationTimeSeconds"] >= week_ago:
                solved_problems.add(
                    f"{submission["problem"]['contestId']}-{submission["problem"]['index']}"
                )

        return len(solved_problems)

    except req.exceptions.RequestException as err:
        handle_request_error(err)

    return None
