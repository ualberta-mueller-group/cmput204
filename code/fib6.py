import math

MAX = 20

f = [0,1]
t = [3,3]
for n in range(2, MAX):
    f.append(f[n-1] + f[n-2])

phi = (1+math.sqrt(5))/2
print ("Phi = ", phi)

for n in range(MAX):
    print ("fib(", n, ") =", f[n], "phi^", n, " =", phi**n)
    print ("ratio =", f[n]/phi**n)
