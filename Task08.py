

quan_money = int(input("Введите кол-во монет:"))

def get_random_money(quan):
    count0, count1 = 0, 0
    for el in range(quan_money):
        import random
        coin=random.randint(0,1)
        print(coin,end=' ')
        if coin>0:
            count1+=1
        else:
            count0+=1
    print()
    print(f'Нужно перевенуть {count0} монет' if count0 < count1 else f'Нужно перевернуть {count1} монет')

get_random_money(quan_money)
