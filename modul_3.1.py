calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):                       # Принимает аргумент - строку и возвращает кортеж из:
                                               # длины этой строки, строку в верхнем регистре, строку в нижнем регистре
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):       # Принимает два аргумента: строку и список, и возвращает True,
                                               # если строка находится в этом списке, False - если отсутствует
    count_calls()
    string_lower = string.lower()
    return any(string_lower == item.lower()
               for item in list_to_search)

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)