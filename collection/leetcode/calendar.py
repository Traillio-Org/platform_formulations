import requests as req
import os
import json
from dotenv import load_dotenv, dotenv_values
import datetime
from datetime import datetime as date_time
from utils.error import handle_request_error


def get_user_weekly_submissions(handle="nkca122"):
    url = os.getenv("ALFA_LEETCODE_API")
    try:
        res = req.get(f"{url}/{handle}/calendar")
        res.raise_for_status()

        res_json = res.json()
        submission_calendar = json.loads(res_json.get("submissionCalendar", "{}"))

        if not submission_calendar:
            return None
        else:
            week_ago = (int)((date_time.now() - datetime.timedelta(days=7)).timestamp())
            return sum(
                ct
                for timestamp, ct in submission_calendar.items()
                if (int)(timestamp) >= week_ago
            )
    except req.exceptions.RequestException as err:
        handle_request_error(err)

    return None
