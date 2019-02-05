import requests
import re

content = requests.get('http://baijiahao.baidu.com/s?id=1582686673550607795&wfr=spider&for=pc').text
print(content)

findall
