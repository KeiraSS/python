# 相同属性的集合
# 可以进行封装，继承，覆盖，
# 不能直接引用，必须进过实例化

user1 = {'name' : 'tom', 'hp' : 100}
user2 = {'name' : 'Jerry', 'hp' : 80}

def print_name(rolename):
    print("name is %s , hp is %s" %(rolename['name'],rolename['hp']))

#print(print_name(user1))


# define class 类-抽象

class Player():  # 定义， 名字为大写
    def __init__(self,name,hp):
        self.name = name   # self为类实例化的本身
        self.hp = hp
    def print_role(self): #定义一个方法
        print("name is %s , hp is %s" %(self.name,self.hp))
    def updatename(self,newname): # 在类里面必须有self
        self.name = newname


class Monster():  #主类
    def __init__(self,hp):
        self.hp = hp
    def run(self):
        print('移动到一个位置')
    def whoami(self):
        print('我是怪物父亲')



class Animals(Monster):  # 如果想继承，需要把主类写进（）--- 子类
    '小妖怪'
    def __init__(self,hp):
        #self.hp = hp
        super().__init__(hp)



class Boss(Monster):
    '大妖怪'
    def whoami(self):
        print('我谁都不怕')

a1 = Monster(100)
print(a1.hp)
print(a1.run())
a2 = Animals(50)
print(a2.hp)
print(a2.run())
a3 = Boss(90)
print(a3.hp)
print(a3.whoami())

# 判断哪里个类
print("a1的类型%s" %type(a1))
print(isinstance(a2,Monster))

#   猫科动物 -》 猫

user1 = Player('tom',100) #类的实例化
user1.print_role()
user1.updatename('Lily')
user1.print_role()
user1.name = 'aaa'
user1.print_role()
