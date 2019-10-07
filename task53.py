print('Введите точки a, b, c, d, e, f, g, h')
a = int(input('a = : '))
b = int(input('b = : '))
c = int(input('c = : '))
d = int(input('d = : '))
e = int(input('e = : '))
f = int(input('f = : '))
g = int(input('g = : '))
h = int(input('h = : '))

l1 = (a - e) * (h - f) - (b - f) * (g - e)
l2 = (c - e) * (h - f) - (d - f) * (g - e)

if (l1 < 0 and l2 < 0) or (l1 > 0 and l2 > 0):
    print('Точки a, d и c, d принадлежат одной и той же полуплоскости')
else:
    print('Точки a, d и c, d не принадлежат одной и той же полуплоскости')
