# Строки в Python
# my_string_1 = 'Текст в одинарных кавычках'
# my_string_2 = "Текст в двойных кавычках"
# my_string_3 = '''Текст в тройных кавычках'''
# print(my_string_1)
# print(my_string_2)
# print(my_string_3)

# Кавычки внутри строки
# string_1 = "Двойные кавычки, 'внутри одинарные'"
# print(string_1)
# string_2 = 'Одинарные кавычки, "внутри двойные"'
# print(string_2)

# string_3 = "Двойные кавычки, \"внутри двойные\""
# print(string_3)
# string_4 = 'Одинарные кавычки, \'внутри одинарные\''
# print(string_4)

# string_5 = ''''Первая строка в одинарных кавычках', 
# "вторая строка в двойных кавычках"'''
# print(string_5)

# Форматирование строк
# f-строка
string_1 = 'солнечная'
string_2 = 'безоблачная'
# print(f'Сегодня {string_1} {string_2} погода')
# # Метод format
# print('Сегодня {0} {1} погода'.format(string_2, string_1))
# print('Сегодня {str_1} {str_2} погода'.format(str_2 = string_2, str_1 = string_1))
# Оператор % + s
print('Сегодня %s %s погода' % (string_1, string_2))