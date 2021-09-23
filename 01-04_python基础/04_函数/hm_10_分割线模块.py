def print_a_char_n_times(char: str, n: int) -> object:
    """打印一个字符N次
    :param char:字符
    :param n:重复次数
    """
    print(str(char) * n)


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


name = "Peter"
