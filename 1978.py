import sys
# sys.stdin = open("input.txt", "rt")
# N= int(input())
# nums = list(map(int,input().split()))
# cnt=0
# max_element = max(nums)
# a = [False, False] + [True] * (max_element - 2) + [True]
# primes = []
# for i in range(2, max_element+1):
#     if a[i]:
#         primes.append(i)
#         for j in range(2*i, max_element+1, i):
#             a[j]= False

# for num in nums:
#     if num in primes: cnt += 1

# print(cnt)

# 제출코드는 에라스토테네스 체를 테스트케이스의 최대값 + 1 만큼 만들어서
# 걸러진 소수들 중 테스트케이스 num이 있는지 확인하는 알고리즘

# 소수판별은 약수의 제곱근 까지만 해도 상관없는 원리를 이용한 코드는 아래와 같다.

import math

sys.stdin = open("input.txt", "rt")
N= int(input())
nums = list(map(int,input().split()))
cnt=0

def is_prime(x):
    if x<2: return False
    for i in range(2, int(math.sqrt(x))+1): # 2 ~ root(x), 1이 들어오면 반복문이 실행 안되므로 False 리턴 불가능, 따라서 예외처리
        if x % i == 0:
            return False
    return True

for num in nums:
    if is_prime(num):
        cnt+=1
print(cnt)
        




