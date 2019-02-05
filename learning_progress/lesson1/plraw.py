# from urllib import request
# from urllib import parse
# 请求网站内容
import socket
import urllib
from urllib import request


url = 'http://www.baidu.com'

# 显示内容
response = request.urlopen(url,timeout=1)
#
print(response.read().decode('utf-8'))

# GET 往服务器传递数据  httpbin.org

# POST 传递用户密码  数据不会出现在网址栏

# data = bytes(parse.urlencode({'hello':'word'}),encoding='utf8')

# response2 = request.urlopen('http://www.httpbin.org/post',data = data)
# print(response2.read().decode('utf-8'))

try:
    response3 = urllib.request.urlopen('http://www.httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout): # 如果e.reason 是 socket.timeout return true
        print('time out!!!')
#print(response3.read().decode('utf-8'))