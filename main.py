import random

a = int(input('Number of bits = '))
list_of = []
for i in range(2 ** a):
    x = random.getrandbits(a)
    list_of.append(hex(x))

print(list_of)

key = list_of[10]
i = 0
while i != key:
    it = random.getrandbits(a)
    i = hex(it)
print("Your key is " + key)
