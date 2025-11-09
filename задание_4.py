while True:
    num = int(input("Введите число: "))

    if num <= 100:
        if 11<= num <= 19:
            print(num, "попугаев")
        elif num % 10 == 1:
            print(num, "попугай")
        elif 2 <= num % 10 <= 4:
            print(num, "попугая")
        else:
            print(num, "попугаев")
        break
    else:
        print("Введите число от 1 до 100!")
