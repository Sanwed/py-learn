calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(str_):
    count_calls()

    return len(str_), str_.upper(), str_.lower()


def is_contains(str_, list_):
    count_calls()

    lower_list = []
    for i in list_:
        if type(i) is str:
            lower_list.append(i.lower())

    return str_.lower() in lower_list


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 32, 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
