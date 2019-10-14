sentence = 'алабама  альфа самка капец собака канава    стул вата  оса дамба'
s = sentence.split()
i = s.index(min(s, key=len))
j = sentence.index(max(s, key=len))
s[i], s[j] = s[j], s[i]
print('Начальный текст: ', ''.join(sentence))
print('Сортированный текст: ', ' '.join(s))


