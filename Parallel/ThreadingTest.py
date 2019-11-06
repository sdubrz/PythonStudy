import threading
import time


exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("线程开始: " + self.name)
        print_time(self.name, self.counter, 5)
        print("线程结束： " + self.name)


def print_time(thread_name, delay, counter):
    while counter:
        if exitFlag:
            thread_name.exit()
        time.sleep(delay)
        print(thread_name + " : " + time.ctime(time.time()))
        counter -= 1


def run_test():
    print("主线程开始")
    thread1 = myThread(1, "Thread 1", 2)
    thread2 = myThread(2, "Thread 2", 5)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("主线程退出")


if __name__ == '__main__':
    run_test()
