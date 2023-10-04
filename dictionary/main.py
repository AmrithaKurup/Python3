menu = {'appam' : 10, 'dosa' : 20, 'puttu' : 30}
print(menu)
print('------------------------------------')
print(menu['appam'])
print('------------------------------------')
print(menu.items())
print('------------------------------------')
for t in menu.items():
    print(t)
print('------------------------------------')
for i,j in menu.items():
    print(i, ':', j)
print('------------------------------------')
for i in menu.keys():
    print(i)
print('------------------------------------')
for i in menu.values():
    print(i)