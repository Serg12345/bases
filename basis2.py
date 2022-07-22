# Строки в Python
# my_string_1 = 'Текст в одинарных кавычках'
# my_string_2 = "Текст в двойных кавычках"
# my_string_3 = '''Текст в тройных кавычках'''
# print(my_string_1)
# print(my_string_2)
# print(my_string_3)

# Зарезервированные имена в Python
# import keyword
# list = keyword.kwlist
# for x in list:
# 	print(x)

# Преобразование типа данных в Python. int(), float(), str(), bool()
# string_1 = '10'
# print(string_1, type(string_1))
# string_2 = '5.75'
# print(string_2, type(string_2))

# my_int = int(string_1)
# print(my_int, type(my_int))
# my_float = float(string_2)
# print(my_float, type(my_float))

# my_string = str(my_int)
# print(my_string, type(my_string))

# my_bool = bool(my_string)
# print(my_bool, type(my_bool))

# Уникальный идентификатор 
# name = 'Олег'
# print(id(name))
# age = '30'
# print(id(age))
# age = '30'
# print(id(age))
# age = '31'
# print(id(age))
# age2 = '30'
# print(id(age2))

# Ввод данных. input()
# name = input("Введите ваше имя: ")
# print(name)
# print(type(name))
# age = input("Сколько вам лет? :")
# print(age)
# print(type(age))
# age2 = int(input("Сколько вам лет? :"))
# print(age2)
# print(type(age2))

# Операторы сравнения
# Оператор равенства ==
# print(5 == 5) # True
# print(5 == 5.0) # True
# print(5 == '5') # False
# print('5' == '5') # True
# print('5' == '5.0') # False
# Оператор неравенства !=
# print(5 != 5) # False
# print(5 != 50) # True
# print(5 != '5') # True
# Операторы больше >, меньше < 
# print(5 > 50) # False
# print(5 < 50) # True
# print(5 < "50")
# Операторы больше или рано >=, меньше или равно <=
# print(5 >= 5) # True
# print(5 <= 50) # True

# Оператор if (оператор условия, сравнивает результат, True или False)
# if выражение 1:
#     блок кода 1
# elif выражение 2:
#     блок кода 2
# else:
#     блок кода 3
# x = 5
# if x:
# 	print('Выражение равно True')
# else:
# 	print('Выражение равно False')

# print('Выражение равно True') if x else print('Выражение равно False')

# Цикл while
# x = 1
# while x <= 5:
# 	print(x, end=' ')
# 	x = x + 1

# Цикл for
# s = 'Сегодня хорошая погода'
# for x in s:
# 	if x == ' ':
# 		continue
# 	print(x, end=' ')
# print('')
# for x in s:
# 	if x == '!':
# 		print('Восклицательный знак есть')
# 		break
# 	print(x, end=' ')
# else:
# 	print('Восклицательного знака нет')

# Функция print. Меняем символ между значениями аргументов
# print('Сегодня', 'хорошая', 'погода', sep='_')
