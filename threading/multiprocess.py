import multiprocessing as mp
import time


def job1(q):  # 多进程调用的函数不能有返回值，所以使用Queue存储多个线程运算的结果
    result = 0
    for i in range(1000):
        result += i + i**2 + i**3
    q.put(result)  # q 就像一个队列，用来保存每次函数运行的结果


def job2(x):
    return x*x  # 丢向Pool的函数有返回值


def job3(v, num, lock):
    lock.acquire()  # 锁住进程
    for _ in range(5):
        time.sleep(0.1)
        v.value += num  # 获取共享内存
        print(v.value)
    lock.release()  # 释放进程


def mulitcore():
    pool = mp.Pool()  # 定义一个Pool
    # 进程池 Pool 就是我们将所要运行的东西，放到池子里，Python会自行解决多进程的问题
    # 有了池子之后，就可以让池子对应某一个函数，我们向池子里丢数据，池子就会返回函数返回的值
    result = pool.map(job2, range(10))
    # 接下来用map()获取结果，在map()中需要放入函数和需要迭代运算的值，然后它会自动分配给CPU核，返回结果
    print(result)  # 输出结果是列表


def main():
    mulitcore()  # 调用函数
    lock = mp.Lock()  # 定义一个进程锁
    v = mp.Value('i', 0)  # 定义共享内存
    q = mp.Queue()  # 定义一个多进程队列，用来存储结果
    # Queue的功能是将每个核或线程的运算结果放在队列中，等到每个线程或核运行完毕后再从队列中取出结果， 继续加载运算
    p1 = mp.Process(target=job1, args=(q,))  # 定义第一个进程函数
    # args 的参数只要一个值的时候，参数后面需要加一个逗号，表示args是可迭代的，后面可能还有别的参数
    p2 = mp.Process(target=job1, args=(q,))  # 定义第二个进程函数，用来处理同一个任务
    p3 = mp.Process(target=job3, args=(v, 1, lock))  # 需要将lock传入
    p4 = mp.Process(target=job3, args=(v, 3, lock))
    # 分别启动、连接两个线程
    p1.start()  # 由于没有使用进程锁，所以进程p1和p2在p3和p4之后执行
    p2.start()
    p3.start()  # 由于使用进程锁，所以进程p3第一个执行
    p4.start()  # 由于使用进程锁，所以进程p4在p3完整运行后才执行
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    # 上面是分两批处理的，所以这里分两批输出，将结果分别保存
    result1 = q.get()
    result2 = q.get()
    print(result1, result2)


if __name__ == '__main__':
    main()

    """
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
1
2
3
4
5
8
11
14
17
20
249833583000 249833583000
    """
