inp = list(input("Введите список, разделяя элементы пробелами\n"))
mylist = list()
numb = 0
while inp != []:
    taken = inp.pop(0)
    if taken == '-':
        taken = inp.pop(0)
        while taken != ' ' and inp != []:
            numb = numb * 10 - int(taken)
            taken = inp.pop(0)

    while taken != ' ' and inp != []:
        numb = numb * 10 + int(taken)
        taken = inp.pop(0)

    if inp == []:
        numb = numb * 10 + int(taken)

    if taken == ' ' or inp == []:
        mylist.append(numb)
        numb = 0
print(mylist)
i = 0
zero = 0
sum = 0
asum = 0
while i < len(mylist):
    if mylist[i] == 0:
        zero = 1
    if zero == 1:
        asum = asum + mylist[i]
    if mylist[i] >= 0:
        sum = sum + mylist[i]
    else:
        mylist.pop(i)
        i = i - 1
    i = i + 1

print(f"Сумма положительных элементов списка равна {sum}")
if zero == 1:
    print(f"Сумма элементов после первого нуля равна {asum}")
else:
    print("Нулевого элемента в списке нету поэтому сумму посчитать нельзя")
print(f"Список после удаления отрицательных элементов: {mylist}")
