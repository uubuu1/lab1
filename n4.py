size = int(input("Введите размер словаря: "))
mydict = {}
i = 0
while i < size:
    mydict[int(input("Введите ключ: "))] = int(input("Введите значение: "))
    i = i + 1
a = sorted(mydict, key=mydict.get)
v = mydict.values()
i = 0
print("По возрастанию: ", end='')
while i < len(a):
    print(f"{a[i]}: {mydict[a[i]]}; ", end='')
    i = i + 1
print("\nПо убыванию: ", end='')
i = len(a) - 1
while i >= 0:
    print(f"{a[i]}: {mydict[a[i]]}; ", end='')
    i = i - 1