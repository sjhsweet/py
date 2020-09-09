import random
list_1 = []
for x in range(10):
    list_1.append(str(x))
for x in range(97,123):
    list_1.append(chr(x))
for x in range(65,91):
    list_1.append(chr(x))
code = random.sample(list_1,4)
print(''.join(code))