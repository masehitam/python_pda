from collections import defaultdict

a = {}
print(a)
a = {'a':1, 'b':2, 'c':3}
print(a.items())
if 2 in a.values():
    print('a is in a')
else:
    print('a is not in a')
print(a.keys())
print(a.values())
for i in a.items():
    print(i)

for i in a.keys():
    print(i)

for i in a.values():
    print(i)

c = {}
b = defaultdict(int)
print(b['a'])
b['a'] += 1
print(b['a'])