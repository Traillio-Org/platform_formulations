from codeforces.rating import get_user_rating
from codeforces.calendar import get_user_weekly_submissions
from codeforces.solved import get_user_solved
from codeforces.submission import get_user_acceptance

import os
import pandas as pd
import numpy as np

with open(os.path.abspath("./collection/codeforces/users.txt")) as f:
    usernames = [line.strip() for line in f]

data = []

for user in usernames:
    rating = get_user_rating(user)
    easy, medium, hard = get_user_solved(user)
    acceptance = get_user_acceptance(user)
    weekly = get_user_weekly_submissions(user)

    data.append([rating, easy, medium, hard, acceptance, weekly])

data = np.array(data)
df = pd.DataFrame(
    data, columns=["rating", "easy", "medium", "hard", "acceptance", "weekly"]
)
df.to_csv(os.path.abspath("./data/raw/codeforces.csv"), index=False)
