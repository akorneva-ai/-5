N = int(input())

n1 = N // 1000
n2 = (N // 100) % 10
n3 = (N // 10) % 10
n4 = N % 10

if d1 == d4 and d2 == d3:
    print("настоящее")
else:
    print("кривое")