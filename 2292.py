'''
1-1까지는 1번에                               
2-7까지는 2번에
8-19까지는 3번에
20-37까지는 4번에
38-61까지는 5번에
62-91까지는 6번에

첫 범위의 공차는 1 6 12 18 24..  
끝 범위의 공차는 6 12 18 24 30.. 
'''

# An = A(n-1) + 6^(n-1) -> 끝 범위 점화식
end_range = 1
n = int(input())
ans, i = 1, 2 # i는 수열의 input용 변수
if n == 1: 
    print(ans)
else :
    while(n > end_range):
        end_range = end_range + 6 * (i-1)
        i += 1 
        ans += s1
    print(ans)