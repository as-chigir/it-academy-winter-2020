"""Шоколадка. на подумать если есть желание. точного решения у меня нет**
   Определения:
   - Шоколадка - прямоугольник, размером n×m (n, m - натуральные).
   - Разлом - деление шоколадки на две части с натуральными размерами по прямой.
   - Долька - элемент шоколадки размером 1х1. Очевидно шоколадка состоит из n*m долек.
   - Кусок - элемент шоколадки произвольного (целочисленного размера).
  Определите:
   1) можно ли одним разломом отделить от шоколадки кусок площадью ровно k.
   2) можно ли отломить от шоколадки ровно k долек за некоторое количество разломов.
   3) можно ли отломить от шоколадки ровно k долек с помощью t разломов
"""


n = int(input("Ширина шоколадки: "))
m = int(input("Длина шоколадки: "))
k = int(input("Заданная площать куска шоколадки: "))
# for n * m => k:

if k % n == 0 or k % m == 0:
    print('Да, можно')
else:
    print('Нет, нельзя')
