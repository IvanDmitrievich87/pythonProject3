def get_multiplied_digits(number):
    str_number = str(number)                                       # Преобразуем число в строку для удобного доступа к цифрам
    if len(str_number) > 1:                                        # Если длина str_number больше 1, продолжаем
        first = int(str_number [0])                                # Отделяем первую цифру и преобразуем её в int
        return first * get_multiplied_digits(int(str_number [1:])) # Рекурсивно вызываем функцию для оставшихся цифр
    return int(str_number)                                         # Если осталась только одна цифра, возвращаем её
result = get_multiplied_digits(40203)
print(result)