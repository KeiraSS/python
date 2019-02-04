import threading
from threading import current_thread

class MyThread(threading.Thread):
    def run(self):
        print(current_thread().getName(),'start')
        print('start')
        print(current_thread().getName(),'stop')

t1 = MyThread()
t1.start()
t1.join()

