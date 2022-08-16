# -*- coding: utf-8 -*-
empty_list = list()
print(empty_list)

techs3 = ['python', 'java', 'c++', 'sql;']
print(techs3)
techs3[0]
techs3[0] = 'python 3.7'

print(techs3)
# %%
numbers = [1, 2, 3, 4, 5]
print(numbers)

print(type(numbers))
# %%
mixed = [23, True, 'tekst']
print(type(mixed))

# %%
nested = [11, 12, 13, ['jeden', 'dwa', True]]

bucket = [mixed, nested]

len(bucket)

mixed + nested

mixed + nested + ['scale']

techs = ['python', 'java', 'c++', 'sql;']

techs += ['html']
print(techs)

# %%
