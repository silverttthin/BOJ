import sys
input = sys.stdin.readline
voca = input()

cnt = 0
Croatian = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in Croatian:
    if i in voca: 
        cnt += voca.count(i)
        voca = voca.replace(i, "6") 
        #replace는 in-place 메서드가 아니므로 대입 연산 있어야함.
        # 처음에 숫자대신 공백으로 바꿔서 non 크로아티안 알파벳끼리 결합해서 크로아티안 알파벳 되는 오류가 있었음. 
        # 공백대신 임의의 비처리 문자(6)로 바꾸니 해결 

for j in voca:
    if j.isalpha(): cnt+=1

print(cnt)

