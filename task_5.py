print('Задача 5. Модуль числа')

# Создайте программу, которая найдёт модуль очередного числа x. Если число x отрицательное, то она должна перевести его в положительное, а в конце на экране должен быть модуль введённого числа.

# Пример:
# Ввели 5, ответ 5
# Ввели −7, ответ 7

# Подсказка: в некоторых случаях достаточно переприсвоить переменную со знаком минус.

number = int(input("Введите число: "))
converting_number = - number

if number > 0:
  print("Ввели", str(number) + ", ответ", number)
else:
  print("Ввели", str(number) + ", ответ", converting_number)
