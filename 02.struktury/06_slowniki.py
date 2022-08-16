# -*- coding: utf-8 -*-
# %%
empty_dict = dict()
print(empty_dict)

d = {}
print(type(d))

# %%
pol_to_eng = {'jeden': 'one', 'dwa': 'two', 'trzy': 'three'}
name_to_digit = {'jeden:': 1, 'dwa': 2}

# %%
pol_to_eng['cztery'] = 'four'
name_to_digit['trzy'] = 3

# %%
pol_to_eng_copied = pol_to_eng.copy()

# %%
pol_to_eng.keys()
list(pol_to_eng.keys())

pol_to_eng.values()
list(pol_to_eng.values())

# %%
list(pol_to_eng.items())

# %%
pol_to_eng['jeden']
print(pol_to_eng['jeden'])
# %%
pol_to_eng.get('jeden', 'brak')
print(pol_to_eng.get('jeden', 'brak'))

# %%
pol_to_eng.pop('cztery')
pol_to_eng.popitem()
# %%
pol_to_eng.update({'jeden':1})
