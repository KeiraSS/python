# import time
#
# print(time.time())
#
# print(time.localtime())
# print(time.strftime('%Y-%m-%d %H:%M:%S'))

import datetime
print(datetime.datetime.now())
newtime = datetime.timedelta(minutes=20) # 时间偏移
print(datetime.datetime.now()+newtime)

one_day = datetime.datetime(2019,2,5)
new_date = datetime.timedelta(days=5)
print(one_day+new_date)