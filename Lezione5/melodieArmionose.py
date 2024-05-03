
from collections import Counter
def find_lhs(notes : list [int]):
    num_freq = dict(Counter(notes))


    max_length= 0
    for num in num_freq:
        max_length = max(max_length, num_freq[num] + num_freq[num+1])


def third_max(gems: list [int]):
    gems = sorted(list(set(gems)), reverse=True)
    if len(gems) >= 3 : 
        return gems[2]
    else:
        return gems[0]
pass
