# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random


n = random.randint(0,100)
list = [i for i in range(n)]
list_2 = [i**2 for i in list]


print (list)
print (list_2)




# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

try:
    fruits_1 = input("Введи фрукты через ',':")
    fruits_2 = input("Введи фрукты через ',':")
    list_1 = [i.replace(" ", "") for i in fruits_1.split(",")]
    list_2 = [i.replace(" ", "") for i in fruits_2.split(",")]

    result = list(set(list_1) & set(list_2))
    print(result)

except ValueError:
    print("Мне нужен список!")

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random

n = random.randint(0, 100)
list = [i for i in range(random.randint(0, 100))]
list_2 = [i for i in list if i % 3 == 0 and i % 4 != 0 and i > 0]



print(list)
print(list_2)