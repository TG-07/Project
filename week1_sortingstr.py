import numpy as np
import random
import string
length = 100
str = ['']
for x in range(length):
    str.append(string.ascii_letters)
print(sorted(str, key=len))
