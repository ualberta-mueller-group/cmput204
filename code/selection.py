# Selection algorithm as in textbook p.54
# One difference is that Python sequences are 0-based,
# while textbook sequence is 1-based

import random

def split(S, v):
    SL = []; Sv = []; SR = []
    for item in S:
        if item < v:
            SL.append(item)
        elif item == v:
            Sv.append(item)
        else:
            SR.append(item)
    return SL, Sv, SR

def selection(S,k):
    assert k >= 0
    assert k < len(S)
    v = random.choice(S)
    SL, Sv, SR = split(S, v)
    if k < len(SL):
        return selection(SL, k)
    elif k < len(SL) + len(Sv):
        return v
    else:
        return selection(SR, k - len(SL) - len(Sv))

def median(S):
    return selection(S, (len(S)-1)//2)
