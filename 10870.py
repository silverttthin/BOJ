def pibo(n: int) -> int:
    if n == 0 : return 0
    elif n == 1 : return 1
    else: return pibo(n-1)+ pibo(n-2)
    

n = pibo(10)
print(n)