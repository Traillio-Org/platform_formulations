from leetcode.ranking import get_user_ranking
from leetcode.solved import get_user_solved
from leetcode.submission import get_user_acceptance
from leetcode.calendar import get_user_weekly_submissions

import os
import pandas as pd 
import numpy as np 
import time 
with open(os.path.abspath("./collection/leetcode/users.txt")) as f:
    usernames = [line.strip() for line in f]


data = []

for user in usernames:
    rating = get_user_ranking(user)
    easy, medium, hard = get_user_solved(user)
    acceptance = get_user_acceptance(user)
    weekly = get_user_weekly_submissions(user)
    data.append([rating, easy, medium, hard, acceptance, weekly])
    time.sleep(1.5)

    

data = np.array(data)
df = pd.DataFrame(data, columns=["ranking", "easy", "medium", "hard", "acceptance", "weekly"])
df.to_csv(os.path.abspath("./data/raw/leetcode.csv"), index=False)
