def print_line():
    """定义一个 `print_line` 函数能够打印 `*` 组成的 **一条分隔线**"""

    print('*' * 50)


print_line()


def print_everything(char: str) -> object:
    """定义一个函数，能够打印任意字符组成的分割线"""

    print(str(char) * 50)


print_everything(5)
print_everything('a')
print_everything('*')
print_everything("$%")


def print_a_char_n_times(char: str, n: int) -> object:
    """

    :param char:字符 
    :param n:重复次数 
    """
    print(str(char) * n)


print_a_char_n_times(5, 5)
print_a_char_n_times('*', 10)
print_a_char_n_times(100, 5)


def print_multiple_lines(char, times, lines):
    """定义一个函数，能够打印任意字符任意次数任意行数
    :param char: 要打印的字符
    :param times: 字符每行重复的次数
    :param lines: 重复的行数
    """

    i = 0
    while i < lines:
        print_a_char_n_times(char, times)
        i += 1


print_multiple_lines(4, 10, 5)
print_multiple_lines('%', 50, 2)


def test_for_document(i: int, j: int, k: int) -> int:
    """
    :rtype: int
    :param i: 字符
    :param j: 次数
    :param k: 行数
    """
    print(i, j, k)


test_for_document(1, 2, 3)

name = "Peter"