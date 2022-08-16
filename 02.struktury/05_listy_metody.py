# -*- coding: utf-8 -*-
# %%
techs = []
print(techs)

techs.append('c++')
print(techs)
# %%
techs.append('Python')
print(techs)

# %%
techs.append(['java', 'html'])
print(techs)
# %%

techs.extend(['sql', 'sass'])

print(techs)

# %%

techs.insert(3,'go')
print(techs)
techs.insert(2, 'erp')
print(techs)

# %%
print(techs)
techs.pop()
print(techs)
techs.pop(1)

print(techs.pop(2))

# %%
techs3 = ['python', 'java', 'c++', 'sql;']
techs3.index('java')
# %%
techs2 = ['python', 'java', 'c++', 'sql', 'angular']
techs2.count('sql')
techs2.sort()
techs2.sort(reverse=True)

# %%
techs4 = ['python', 'java', 'c++', 'sql;']
techs4.reverse()
techs4[1] = 'html'
