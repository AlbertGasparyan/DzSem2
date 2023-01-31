S = int(input("Введите сумму 2 чисел "))
P = int (input("Введите произведение 2 чисел "))
result=0
for i in range(1, P//2):
    if (P % i == 0 and P/i + i == S):
        result=1
        break
if(result):
    print (f'Задуманные числа {i} и {P//i}')
else:
    print('Решения среди целых чисел нет')