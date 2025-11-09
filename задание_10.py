pin = int(input("Придумайте пинкод: "))

if 1900 <= pin <= 2050:
    print("ERROR")
else:
    #Извлекаем цифры из пинкода
    n1 = pin // 1000
    n2 = (pin // 100) % 10
    n3 = (pin // 10) % 10
    n4 = pin % 10

    if d1 != d2 and d1 != d3 and d1 != d4 and d2 != d3 and d2 != d4 and d3 != d4:
        print("OK")
    else:
        print("ERROR")