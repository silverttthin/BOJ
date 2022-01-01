import sys
import math
sys.stdin = open("input.txt", 'rt')
m =int(input())
n =int(input())
ans = []
array = [True for i in range(n+1)]
array[0] = False
array[1] = False

for i in range(2, int(math.sqrt(n))+1): # +1 안하는 실수!!
    if array[i]:
        for j in range(2*i, n+1, i): array[j] = False # 에라토스테네스의 체

for i in range(n+1):
    if array[i] and m<=i<=n: ans.append(i)
if ans == []: 
    print(-1)
    exit()
else : 
    print(f'{sum(ans)}\n{min(ans)}')