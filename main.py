import random

a = int(input('Number of bits = '))
i = 0
while i < 10:
    x = random.getrandbits(a)
    print(hex(x), ' ')
    i = i + 1
