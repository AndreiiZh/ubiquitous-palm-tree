def task26(a):
    print(sorted(list(filter(lambda x: x.count('а') >= 2, a.split()))))


task26('алабама, альфа самка капец собака канава стул вата оса дамба')
