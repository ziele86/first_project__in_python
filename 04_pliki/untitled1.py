# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 10:05:45 2022

@author: ziele
"""

with open('simple.txt', 'r') as file:
    line = file.readline()
    print(line)

# %%
with open('simple.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# %%
with open('simple.txt', 'r') as file:
    lines = file.readlines()
    print(lines, end = '')

# %%
with open('simple.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end = '')
# %%
with open('simple.txt', 'r') as file:
    line = file.readline()
    while line: #jeźeli w pliku txt w pierwszej linii bedzie cokolwiek
        print(line, end = '')
        line = file.readline()
# %%
with open('simple.txt', 'r') as file:
    lines = file.read()
    print(lines)