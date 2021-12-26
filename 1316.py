import sys
import collections

input = sys.stdin.readline
n = int(input())
ans_cnt = 0

def isGroupVoca(voca):

    counter = dict(collections.Counter(voca))

    for char, freq in counter.items():
        first_idx : int  = voca.find(char) # 각 문자의 첫 인덱스를 찾는다.
        
        for i in range(1, freq):
            if voca[first_idx + i] != char : return False
        
    return True

for case in range(n):
    v = input()
    if isGroupVoca(v): ans_cnt+=1

print(ans_cnt)