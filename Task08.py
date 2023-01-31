from random import random, randint


quan_money = int(input("Введите кол-во монет:"))

def GetListMoney(number):
    list_money = []
    for el in range(quan_money):
        list_money.append(randint(0,1))
    return print(list_money)

ListMoney= GetListMoney(quan_money)

