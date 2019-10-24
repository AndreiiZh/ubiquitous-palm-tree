def task44(str):
    x = list(str)
    i = 0
    mx = 0
    for j in x:
        if j == ' ':
            i += 1
        elif i > mx:
            mx = i
        else:
            i = 0

    print('Максимальное повторение " ": ', mx)


task44('xf                  lllls   skkds dsf     fs sfsf  aa            .')
