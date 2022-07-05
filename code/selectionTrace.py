# Selection algorithm as in textbook p.54, plus print statements for trace
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
    assert k >= 1
    assert k <= len(S)
    print ("selection", S, "k=", k)
    v = random.choice(S)
    SL, Sv, SR = split(S, v)
    print ("v=", v, " Lengths of SL, Sv, SR:", len(SL), len(Sv), len(SR))
    if k <= len(SL):
        return selection(SL, k)
    elif k <= len(SL) + len(Sv):
        return v
    else:
        return selection(SR, k - len(SL) - len(Sv))

def median(S):
    return selection(S, len(S) / 2)

