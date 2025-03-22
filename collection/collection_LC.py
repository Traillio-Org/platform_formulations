from leetcode.ranking import get_user_ranking
from leetcode.solved import get_user_solved
from leetcode.submission import get_user_acceptance
from leetcode.calendar import get_user_weekly_submissions

import os
import pandas as pd 
import numpy as np 
import time 
with open(os.path.abspath("./collection/leetcode/users.txt"), encoding="utf-8", errors="ignore") as f:
    usernames = [line.strip() for line in f]


data = []

def fetch_with_retry(func, user, retries=3, delay=2):
    for i in range(retries):
        try:
            return func(user)
        except Exception as e:
            print(f"Error fetching {func.__name__} for {user}: {e}")
            if "429" in str(e) and i < retries - 1:
                wait_time = delay * (2 ** i)
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                return None  
            
        

for user in usernames:
    ranking = fetch_with_retry(get_user_ranking, user)
    easy, medium, hard = fetch_with_retry(get_user_solved, user)
    acceptance = fetch_with_retry(get_user_acceptance, user)
    weekly = fetch_with_retry(get_user_weekly_submissions, user)

    data.append([ranking, easy, medium, hard, acceptance, weekly])

    
data = np.array(data)
df = pd.DataFrame(data, columns=["ranking", "easy", "medium", "hard", "acceptance", "weekly"])
df.to_csv(os.path.abspath("./data/raw/leetcode.csv"), index=False)
