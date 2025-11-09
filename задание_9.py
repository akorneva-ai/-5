h1, h2, h3 = map(int, input().split())

if h1 > h2 and h2 > h3:
    print(h1, h2, h3)
elif h1 > h3 and h3 > h2:
    print(h1, h3, h2)
elif h2 > h1 and h1 > h3:
    print(h2, h1, h3)
elif h2 > h3 and h3 > h1:
    print(h2, h3, h1)
elif h3 > h1 and h1 > h2:
    print(h3, h1, h2)
else:
    print(h3, h2, h1)