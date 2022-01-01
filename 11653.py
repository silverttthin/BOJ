n = 9991
#내코드
# for i in range(2, n+1):
#     while(1):
#         if n%i == 0:
#             print(i)
#             n = n // i
#         else: break  

i=2
while n!=1:
    if n % i == 0: 
        n //= i
        print(i)
    else: i+=1

