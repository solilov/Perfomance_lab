"""
Скрипт для получения пути по которому,
двигаясь интервалом длины m по  заданному массиву,
концом будет являться первый элемент.

n - количество элемнетов в массиве.
m - интервал движения по массиву.

Пример:
n = 4, m = 3

Круговой массив: 1234. При длине обхода 3 получаем интервалы: 123, 341.
Полученный путь: 13.
"""
import sys


n, m = int(sys.argv[1]), int(sys.argv[2])

start_interval = 1
while True:
    print(start_interval, end='')
    start_interval = (start_interval + m - 2) % n + 1
    if start_interval == 1:
        break
print()
