first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(s[0]) - len(s[1]) for s in zip(first, second) if len(s[0]) != len(s[1]))
second_result = (len(first[s]) == len(second[s]) for s in range(len(first)))


print(list(first_result))
print(list(second_result))