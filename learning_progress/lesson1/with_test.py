# 初始化和结束会被调用
class Testwith():
    def __enter__(self):
        print('run')
    def __exit__(self, exc_type, exc_val, exc_tb): #exc_tb 没有异常为空
        #print('stop')
        if exc_tb is None:
            print('normal')
        else:
            print('error is %s' %exc_tb)


with Testwith():
    print('test is running.')
    raise NameError('testNamerror')
