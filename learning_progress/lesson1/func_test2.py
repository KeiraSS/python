#function closure

def counter(FIRST=0):
    cnt = [FIRST]
    def add_one():
        cnt[0] += 1
        return cnt[0]
    return add_one

num1 =counter(5)
print(num1())

# a*x+b = y

def a_line(a,b):
    def arg_y(x):
        return a*x+b
    return arg_y

def a_line(a,b):
    return lambda x: a*x+b



line = a_line(2,7)

print(line(10))

