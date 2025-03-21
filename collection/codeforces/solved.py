import requests as req
import os
from dotenv import load_dotenv, dotenv_values
from utils.error import handle_request_error
import datetime
from datetime import datetime as date_time

load_dotenv()


def get_user_solved(handle="Nkca122"):
    url = f"{os.getenv("CODEFORCES_API")}/user.status?handle={handle}&from=1&count=1000"

    try:
        res = req.get(url)
        res.raise_for_status()

        res_json = res.json()

        if res_json.get("status", None) != "OK":
            return None

        solved_problems = {}
        difficulty_ranges = {
            "Easy": (800, 1500),
            "Medium": (1500, 2200),
            "Hard": (2200, float("inf")),
        }

        for submission in res_json.get("result", []):
            if submission["verdict"] == "OK" and "problem" in submission:
                problem = submission["problem"]
                problem_id = f"{problem['contestId']}-{problem['index']}"
                difficulty = problem.get("rating", None)

                if difficulty:
                    for category, (low, high) in difficulty_ranges.items():
                        if low <= difficulty < high:
                            solved_problems.setdefault(category, set()).add(problem_id)

        return (
            len(solved_problems.get("Easy", set())),
            len(solved_problems.get("Medium", set())),
            len(solved_problems.get("Hard", set())),
        )

    except req.exceptions.RequestException as err:
        handle_request_error(err)

    return None
