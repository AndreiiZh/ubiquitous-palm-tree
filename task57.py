import random

str1_4 = ''
for i in range(4):
    str1_4 = str1_4 + random.choice(list('0123456789'))
_list = 'abcdefghijklmnopqrstuvwxyz'
str5 = random.choice(list(_list))
newlist = _list.replace(str5, '')
str6 = random.choice(list(newlist))
str7_10 = random.choice(
    list(['1111', '0001', '1110', '1100', '0011', '0010', '0100', '1000', '0101', '1010', '1001']))

print(str1_4 + str5 + str6 + str7_10)
