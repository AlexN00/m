my_dict={'Alex': 2000, 'Denis':1996, 'Max': 2001}
print(my_dict)
print(my_dict['Alex'])
print(my_dict.get('Anton'))
my_dict.update({'Lena':1997,
'Kriss': 2006})
print(my_dict)
a=my_dict.pop('Alex')
print(a)
print(my_dict)
my_set={1,2,'orange', 1,2}
my_set=set(my_set)
print(my_set)
print(my_set.add(5))
print(my_set.add('apple'))
print(my_set)
print(my_set.discard(1))
print(my_set)