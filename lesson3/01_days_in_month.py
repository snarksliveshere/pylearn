# -*- coding: utf-8 -*-

import sys

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


if not isint(user_input):
    print("shit")
    sys.exit(1)

month = int(user_input)

if month == 1:
    print(31)
elif month == 2:
    print(28)
elif 2 < month <= 12:
    print(32)
else:
    print("no such month")

#
# print('Вы ввели', month)


