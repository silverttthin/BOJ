'''
골드바흐의 추측은 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 

또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다.
예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 
10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.

2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 
만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.
'''

'''
0. n은 4이상 10000 이하의 짝수이다.

1. 에라토스테네스의 체로 n까지의 소수들을 가져온다.

2. 소수 리스트에서 투 포인터로 n - left 가 right와 같다면 골드바흐 파티션! 이후 계속 조사해본다.

3. 만약 아니라면 대소비교를 해본다. n-left가 더 크면 left += 1, 그렇지 않다면 right -= 1

4. 만약 이후에 또다른 골드바흐 파티션이 발견됐다면 그게 차이가 더 작은 파티션이다. right - left가 더 좁아들었을 것이므로.

'''


n = 6
sosu = []
array = [True for i in range(n+1)] # 0-100
array[0] = False
array[1] = False

for i in range(2, int(n**0.5 +1)) : # 어떤 수 x가 소수인지는 math.sqrt(x)까지만 나눠봐도 충분하니
    if array[i]:
        for j in range(2*i, n+1, i): array[j] = False
for i in range(2, n+1):
    if array[i]: sosu.append(i)


left, right = 0, len(sosu) - 1

while left<=right: # 등호 안붙여서 오답났었음.
    if n-sosu[left] == sosu[right]: 
        ans = [sosu[left], sosu[right]]
        left += 1
        right -= 1
    
    elif n-sosu[left] > sosu[right]:
        left+=1
    else : 
        right -= 1
    
print(ans)




