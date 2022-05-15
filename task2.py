import sys

POSITON = {
    0: 'Точка лежит на окружности',
    1: 'Точка принадлежит кругу',
    2: 'Точка не принадлежит кругу'
}


class Point:
    """
    Класс описания точки.
    Имеет атрибуты координат по оси x и оси y.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_coordinates_from_args(arg: int) -> list:
    """
    Функция получения координат из параметра в командной строке.
    На вход принимает номер агрумента.
    Возвращает список с коррдинатами.
    """
    with open(sys.argv[arg]) as f:
        lines = f.read().splitlines()
        coordinate = [line.split(' ') for line in lines]
        return coordinate


def get_center_and_radius(coordinate: list):
    """
    Функция создания центра с заданными координатами.
    А также получение заданного радиуса.
    На вход принимает список с координатами.
    Возвращает объект класса Point и радиус.
    """
    center = Point(float(coordinate[0][0]), float(coordinate[0][1]))
    r = float(coordinate[1][0])
    return center, r


def get_coordinates_point(coordinate: list) -> list:
    """
    Функция создания точки с заданными координатами.
    На вход принимает список с координатами.
    Возвращает объект класса Point.
    """
    point = Point(float(coordinate[0]), float(coordinate[1]))
    return point


def get_point_position(center: object, r: float, point: object) -> int:
    """
    Функция получения позиции точки по отношению к окружности.
    На вход принимает объект класса Point с координатами центра окружности,
    радиус окружности, объект класса Point c координатами точки.
    Возращает число:
        - точка лежит на окружности - 0,
        - точка принадлежит кругу - 1,
        - точка не принадлежит кругу - 2.
    """
    sum_sqr_coord = (point.x - center.x)**2 + (point.y - center.y)**2
    if sum_sqr_coord < r**2:
        return 1
    elif sum_sqr_coord > r**2:
        return 2
    return 0


def main():
    center_and_r = get_coordinates_from_args(1)
    points = get_coordinates_from_args(2)
    c, r = get_center_and_radius(center_and_r)
    for point in points:
        p = get_coordinates_point(point)
        yield get_point_position(c, r, p)


if __name__ == '__main__':
    for i in main():
        print(f'{i} - {POSITON[i]}')
