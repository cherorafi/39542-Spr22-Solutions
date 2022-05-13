# Seat: Podium
# Row: Podium
# I attended lecture.

import numpy as np
import random

def diceSim(D1,D2,trials):
    """
    Input:  the number of sides on die 1 (D1) and die2 (D2) and the number of trials
    Return:  an array with the percentage each possible sum of rolls occured.
    """

    length = D1 + D2
    tots = np.zeros(length+1)
    for i in range(trials):
        tots[random.randint(1,D1)+random.randint(1,D2)] += 1
    return(tots/trials)
