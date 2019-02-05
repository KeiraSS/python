# re module
# regular expression

import re
p = re.compile('c.*t$')
print(p.match('catrt'))

# . single character
# ^ match start of string
# $ match end of string
# * match [0-many] front character
# + match [1-many] front character
# ? match [0-1]
# {}
p = re.compile('cr{4,6}t')
print(p.match('crrrrrt'))

# \d 字符

# [0-9][0-9][0-9]... -> [0-9]+ ->\d
# \D 匹配非数字
# \s  -> [a-z]

2018-03-04
(2018)-(03)-(04).group()
(03|04)

# ^$
# .*? - <img  /img>

