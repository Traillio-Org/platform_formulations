from codeforces.rating import get_user_rating
from codeforces.calendar import get_user_weekly_submissions
from codeforces.solved import get_user_solved
from codeforces.submission import get_user_acceptance

import pandas as pd 
import numpy as np 

res = get_user_acceptance("sarafarajnasardi")
print(res)
