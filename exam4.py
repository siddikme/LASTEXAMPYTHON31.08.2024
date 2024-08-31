# ### 1 Question
# Кадом методҳои модули datetime ва randome - ро медонед. Бо мисолҳо фаҳмонед.


# Модуль datetime используется для работы с датой и временем в Python.
# Модуль random используется для генерации случайных чисел и выбора случайных элементов.
# random.randint(a, b)
# Возвращает случайное целое число в диапазоне от a до b включительно.
# solved:


# python
# import random

# random_number = random.randint(1, 10)
# print("Случайное число:", random_number)
# Результат:
# Случайное число: 7 (Результат может быть любым числом от 1 до 10.)


### 2 Question
# Кадом методхо ва функсияхоро барои кор бо файл медонед.

# Открытие файла
# Чтобы открыть файл, используйте функцию open(). Она возвращает объект файла, с которым можно работать.

# Чтение содержимого файла
# После открытия файла, можно прочитать его содержимое с помощью различных методов:

# read(): Читает весь файл сразу.

# Запись в файл
# Чтобы записать данные в файл, откройте его в режиме записи ('w') или добавления ('a'):

# write(): Записывает строку в файл
# Закрытие файла
# После завершения работы с файлом, его нужно закрыть с помощью метода close().
# solved:

# ### 3 Question
# Github чист? Командахои GitHub-ро фахмонед.

# GitHub — это платформа для разработки программного обеспечения, где разработчики могут хранить, управлять своим кодом и сотрудничать с другими разработчиками.
# Она основана на Git, системе контроля версий, которая позволяет отслеживать изменения в коде и управлять различными версиями проекта.
# С помощью GitHub вы можете управлять проектами, документировать их и сотрудничать с разработчиками по всему миру.

# git init
# Эта команда инициализирует новый репозиторий. Она создает скрытую папку .git в текущем каталоге, где хранятся все данные и версии проекта.
# git add
# Добавляет изменения в коде, чтобы их можно было сохранить. Например, можно добавить один файл или все файлы сразу.

# git commit -m
# Сохраняет изменения, которые были добавлены командой git add, в репозиторий. Нужно написать комментарий, который объяснит изменения.

# git push  -u origin main/master
# Отправляет сохраненные изменения из вашего компьютера на GitHub.

# git status
# Показывает, какие файлы были изменены, добавлены или готовы к сохранению.

# git branch -M
# Управляет ветками в репозитории. Можно создать новую ветку, посмотреть все ветки или переключиться на другую ветку.
# git remote add origin  ----siilka---
# привязываем наш проект в гит репозитор для дальнейших работ 
# solved:

# ### 1 Question
# Write a Python program to insert an element at a specified position into a given list.
# Напишите программу Python для вставки элемента в указанную позицию в заданный список.
# Барономае нависед дар Python, барои дохил кардани 
# [1, 1, 2, 3, 4, 4, 5, 1]
# # input
#     Enter an element: Sorbon
#     Index: 3
# # output
#     [1, 1, 2, "Sorbon", 3, 4, 4, 5, 1]


# my_list = [1, 1, 2, 3, 4, 4, 5, 1]
# element = input("Enter an element: ")
# index = int(input("Index: "))
# my_list.insert(index, element)
# print(my_list)
# solved:


# ### 2 Question
# Write program to print 2 days before, today, 2 days after / Напишите программу для печати позавчера, сегодня, послезавтра. / Барномаи нависед, то пареррӯз, имрӯз, фардои дигарро чоп кунад 

# from datetime import datetime, timedelta
# today = datetime.now()
# two_days_before = today - timedelta(days=2)
# two_days_after = today + timedelta(days=2)

# print("Two days before:", two_days_before.strftime("%Y-%m-%d"))
# print("Today:", today.strftime("%Y-%m-%d"))
# print("Two days after:", two_days_after.strftime("%Y-%m-%d"))
# solved:

# ### 3 Question
# Write a program to subtract five days from the current date / Напишите программу, которая вычитает пять дней из текущей даты.

# Input: 17.02.2024           Output: 12.02.2024

# from datetime import datetime, timedelta
# input_date = input("Enter a date (dd.mm.yyyy): ")


# date_object = datetime.strptime(input_date, "%d.%m.%Y")
# new_date = date_object - timedelta(days=5)
# output_date = new_date.strftime("%d.%m.%Y")
# print("Output:", output_date)
# solved:

# ### 4 Question
# Create a function that takes a string and returns the sum of vowels, where some vowels are considered numbers (Exactly use dictionary.). Создайте функцию, которая принимает строку и возвращает сумму гласных, где некоторые гласные считаются числами (Обязательно используйте словари).(A=4, E=3, I=1, O=0, U=0) 

# Input                                           Output
# sum_of_vowels("Do I get the correct output?")   10

# def sum_of_vowels(s):
#     vowel_values = {'A': 4, 'E': 3, 'I': 1, 'O': 0, 'U': 0}
#     s = s.upper()
#     total = 0
#     for char in s:
#         if char in vowel_values:
#             total += vowel_values[char]
#     return total

# s = input("Enter a string: ")
# result = sum_of_vowels(s)
# print(result)
 # solved:


# ### 5 Task
# Create a python program to read line number N from the following file.
# Создайте программу Python для чтения строки номер N из следующего файла.
# my_file.txt -> Hello world
#                TEST
#                Tajikistan
#                An apple
# # input
#     3
# # otput
#     Tajikistan

#                                   Уважаемый Учитель я создал еще один файл и превизал данный код в сушествуюший файл! 
#                                      вам нужно просто обратится по строкам вводя числа. Строки начинаются от '1'!


# filename = "my_file.txt"
# line_number = int(input("Enter the line number: "))

# try:
#     with open(filename, 'r') as file:
#         lines = file.readlines()

#     if 1 <= line_number <= len(lines):
#         print(lines[line_number - 1].strip())
#     else:
#         print("Line number out of range")
# except FileNotFoundError:
#     print("File not found")

# solved:




# ### 6 Question
# Write a program that replaces the content of all odd lines in a given file with a word that we input.
# Напишите программу, которая в заданном файле заменяет содержимое всех нечётных строк на слово, которое мы вводим.
# Барномае нависед, ки дар файли додашуда маълумоти хама сатрхои токро ба калимае, ки мо дохил мекунем, иваз кунад. 



#               Уважаемый учитель я и здесть тоже создал отделный файл где хранятся данные которые вы собственно можете изменит.
#               В задаче сказана изменять все строки под нечетным нумерациями.
#               напишитете свое слово которая будет внесена в мой файл под нечетными нумерациями
#               Потом проверьте файл и вы увидите изменение которые осушествятся благодаря вашем внесениям новых изменений

# filename = "raplace_odd_n.txt"
# word = input("Enter the word to replace odd lines: ")

# with open(filename, 'r+') as file:
#     lines = file.readlines()

# with open(filename, 'w') as file:
#     for i, line in enumerate(lines):
#         if i % 2 == 0:  
#             file.write(word + '\n')
#         else:
#             file.write(line)
# print("Program ended check the created file (raplace_odd_n.txt) ")
# solved:






# ### 7 Question
# Create a python program to generate a random password of the specified length.
# Создайте программу Python для создания случайного пароля указанной длины.
# # input
#     Enter the desired password length: 12
# # output
#     Generated password: Xy#7pLm$9oR5

# import random

# length = int(input("Enter the desired password length: "))
# letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# digits = "0123456789"
# punctuation = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
# characters = letters + digits + punctuation
# password = ''.join(random.choice(characters) for _ in range(length))

# print("Generated password:", password)
# solved:



# ### 8 Question
# Write a Python script to print a dictionary where the keys are numbers between 1 and N (both included) and the values are the square of the keys.
# Напишите сценарий Python для печати словаря, в котором ключами являются числа от 1 до N (оба включены), а значениями являются квадраты ключей.
# # input
#     15
# # output
#     {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}


# N = int(input())
# squares = {i: i * i for i in range(1, N + 1)}
# print(squares)
# solved:



# ### 9 Question
# Create a function that returns the number of times a character appears in each word in a sentence. Treat upper and lower case characters of the same letter as being identical. Создайте функцию, которая возвращает количество раз, когда символ встречается в каждом слове предложения. Считать символы верхнего и нижнего регистра одной и той же буквы идентичными.

# Input       
# char_appears("She sells sea shells by the seashore.", "s")

# Output
# [1, 2, 1, 2, 0, 0, 2]


# def char_appears(sentence, char):
#     char = char.lower()
#     words = sentence.lower().split()
#     return [word.count(char) for word in words]

# sentence = input("Enter a sentence: ")
# char = input("Enter the character to count: ")
# result = char_appears(sentence, char)
# print(result)
# solved:


# ### 10 Task
# Given a list of elements of any data types. Create a Python program to separate elements by their types and save them into a new dictionary.
# The keys of a dictionary must be of a data type, and its element must be data belonging to that type.
# Дан список элементов любых типов данных. Создайте программу Python для разделения элементов по их типам и сохранения их в новый словарь.
# Ключи словаря должны иметь тип данных, а его элементом должны быть данные, принадлежащие этому типу.
# # input
#     1 hello True 12 Muhammad
# # output
#     {"int": [1,12], "str": ["hello", "Muhammad"], "bool": [True]}


# elements = input("Enter ur text: ").split()
# result = {}
# for element in elements:
#     if element.isdigit():
#         key = "int"
#         value = int(element)
#     elif element in ["True", "False"]:
#         key = "bool"
#         value = element == "True"
#     else:
#         key = "str"
#         value = element
    
#     if key not in result:
#         result[key] = []
#     result[key].append(value)

# print(result)
# solved:
