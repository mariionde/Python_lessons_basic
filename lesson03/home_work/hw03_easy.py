# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.5 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    pass


print(my_round(2.1234567, 5)) # 2.12346
print(my_round(2.1999967, 5)) # 2.20000
print(my_round(2.9999967, 5)) # 3.00000


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):

    ticket_number = str(ticket_number)
    ticket_list = []

    for digit in ticket_number:
        ticket_list.append(int(digit))

    a = ticket_list[0:3]
    b = ticket_list[3:6]
    left_sum = sum(a)
    right_sum = sum(b)
    if left_sum == right_sum:
        return ("Ваш билет выиграл")
    else:
        return ("Вам обязательно повезет в следующий раз!")


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
