# 2525와 거의 같은 문제
# 단 주어지는 duration이 초단위 + second 변수 추가
h, m , second= 23,59,0

duration = 500000

# 초단위 duration 이므로 //60 한 값의 결과는 분, % 60한 값의 결과는 초 
m += duration //60
second += duration % 60 

if second >= 60:
    m = m + (second//60)
    second %= 60


if m>= 60 :
    h = h + (m//60)
    m %= 60


if h >= 24: h %= 24 # h처리를 h-=24로 해서 큰 데이터가 넣어졌을때 에러

print(h, m, second)

# 교훈 : 테스트 케이스로 매우 큰 데이터를 넣어보는 것은 도움된다.
# 또한 문제에서 조건에 근접한 경계값 근처에서 여러 데이터를 넣어보자.

