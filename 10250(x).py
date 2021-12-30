n = 2
Y, X = 1, 1 # x가 호실, y가 층수

for i in range(n):
    floor, room, guest = 6,12,6
    X = guest // floor + 1
    Y = guest % floor 
    if Y == 0: 
        Y= floor
        X= guest//floor
    ans = Y*100+X
    # print(f'{Y}{X:02d}')
    print(ans)

# 규칙은 찾았는데 X의 예외는 찾지 못했고 초기 X 처리가 아쉬웠음


