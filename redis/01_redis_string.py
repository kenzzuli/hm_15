from redis import *

if __name__ == '__main__':
    # 创建一个strict redis对象，链接redis数据库
    try:
        sr = StrictRedis()
        # 添加一个kv对
        # res = sr.set('name', 'ken')
        # print(res)  # True

        # 获取name对应的值
        # print(sr.get('name'))

        # 更改name对应的值
        # res = sr.set('name', 'liulei')
        # print(res) # True
        # print(sr.get('name')) # liulei

        # 删除name及其对应的值
        # res = sr.delete('name')
        # print(res)  # 1

        # 删除多个键值对
        # res = sr.delete('a1', 'a3')
        # print(res)  # 2

        # 获取数据库中所有的键
        print(sr.keys())  # [b'a2']
    except Exception as e:
        print(e)
