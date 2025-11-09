d1 = int(input("Введите кол-во улыбок в первый день: "))
d2 = int(input("Введите кол-во улыбок во второй день: "))
d3 = int(input("Введите кол-во улыбок в третий день: "))

smiles = [d1, d2, d3]

max_num = max(smiles.count(d1), smiles.count(d2), smiles.count(d3))

print(max_num)