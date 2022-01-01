#틀린풀이 같긴했지만 재귀로 해보려다가 경험부족으로 거의 완성했지만 구현포기
# def get_downstairs_num(k, n): # ex: k = 2, n = 3\
#     ans = 0
#     if k == 0 : return n

#     for i in range(1, n+1):
#         ans += get_downstairs_num(k-1, i)
#     return ans
# k, n = 2, 3
# print(get_downstairs_num(k, n))

for i in range(1):
    # k = int(input())
    # n = int(input())
    k = 2
    n = 3

    people = [i for i in range(1, n+1)]

    for _ in range(k):
        for y in range(1, n):
            people[y] += people[y-1]
        print(people)