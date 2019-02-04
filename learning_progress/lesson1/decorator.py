#decorator

import time

print(time.time())

def timer(func):
    def wrapper():
        start_time = time.time()
        func()  #I_can_sleep 函数
        finish_time = time.time()
        print("用了%s" %(finish_time-start_time))
    return wrapper


@timer            #timer 修饰 I_can_sleep
def I_can_sleep():
    time.sleep(5)

#start_time = time.time()
I_can_sleep()  # 自动找 @timer
#finish_time = time.time()

#print("运行了 %s" %(finish_time-start_time))

def new_tips(argv):
    def tips(func):
        def wrapper(a,b):
            print("start")
            func(a,b)
            print("stop")
        return wrapper
    return tips

@new_tips("add_module")
def add(a,b):
    print(a+b)

print(add(4,5))

# advantage:
# 1. avoid duplicated function
# 2. able to repeatly use - simplicity

