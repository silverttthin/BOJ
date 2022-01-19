def facto(n):
    if n == 1 or n== 0: return 1
    else:
        return n * pibo(n-1)

n = facto(int(input()))