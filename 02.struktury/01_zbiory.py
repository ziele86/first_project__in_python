# -*- coding: utf-8 -*-

empty_set = set()
print(empty_set)
print(type(empty_set))

# %%
techs = {'python', 'java', 'c++', 'sql'}
print(techs)
print(type(techs))
print(len(techs))
# %%

set('python')
set('aaaaaale')

# %%
'python' in techs
'go' in techs

# %%
print(dir(set))

# %%
techs.add('sas')

# %%%
print(techs)

# %%
techs.remove('sas')

print(techs)

# %%
techs.pop()

# %%
techs.clear()

# %%
A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 6, 7, 8, 9,}
C = {5, 6}

C.issubset(A)
C.issubset({5, 6})
A.issuperset(C)
C.union(B)
A.intersection(B)
A.symmetric_difference(B)

D = B.copy()
print(D)
