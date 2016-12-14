import copy

i = ['title', 'email', 'password2', 'password1', 'first_name','last_name', 'next', 'newsletter']
j = copy.deepcopy(i)
print i
print j
a, b = i.index('password2'), i.index('password1')
i[b], i[a] = i[a], i[b]

print i
print j
