print('Задача 3. Следим за расписанием')

# После выполненной задачи Вася устал и понял, что весь следующий день ему придётся восстанавливать силы. Вася решил, что работать он будет только в чётные дни и написал небольшую программу, которая поможет ему не пропустить рабочий день.

# Напишите программу, которая проверяет, чётное ли число ввёл пользователь, и выводит соответствующее сообщение. 

# Подсказка: для проверки чётности используйте оператор %.

number = int(input("Введите число: "))

if number % 2 == 0:
  print("Введённое число " + str(number) + ", четное")
else:
  print("Введённое число " + str(number) + ", нечётное")
