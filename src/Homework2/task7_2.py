"""https://acmp.ru/index.asp?main=task&id_task=61
   Известны результаты каждой из 4х четвертей
   баскетбольной встречи. Нужно определить победителя
   матча. Побеждает команда, набравшая больше очков
   в течение всего матча.
"""


A1 = int(input('Первая четверть, результат команды А:'))
A2 = int(input('Вторая четверть, результат команды А:'))
A3 = int(input('Третья четверть, результат команды А:'))
A4 = int(input('Четвертая четверть, результат команды А:'))
B1 = int(input('Первая четверть, результат команды B:'))
B2 = int(input('Вторая четверть, результат команды B:'))
B3 = int(input('Третья четверть, результат команды B:'))
B4 = int(input('Четвертая четверть, результат команды B:'))

a = A1 + A2 + A3 + A4
b = B1 + B2 + B3 + B4

if a == b:
    print('Ничья')
elif a < b:
    print('Победитель - команда B')
else:
    print('Победитель - команда A')
