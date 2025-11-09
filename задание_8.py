N = int(input("Введите канты: "))

#1 галлеон = 17 сиклей, 1 сикль = 29 кнатов

gal = N // 493 #17*29 = 493
N = N % 493
sik = N // 29
kant = N % 29

if gal != 0 and sik != 0 and kant != 0:
    print(gal, "галлеонов", sik, "сиклей", kant, "кантов")
elif gal != 0 and sik == 0 and kant != 0:
    print(gal, "галлеонов", kant, "кантов")
elif gal != 0 and sik != 0 and kant == 0:
    print(gal, "галлеонов", sik, "сиклей")
else:
    print("0")