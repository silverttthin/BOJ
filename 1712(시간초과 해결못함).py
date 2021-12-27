import sys
input = sys.stdin.readline

n = 1

a,b,c = map(int, input().split())

if b>=c :   # b(가변비용)가 c(판매가)보다 더 크거나 같다면 a가 0이더라도 영원히 이득 못봄.
    print(-1)
    exit(0)

while(a+b*n >= c*n):
    n += 1

print(n)