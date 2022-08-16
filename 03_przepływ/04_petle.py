# -*- coding: utf-8 -*-

for character in 'Python':
    print(character)
# %%
name = 'Sas'
for character in name:
    print(character)
# %%
name = 'Python'
index = 0
for character in name:
    print(index, character)
    index = index + 1
# %%
for index in range(10):
    print(index)
# %%
for index in range(len(name)):
    print(index, name[index])
# %%
for enu in enumerate(name):
    print(enu)

for indeks, character in enumerate(name):
    print('Nr indeksu: ', indeks, character)
    
# %%

for iii in [2, 4, 5, 6, 22]:
    print(iii)
# %%

for iii, value in enumerate([2, 4, 5, 6, 22]):
    print(iii, value)
# %%
for ii in range(100):
    print(ii)
# %%
for ii in range(10, 21):
    print(ii)
    
# %%
for iiii in range(10, 40, 5):
    print(iiii)
# %%
for iiii in range(10, 40, 5):
    print(iiii)
# %%
for iiiiii in range(10, 100, 10):
    print(iiiiii)
# %%
techs = 'java'
for i in range(len(techs)):
    print(i, techs[i])
# %%
string = 'Python Course'
for char in string[::-1]:
    print(char)
# %%
hashtags = '#sport#gym#fitness'
for char in hashtags:
    if char not in '#':
        print(char)
# %%
for char, number in zip('abcde', '12345'):
    print(char, number)
# %%
result = ''
for char in hashtags:
    print(char)