from rediscluster import *

if __name__ == '__main__':
    try:
        # 构建所有的节点（只需写主节点），Redis会使⽤CRC16算法，将键和值写到某个节点上
        startup_nodes = [
            {'host': '10.1.76.27', 'port': '7000'},
            {'host': '10.1.76.28', 'port': '7003'},
            {'host': '10.1.76.27', 'port': '7001'},
        ]
        # 构建RedisCluster对象
        rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
        # 设置键为name、值为ken的数据
        result = rc.set('name', 'ken')
        print(result)  # True
        # 获取键为name
        name = rc.get('name')
        print(name)  # ken
    except Exception as e:
        print(e)
