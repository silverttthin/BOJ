import sys
import collections

input = sys.stdin.readline
n = int(input())
ans_cnt = 0

def isGroupVoca(voca):

    counter = dict(collections.Counter(voca)) # 각 문자의 빈도 수 계산

    for char, freq in counter.items():
        first_idx : int  = voca.find(char) # 각 문자의 첫 인덱스를 찾는다.
        
        for i in range(1, freq):
            if voca[first_idx + i] != char : return False 
# 문자 수만큼 연속하여 나오지 않는다면 다른쪽에 있다는 의미이므로 False 리턴

    return True

for case in range(n):
    v = input()
    if isGroupVoca(v): ans_cnt+=1

print(ans_cnt)