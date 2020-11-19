# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 17:28:12 2020

@author: hongbo
"""

import threading
import time
import _thread


exitFlag = 0

# exitFlag表示是否每个线程要进行工作后再退出，设定1则所有线程启动后直接退出


class myThread (threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        super().__init__()  #
        self.threadID = threadID
        self.name = name
        self.counter = counter


    def run(self):
        # 把要执行的代码写到run函数里面线程在创建后会直接运行run函数
        print("Starting " + self.name)
        self.print_time(self.name, 2, self.counter)
        print("Exiting " + self.name)


    def print_time(self, threadName, delay, counter):
        global exitFlag
        while counter:
            if exitFlag:
                _thread.exit()  # 这个是让线程主动退出
            time.sleep(delay)
            print("%s: %s" % (threadName, time.ctime(time.time())))
            exitFlag+=1
            counter -= 1


# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
print()
thread2 = myThread(2, "Thread-2", 2)
# 开启线程

thread2.start()
time.sleep(3)
thread1.start()

print("\nExiting Main Thread")