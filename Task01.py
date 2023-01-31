number = float(input("Insert number: "))
while number != int(number):
    number *= 10
sum = 0
while number > 0:
    sum += number % 10
    number //= 10
print(int(sum))