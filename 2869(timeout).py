#타임아웃 코드는 간단한 코드여서 생략, 하단은 정답코드
import sys

A, B, V = map(int,sys.stdin.readline().split())

# (A-B) * n+ A >= V,  n>= (V-A)/(A-B)

if (V-A)%(A-B) == 0:
    print(int((V-A)/(A-B))+1) # 
else:
    print(int((V-A)/(A-B))+2) # 원래는 올림 후 +1인데 올림처리 안했으므로 +2