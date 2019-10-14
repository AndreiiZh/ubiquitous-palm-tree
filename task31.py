def task31(str):
    s = len(str)
    if s > 5:
        print(str[:3], str[-3:])
    else:
        print(str[0] * s)


task31('kasljsfdfksj jkjksja')
