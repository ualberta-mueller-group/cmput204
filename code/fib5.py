def fib(n):
    return f[n]

f = [0,1]
t = [3,3]
for n in range(2, 21):
    f.append(f[n-1] + f[n-2])
    t.append(t[n-1] + t[n-2] + 3)

for n in range(20):
    print ("fib(", n, ") =", f[n], "       T(", n, ") =", t[n])

for n in range(1,20):
    print ("fib(", n+1, ") / fib(", n, ") =", f[n+1]/f[n])
for n in range(1,20):
    print ("T(", n+1, ") / T(", n, ") =", t[n+1]/t[n])
