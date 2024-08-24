def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(10)
print_params(10, 'Привет')
print_params(b=25)
print_params(c=[1, 2, 3])


print('----------------------------------') #просто визуально разделить, нет в задании
values_list = [42, 'Пример', False]
values_dict = {'a': 1, 'b': 'строка', 'c': True}


print_params(*values_list)
print_params(**values_dict)


print('----------------------------------') #просто визуально разделить, нет в задании
values_list_2 = [37.5, 'тест']


print_params(*values_list_2, 42)