'''
종말의 숫자란 어떤 수에 6이 적어도 3개이상 연속으로 들어가는 수를 말한다. 제일 작은 종말의 숫자는 666이고, 그 다음으로 큰 수는 1666, 2666, 3666, .... 과 같다.

따라서, 숌은 첫 번째 영화의 제목은 세상의 종말 666, 두 번째 영화의 제목은 세상의 종말 1666 이렇게 이름을 지을 것이다. 
일반화해서 생각하면, N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 숫자) 와 같다.

숌이 만든 N번째 영화의 제목에 들어간 숫자를 출력하는 프로그램을 작성하시오. 숌은 이 시리즈를 항상 차례대로 만들고, 다른 영화는 만들지 않는다.

입력 n은 1~10000 숫자다.

666 1666 2666 3666 4666 5666 6660 6661 6662 6663 6664 6665 6666 6667 6668 6669 7666 8666 9666 

뭔지 도저히 모르겠다. 일단 666부터 시작하여 전부다 검사해보자. 그게 브루트포스니까

1씩 더하면서 다른 숫자가 될때마다 6이 3번 이상 연속되는지 파악하자. 

'''
# n = int(input())
n = 500
cnt = 0
num = 666

while True:
    if '666' in str(num):
        cnt += 1
        if cnt == n : break

    num += 1
print(num)




