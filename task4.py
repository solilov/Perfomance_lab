import sys


def get_arg() -> list:
    """
    Функция получения массива чисел из файла переданного как
    аргумент в командной строке.
    Возвращает список.
    """
    with open(sys.argv[1]) as data:
        nums = data.read().splitlines()
        return [int(i) for i in nums]


def calc_min_number_moves(nums: list) -> int:
    """
    Функция подсчета минимального количества шагов,
    требуемых для приведения всех элементов к одному числу.
    На входит принимает список с числами.
    Возвращает число шагов.
    """
    nums = sorted(nums)
    ind_avg_elem = len(nums) // 2
    count = 0
    for i in nums:
        while i != nums[ind_avg_elem]:
            if i < nums[ind_avg_elem]:
                i += 1
                count += 1
            elif i > nums[ind_avg_elem]:
                i -= 1
                count += 1
    return count


def main():
    nums = get_arg()
    return calc_min_number_moves(nums)


if __name__ == '__main__':
    print(main())
