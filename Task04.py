from random import random, randint

#Здесь мы задаём список размерностью который вводит пользователь.
N = int(input('Введите число'))
numbers = []
for i in range(N):
    numbers.append(randint(-N, N + 1))
#Выводим список на экран и находим произведение 2 значения списка с 4.
print(numbers)
print(numbers[1] * numbers[3])

#Создаём файл для чтения где будем доставать позиции для вычесления и закрываем файл.
f = open('file.txt', 'w')
while True:
    s = input('Укажите позицию для вычисления - ')
    if s == "":
        break
    f.write(s + "\n")
f.close()

#Здесь открываем файл чтобы произвести вычисление значений которые вытащили.
result = 1
f = open('file.txt', 'r')
for line in f:
    if line == "":
        break
    result *= numbers[int(line)]
f.close()
print(result)