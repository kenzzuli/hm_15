import time

num = 0


def test(times):
    global num
    for i in range(times):
        num += 1
    print(num)


if __name__ == '__main__':
    start = time.time()
    times = 200000000
    test(times)
    end = time.time()
    print(end - start)

# 11.901100635528564
