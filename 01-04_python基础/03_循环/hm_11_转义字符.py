row = 1
while row <= 9:
    # 每行将col先置为1
    col = 1
    while col <= row:
        # print("%d * %d = %2d" % (col, row, row * col), end='   ')
        """
         `\t` 在控制台输出一个 **制表符**，协助在输出文本时 **垂直方向** 保持对齐
         `\n` 在控制台输出一个 **换行符**
        """
        print("%d * %d = %d" % (col, row, col * row), end="\t")
        col += 1
    print('')
    row += 1
