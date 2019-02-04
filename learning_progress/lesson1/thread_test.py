import threading
import time

def myThread(arg1,arg2):
    print('%s %s ' %(arg1,arg2))
    time.sleep(1)

for i in range(1,6,1):
    # t1 = myThread(i,i+1)
    t1 = threading.Thread(target=myThread, args=(i,i+1))
    t1.start()

# 线程




