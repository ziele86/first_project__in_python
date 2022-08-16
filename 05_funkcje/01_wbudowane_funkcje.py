# -*- coding: utf-8 -*-

modul = abs(-10) #wartosc bezwzględna
print(modul)
# %%
bool([])
bool({})
bool('')
bool(' ')
bool(112)
bool(0)
# %%
dir(list)
dir(tuple())
# %%
list(enumerate(['piotr', 'python', 'java']))
# %%
eval('1 + 2')

x = 10
eval('x + 23')

# %%
list(filter(abs, [-2, -1, 0, 1, 2]))

# %%
list(filter(bool, ['python', '', 'java']))

# %%
float(1)
float(1.3)
float('1')
float('1.5')
float('geds')
type(2.4)
type('fds')
# %%
help(float)
help(int)
# %%
isinstance(1, int)
isinstance(2.5, str)
isinstance('egfe', str)
isinstance('', str)
# %%
len('python')

list('Python')
list(range(10))

# %%
list(map(abs, [-2, -1, 0, 1, 2]))
# %%
names = ['piotr', 'paweł', 'adam']   
list(map(str.title, names))

# %%
max(range(15))
max([1, 2151, 3153])
max('Tomek')

min(range(241242))
min('piotr')
min('tomek')

pow(2, 5) #potęgowanie

list(reversed([5, 5235, 21]))
list(reversed('piotr'))

round(4.244141, 3) #zaokrąglanie

str(1)

sum([2, 35, 45])
lista1 = [1, 2, 3]
lista2 = [4, 5, 6, 7]
list(zip(lista1, lista2)) #dziala do momentu najkrótszej listy

list(zip('python', 'java'))
