from modexp import modexp

# Testing that our modexp function computes the same results as 
# Python's built-in pow (power) function
# for some small values

for j in range(-5, 5):
    for k in range(10):
        for m in range(10):
            assert modexp(j, k, m+2) == pow(j, k, m+2)
print("All correct!") # if we get here without an assertion firing, all is good