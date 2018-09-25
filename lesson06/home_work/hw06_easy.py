# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
class triangle:

    def _init_(self, dotone,dottwo, dotthree,get_s, get_p):
        self.dotone = dotone
        self.dottwo = dottwo
        self.dotthree = dotthree


    def get_s(self):
        self.get_s = (int(self.dotone)+int(self.dottwo)+int(self.dotthree))/2
      print ("Площадь треугольника:", get_s)

    def heigh(self):
        self.height_1 = (2 * int(self.get_s))/ int(self.dotone)
        self.height_2= (2 * int(self.get_s))/int(self.dottwo)
        self.height_3 = (2 * int(self.get_s))/ int(self.dotthree)

        print ("Высоты вашего треугольника равны:" +
               "\nAH: ",self.height_1, "\nAB: ",  self.height_2, "\nAC: ",  self.hight_3)

    def get_perimeter(self):
        self.get_perimeter = int(self.dotone)+int(self.dottwo)+int(self.dotthree)
        print ("Периметр треугольника:", self.get_perimeter)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class trapezium:

def _init_(self):
    self.dotone = dotone
    self.dottwo = dottwo
    self.dotthree = dotthree
    self.dotfour = dotfour

    def check(self):
        import math
        self.side_1 = math.sqrt(((self.dotone - self.dottwo) ** 2)
        self.side_2 = math.sqrt(((self.dotthree - self.dotfour) ** 2)

        if self.side_1 == self.side_2:
            print("Трапеция равнобокая")
        else:
            print("Трапеция неравнобокая")

    def get_perimeter(self):
        self.get_perimeter = int(self.dotone)+int(self.dottwo)+int(self.dotthree)
        print ("Периметр трапеции:", self.get_perimeter)

    def get_s(self):
        self.get_s = (int(self.dotone)+int(self.dottwo)+int(self.dotthree))/2
      print ("Площадь трапеции:", self.get_s)

    def len_side(self):
        import math
        c = math.sqrt(((self.dottwo - self.dotone) ** 2))
        d = math.sqrt(((self.dotfour - self.dotthree) ** 2))
        a = math.sqrt(((self.dotthree - self.dottwo) ** 2))
        b = math.sqrt(((self.dotfour - self.dotone) ** 2))

        print("Длина сторон: " + "\nAB: ", a, "\nBC: ", c, "\nCD: ", d, "\nDC: ", b)