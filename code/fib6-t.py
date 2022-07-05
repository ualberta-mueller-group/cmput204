import math

MAX = 20

t = [3,3]
for n in range(2, MAX):
    t.append(t[n-1] + t[n-2] + 3)

phi = (1+math.sqrt(5))/2
print (phi)

for n in range(MAX):
    print ("T(", n, ") =", t[n], "phi^", n, " =", phi**n, "ratio =", t[n]/phi**n)
