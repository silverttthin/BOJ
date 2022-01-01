import sys

sys.stdin = open("input.txt", "rt")

for i in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    center_d_squared = (x1-y1)**2 + (x2-y2)**2 
    rsum_squared = (r1+r2)**2
    rminus_squared = (r1 - r2)**2

    if x1==x2 and y1==y2 and r1 == r2 : print(-1) # clear
    elif center_d_squared > rsum_squared or center_d_squared < rminus_squared: print(0)
    elif center_d_squared == rsum_squared or center_d_squared == rminus_squared : print(1) 
    elif rminus_squared < center_d_squared < rsum_squared: print(2)
 
    
    
"""
두 원의 위치관계
1. 두 점에서 만날 때 
2. 한 점에서 접할 때 
3. 만나지 않을 때 


"""