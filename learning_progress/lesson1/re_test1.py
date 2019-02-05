import re

# 分组
# p = re.compile('.{3}')
# print(p.match('bat'))

p = re.compile(r'(\d+)-(\d+)-(\d+)') # match 必须匹配相同的字符串
# print(p.match('aa2018-05-10').group(2)) #(空) 取出所有的部分进行输入
#
# # print(r'\nx\n') # -> 原样输出，不需要转译
#
# year, month, day = p.match('2018-05-10').groups()
# print(day)


print(p.search('aa2018-05-10').group()) # 匹配一直到能成功。 只要包含就行

# match 完全匹配进行分组
# search 搜索指定字符串

# sub('元字符','要替换的',字符串) # 字符串替换
phone = '222-444-53342 #这是电话号码' # 字符串
s = re.sub(r'#.*$','55555',phone)
print(s)
s1 = re.sub(r'\D','',s)
print(s1)

re.findall()