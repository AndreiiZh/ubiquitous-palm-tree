print('Введите три числа: ')
a = int(input())
b = int(input())
c = int(input())
if a >= b:
    if b >= c:
        print('Ваши числа: ', a * 2, b * 2, c * 2)
else:
    print(abs(a), abs(b), abs(c))
