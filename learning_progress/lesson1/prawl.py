# import requests
# pip install requests
# # get
# url = 'http://www.httpbin.org/get'
# data = {'key':'value','abc':'xyz'}
#
# response = requests.get(url,data)
# print(response.text)

# post

import requests
url = 'http://www.httpbin.org/post'
data = {'key':'value','abc':'xyz'}

response = requests.post(url,data)
print(response.json())