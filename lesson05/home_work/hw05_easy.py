# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def create_dir():
    import os
    dir_name = input("Напиши имя папки, которую мы будем создавать: ")
    if not dir_name:
        print("Необходимо указать имя папки")
    else:
        dir_path = os.path.join(os.getcwd(), dir_name)
        try:
            os.mkdir(dir_path)
            print('Директория {} создана'.format(dir_name))
        except:
            print('директория {} уже существует'.format(dir_name))

#создание директорий с 1 по 9
def create_dirs():
    import os
    dir_name = input("Напиши имя папок, которую мы будем создавать: ")
    n = input("Введите кол-во папок: ")
    if not dir_name:
        print("Необходимо указать имя папки")
    else:
        dir_path = os.path.join(os.getcwd(), dir_name)
        try:
            i = int(n or 9)
            while i != 0:
                os.mkdir(f"{dir_path}_{i}")
                i -= 1
            print('Директории созданы')
        except:
            print('директория {} уже существует'.format(dir_name))

def delete_dir():
    import os
    dir_name = input("Напиши имя папки, которую мы будем удалять: ")
    if not dir_name:
        print("Необходимо указать имя папки")
    else:
        try:
            os.rmdir(dir_name)
            print ("Директория {} удалена")
        except:
            print('директория {} не существует'.format(dir_name))

def go_dir():
    import os

    dir_name = input("Ваша директория '{}'.Напишите имя папки, в которую мы перейдем: ".format(os.getcwd()))
    if not dir_name:
        print("Необходимо указать имя папки")
    else:
        try:
            os.chdir(dir_name)
            print('Текущая папка {}'.format(dir_name))
        except FileExistsError:
            print('директория {} не существует'.format(dir_name))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def show_dir():

    import os
    for name in os.listdir():
     print(name)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file():
    from shutil import copyfile
    import os
    cur_file = os.path.basename(__file__)
    print(cur_file)

    new_file = input("Введите новое имя файла, который нужно скопировать: ")
    if not new_file:
        print("Необходимо указать имя файла")
    else:
        try:
            copyfile(cur_file, new_file)
            print(f"Файл {new_file} скопирован")
        except:
            print("Что-то пошло не так")