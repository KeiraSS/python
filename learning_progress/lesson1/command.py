# os.path
# import os
#
# print(os.path.abspath('.')) #绝对路径
# print(os.path.exists('/Users'))
# print(os.path.isfile('/tmp'))
# print(os.path.isdir('/tmp'))
# os.path.join('/tmp',)

import pathlib

from pathlib import Path

p = Path('.') # 需要封装
print(p.resolve())

print(p.is_dir())

# 新建目录/tmp

q = Path('/tmp/m')
Path.mkdir(q,parents=True)