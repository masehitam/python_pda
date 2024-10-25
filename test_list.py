L1 = [2,1,3]
L2 = [4,5,6]
L3 = L1 + L2
L2.extend([0,6])
print(L3)
print(L1)
print(L2)
del(L2[1])
print(L2)
# del(L2[2])
print(L2.pop(2))
print(L2)
L2.remove(6)
print(L2)
L2.pop()
print(L2)
L2.pop(0)
print(L2)
# L2.pop(1)
# print(L2)
# L2.pop(2)


a = 1
b = a
print(a)
print(b)

warm = ['red', 'yellow', 'orange']
hot = warm
hot. append ('pink')
print(hot)
print (warm)