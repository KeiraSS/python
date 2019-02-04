

#print(dict2)


def func():
    num1 = 1
    num2 = 2
    print(num1 + num2)

func()

def sum(a):
    def add(b):
        return a+b
    return add

num2 = sum(2)
print(num2(7))