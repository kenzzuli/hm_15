from queue import Queue

q = Queue(3)  # 最多可以放3条数据
q.put("hi")
q.put(1)
# 判断队列是否满了
print(q.full())  # False
q.put([1, 2, 3])
print(q.full())  # True

try:
    q.put(4, True, 2)  # 等待2s，如果还无法放入队列，抛出异常
except:
    print("队列已满，当前数据数量为: %d" % q.qsize())

try:
    q.put_nowait(4)  # 不等待，直接放，如果队列已满，直接抛出异常
except:
    print("队列已满，当前数据数量为: %d" % q.qsize())

# 正确的存入队列方式
if not q.full():
    q.put_nowait(4)

# 正确的读取方式
if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())
