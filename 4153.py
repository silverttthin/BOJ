import sys
sys.stdin = open("input.txt", "rt")

while True:
    array = sorted(list(map(int, input().split())))
    if array[0] == 0 : break
    print("right" if array[0]**2 + array[1]**2 == array[2]**2 else "wrong")
    