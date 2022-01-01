l = [list(map(int,input().split())) for _ in range(int(input()))]
    
ans = sorted(l, key = lambda x : (x[0], x[1]))

for i in ans:
    print(*i)

