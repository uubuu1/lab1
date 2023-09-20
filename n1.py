print("Введите число")
while True:
    inp = input()
    if inp.isdigit(): break
    print("Введите числовое значение")
past = 0
while inp > 0:
    number = inp % 10
    inp = inp // 10
    if past > number:
        print("Последовательность цифр не является упорядоченной по убыванию при просмотре справа налево")
        break
    past = number
else:
    print("Последовательность цифр является упорядоченной по убыванию при просмотре справа налево")