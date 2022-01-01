import sys, math
sys.stdin= open("input.txt", "rt")

m,n =map(int, input().split())

array = [True for i in range(n+1)]
array[0] = False
array[1] = False
for i in range(2, int(math.sqrt(n))+1):
    if array[i]==True:
        for j in range(i*2, n+1, i): array[j] = False

for i in range(n+1):
    if array[i]==True and m<=i<=n:
        print(i)
