# 多线程编程的实验
import threading
import _thread
import time


# 为线程定义的函数
def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(thread_name + " : " + time.ctime(time.time()))


def test():
    # 创建两个线程
    try:
        _thread.start_new_thread(print_time, ("Thread 1", 2, ))
        _thread.start_new_thread(print_time, ("Thread 2", 4, ))
    except:
        print('线程启动失败')

    while 1:
        pass


if __name__ == '__main__':
    test()
