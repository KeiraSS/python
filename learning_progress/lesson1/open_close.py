#ry:
    for line in fd:
        print(line)
finally:
    pd.close()


with open("README.md") as f:
    for line in f:
        print(line)

import os

import time as t

import mymod

mymod.print_me()


