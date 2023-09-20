word = input("Введите слово:\n")
caps = -1
count_up = 0
count_down = 0
glas = 0
i = 0
while i < len(word):

    if ord(word[i]) >= ord('A') and ord(word[i]) <= ord('Z'):
        if caps == 1:
            count_up = count_up + 1
        caps = 1

    elif ord(word[i]) >= ord('a') and ord(word[i]) <= ord('z'):
        if caps == 0:
            count_down = count_down + 1
        caps = 0

    else:
        caps = -1

    if word[i] in ['e', 'y', 'u', 'i', 'o', 'a', 'E', 'Y', 'U', 'I', 'O', 'A']:
        glas = glas + 1
    i = i + 1
print(f"Пар в верхнем регистре - {count_up}\nПар в нижнем регистре - {count_down}\nГласных - {glas}")
