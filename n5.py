dictionary = {"Торт": ['мука, сахар, яйца и другие ингридиенты торта', 1.99, 3200], 'Пирожное': ['мука, сахар и другие ингридиенты пирожного', 2.50, 600], 'Маффин': ['мука, сахар и другие ингридиенты маффина', 1.50, 300]}
keys = list(dictionary.keys())
def read_comp(dict, keys):
    i = 0
    while i < len(dict):
        print(keys[i], "состав:", dict.get(keys[i])[0])
        i += 1

def read_price(dict, keys):
    i = 0
    while i < len(dict):
        print(keys[i], "цена за 100г:", dict.get(keys[i])[1])
        i += 1

def read_weight(dict, keys):
    i = 0
    while i < len(dict):
        print(keys[i], "имеется грамм:", dict.get(keys[i])[2])
        i += 1

def read_info(dict, keys):
    i = 0
    while i < len(dict):
        print(keys[i], ":\nЦена за 100г:", dict.get(keys[i])[1], "\nИмеется грамм:", dict.get(keys[i])[2], "\nСостав:", dict.get(keys[i])[0], '\n')
        i += 1

def buy(dict, keys):
    basket = {}
    while True:
        print("Выберите товар, который желаете приобрести или 0 чтобы завершить покупку")
        i = 0
        while i < len(dict):
            print(keys[i], "-", i + 1)
            i += 1
        while True:
            choice = input()
            if choice.isdigit():
                choice = int(choice)
                if choice < 0 or choice > i:
                    print("Введите число, попадающее в поле от 0 до", i)
                else:
                    break
            else:
                print("Необходимо ввести числовое значение")
        if choice == 0: break
        choice -= 1
        print(keys[choice], ":\nЦена за 100г:", dict.get(keys[choice])[1], "\nИмеется грамм:",
              dict.get(keys[choice])[2], "\nСостав:",
              dict.get(keys[choice])[0], '\n')
        print("Введите сколько грамм продукта вы готовы купить или 0, чтобы отменить покупку")
        while True:
            weight = input()
            if weight.isdigit():
                weight = int(weight)
                if weight < 0:
                    print("Нужно ввести положительное количество грамм или 0")
                elif weight > dict.get(keys[choice])[2]:
                    print("Вы не можете приобрести больше продукта, чем есть в магазине")
                else:
                    break
            else:
                print("Необходимо ввести числовое значение")
        w = 0
        p = 0
        if basket.get(keys[choice]) != None:
            p = basket.get(keys[choice])[1]
            w = basket.get(keys[choice])[0]
        basket.update({keys[choice]: []})
        basket[keys[choice]] += [w + weight, p + weight * dict.get(keys[choice])[1] / 100]
        #Перезапись в меню магазина
        s = dict.get(keys[choice])[0]
        p = dict.get(keys[choice])[1]
        w = dict.get(keys[choice])[2]
        dict[keys[choice]] = [s, p, w - weight]
    k = list(basket.keys())
    i = 0
    total_price = 0
    print("Ваша корзина:")
    while i < len(k):
        print(k[i], "массой", basket.get(k[i])[0], "стоимость:", basket.get(k[i])[1])
        total_price += basket.get(k[i])[1]
        i += 1
    print("Итого к оплате", total_price)


while True:
    print("1 - прочесть составы товаров\n2 - посмотреть цены товаров\n3 - посмотреть количество товаров\n4 - посмотреть полную информацию о товарах\n5 - совершить покупку\n6 - выйти")
    i = input("Ваш выбор: ")
    if i not in ['1', '2', '3', '4', '5', '6']:
        print("Нужно ввести целое число от 1 до 6")
        continue
    if i == '1':
        read_comp(dictionary, keys)
    if i == '2':
        read_price(dictionary, keys)
    if i == '3':
        read_weight(dictionary, keys)
    if i == '4':
        read_info(dictionary, keys)
    if i == '5':
        buy(dictionary, keys)
        break
    if i == '6':
        break

