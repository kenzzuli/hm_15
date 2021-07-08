def multiple_table():
    row = 1
    while row <= 9:
        # 每行将col先置为1
        col = 1
        while col <= row:
            print("%d * %d = %2d" % (col, row, row * col), end='   ')
            col += 1
        print('')
        row += 1
