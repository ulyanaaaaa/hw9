""" На столе лежат n монеток. Некоторые из них лежат
вверх решкой, а некоторые – гербом. Определите
минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той
же стороной. Выведите минимальное количество монет,
которые нужно перевернуть """

""" 
import random

monetki = int(input("Введите количество монеток: "))

print(f'\nКоличество монеток на столе: {monetki}')

reshka = 0
orel = 1
count_reshki = 0
count_orly = 0

for i in range(monetki):
    storona = random.randint(0, 1)
    print(storona)
    if storona == reshka:
        count_reshki = count_reshki + 1
    if storona == orel:
        count_orly = count_orly + 1


if count_reshki > count_orly:
    print(f'Нужно перевернуть {count_orly} монеток')
if count_orly >= count_reshki:
    print(f'Нужно перевернуть {count_reshki} монеток')
"""

""" Петя и Катя – брат и сестра. Петя – студент, а 
Катя – школьница. Петя помогает Кате по математике. Он 
задумывает два натуральных числа X и Y (X,Y≤1000), а Катя 
должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа. """

"""
import random

chislo_odin = random.randint(0, 1000)
chislo_dwa = random.randint(0, 1000)

#print(chislo_odin, chislo_dwa)

summa = chislo_odin + chislo_dwa
proizvedenie = chislo_odin * chislo_dwa

print(f'\nСумма двух чисел равна: {summa}\nПроизведение двух чисел равно: {proizvedenie}')

diskrimenant = (summa*summa - 4*proizvedenie) ** (0.5)
print(f'\nЧисло 1 равно: {(summa + diskrimenant) / 2}\nЧисло 2 равно {(summa - diskrimenant) / 2}')
"""

"""
Требуется вывести все целые степени двойки (т.е. числа 
вида 2k), не превосходящие числа N.
"""

maksimalnoe_chislo = int(input("Введите число до которого мы выводим степени: "))

begin = 1
print(f'Целочисленные степени двойки до числа {maksimalnoe_chislo}:\n')
while begin*2 <= maksimalnoe_chislo:
    begin = begin * 2
    print(begin)
