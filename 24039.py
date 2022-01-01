n = int(input())
a = [False, False] + [True] * (104)
primes = []
for i in range(2, 106):
    if a[i]:
        primes.append(i)
        for j in range(2*i, 106, i):
            a[j]= False

a = 0
ans = primes[a]*primes[a+1]

while(ans <= n):
    a += 1
    ans = primes[a]*primes[a+1]

print(ans)
