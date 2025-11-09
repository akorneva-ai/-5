height = float(input("Введите рост: "))
weight = float(input("Введите вес: "))

imt = weight/((height/100)**2)

if imt < 16:
    print("выраженный дефицит массы тела")
elif 16 <= imt <= 18.49:
    print("недостаточная масса тела")
elif 18.5 <= imt <= 24.99:
    print("норма")
elif 25 <= imt <= 29.99:
    print("избыточная масса тела")
elif 30 <= imt <= 34.99:
    print("ожирение первой степени")
elif 35 <= imt <= 39.99:
    print("ожирение второй степени")
else:
    print("ожирение третьей степени")
