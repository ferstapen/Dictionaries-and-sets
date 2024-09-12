# task 2
my_dict = {'Егор': 1985,
           'Слава': 2001}
print(my_dict)
print(my_dict['Егор'])
my_dict['Сергей'] = 1998
print(my_dict)
my_dict.update({'Марина': 2015,
                'Юлия': 1986})
print(my_dict)
x = my_dict.pop('Марина')
print(x)
print(my_dict)

# task 3
my_set = {20, 20, True, 'a', 'b'}
print(my_set)
my_set.add(100)
my_set.add(200)
my_set.discard(True)
print(my_set)