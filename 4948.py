import sys, math
sys.stdin=open("input.txt", "rt")
# 베르트랑 공준 : 임의의 자연수 n에 대해 (n,2n]의 범위 내에 소수는 적어도 한 개 이상 존재.

# 마지막 인풋이 0일 때 False 리턴하는 함수
# 해당 함수를 while문에 계속 돌리기
# 그러면 0일 때 반복문 빠져나오면서 프로그램 종료

# 에라토스테네스의 체는 2x까지 만들어야함. range(2x+1)
# 이후 2x까지 소수들을 걸러내고 n 초과 2n 이하의 범위 내의 소수 개수 카운트
def checker(x: int) -> int:
    if x == 0: return -1
    cnt = 0
    array = [True for i in range(2*x + 1)]
    array[0]=False
    array[1]=False

    for i in range(2, int(math.sqrt(2*x)) + 1):
        if array[i]==True:
            for j in range(i*2, 2*x + 1, i): array[j] = False
    
    for i in range(x+1, 2*x+1):
        if array[i] == True: cnt+=1
    return cnt
    
while(1):
    cnt = checker(int(input()))
    if cnt<0: exit()
    else : print(cnt)
    

