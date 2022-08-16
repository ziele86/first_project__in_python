# -*- coding: utf-8 -*-

file = open('simple.txt', 'r')

for line in file:
    print(line, end = '') #usuwa znak nowej linii po każdej linii
file.close()

# %%
#to samo co wyżej ale lepiej
with open('simple.txt', 'r') as file:
    for line in file:
        print(line, end = '')

# %%
with open('simple.txt', 'r') as file:
    line = file.readline()
    print(line)
# %%
with open('simple.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end = '')
# %%
with open('simple.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end = '')
        line = file.readline()
# %%
#wczytuje cały plik
with open('simple.txt', 'r') as file:
    lines = file.read()
    print(lines)