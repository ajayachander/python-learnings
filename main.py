from sys import path

path.append('..\\Modules')

from module import suml,prodl


sumlist = [i+1 for i in range(20)]
prodlist = [j for j in range(1,5)]

print(prodlist)
print(suml(sumlist))
print(prodl(prodlist))
