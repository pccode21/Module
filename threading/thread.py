from threading import Lock, Thread  # 引用线程和线程中的锁
import time
from queue import Queue
# queue 模块实现了多生产者、多消费者队列。这特别适用于消息必须安全地在多线程间交换的线程编程
# Queue 类实现了所有所需的锁定语义。


def job1():
    global A, lock  # 定义全局变量
    lock.acquire()  # 加锁
    for i in range(10):  # 遍历
        A += 1
        print('job1:', A)
    lock.release()  # 释放锁


def job2():
    global A, lock  # 定义全局变量
    lock.acquire()  # 加锁
    for i in range(10):  # 遍历
        A += 10
        print('job2:', A)
    lock.release()  # 释放锁


def job3(li, q):
    for i in range(len(li)):
        li[i] = li[i]**2
    q.put(li)  # 将列表 li 放入Queue类列表


def multithreading():
    q = Queue()  # 把q定义为Queue()类型
    threads = []  # 创建线程空列表
    data = [[1, 2, 3], [3, 4, 5], [4, 4, 4], [5, 5, 5]]
    for i in range(4):  # 遍历4个线程
        time.sleep(0.1)
        t = Thread(target=job3, args=(data[i], q))  # 创建线程 t 目标是执行函数 job3 参数值是(data[i], q)
        # t = Thread(target=job3(data[i], q))  # 也可以写成这样
        t.start()  # 开始执行线程
        threads.append(t)  # 将4个线程追加到列表threads中
    for thread in threads:
        thread.join()  # 每个线程开始后都要执行join()
    results = []  # 创建一个运算结果空列表
    for _ in range(4):  # 遍历4次
        results.append(q.get())  # 从Queue类列表中取出列表并追加到结果列表中
    print(results)


if __name__ == '__main__':
    lock = Lock()  # 给全局变量赋值，锁函数
    A = 0  # 给全局变量赋值 0
    t1 = Thread(target=job1)  # 创建线程 t1 目标是执行函数 job1
    t2 = Thread(target=job2)  # 创建线程 t2 目标是执行函数 job2
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    multithreading()
