#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random
import numpy as np


class Card:
    def __init__(self,name):
        list = [sorted([(random.randint(1,90)) for x in range(5)]) for x in range(3)]
        self.__list = [[],[],[]]
        for y in range(3):
            for x in list[y]:
                self.__list[y].append(str(x))

        self.__name = name

    def get_card(self):
        return self.__list

    def delete_keg(self, keg_name):
        for y in range(3):
            for x in range(5):
                if keg_name == self.__list[y][x]:
                    self.__list[y][x] = '-'

    def get_card_text(self):
        s = ' '
        return f"---- {self.__name} -----\n" \
               f"{s.join(self.__list[0])}\n" \
               f"{s.join(self.__list[1])}\n" \
               f"{s.join(self.__list[2])}\n" \
               f"--------------------------"


class Bag:
    def __init__(self):
        self.__bag = [str(x) for x in range(1,91)]
        self.__keg = ""

    def get_bag(self):
        return self.__bag

    def get_len(self):
        return len(self.__bag)

    def get_keg(self):
        random_index = random.randint(0,self.get_len() - 1)
        self.__keg = self.__bag[random_index]
        self.delete_keg(self.__keg)

    def get_current_keg(self):
        return self.__keg

    def delete_keg(self,keg_name):
        self.__bag.remove(keg_name)

    def print_bag_text(self):
        print(f"Новый бочонок:{self.__keg}(осталось {self.get_len()})")


class Player:
    def __init__(self,is_computer, bag):
        self.__bag = bag
        self.__is_computer = is_computer
        self.__card = Card("Карточка компьютера" if is_computer else "Ваша карточка")

    def print_card_text(self):
        print(self.__card.get_card_text())

    def make_choice(self):
        card = np.ravel(self.__card.get_card())
        new_keg = self.__bag.get_current_keg()
        if self.__is_computer:
            return self.make_computer_choice(card, new_keg)
        else:
            return self.make_human_choice(card, new_keg)

    def make_human_choice(self, card, new_keg):
        choice = str(input("Зачеркнуть цифру?y/n\n"))
        is_win = 0

        try:
            if choice == "y":
                if new_keg in card:
                    print("Хорошо! Играем дальше!")
                    self.__card.delete_keg(new_keg)
                else:
                    print("Цифры не было на карточке, вы проиграли!")
                    is_win = -1
            elif choice == "n":
                if new_keg not in card:
                    print("Хорошо! Играем дальше!")
                else:
                    print("Цифры не было на карточке, вы проиграли!")
                    is_win = -1
            else:
                raise ValueError

            if self.check_card(card):
                is_win = 1

            return is_win

        except ValueError:
            print("Вы ввели неверное значение, вы проиграли!")
            return False

    def make_computer_choice(self, card, new_keg):
        if new_keg in card:
            self.__card.delete_keg(new_keg)
            return 1 if self.check_card(np.ravel(self.__card.get_card())) else 0
        else:
            return 0

    def check_card(self, card):
        is_win = True

        for keg in card:
            if keg != '-':
                is_win = False
                break

        return is_win


bag = Bag()
human = Player(False, bag)
computer = Player(True,bag)
is_win = 0

while is_win == 0:
    bag.get_keg()
    bag.print_bag_text()
    human.print_card_text()
    computer.print_card_text()
    human_result = human.make_choice()
    computer_result = computer.make_choice()

    if human_result == -1:
        is_win = human_result
    elif human_result == 1:
        is_win = human_result
        print('Пользователь победил!')
    elif computer_result == 1:
        is_win = computer_result
        print('Компьютер победил')
    elif human_result == 1 and computer_result == 1:
        is_win = 1
        print('Игра завершилась ничьей')