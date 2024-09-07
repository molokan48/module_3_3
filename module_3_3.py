def print_params(a = 1 , b = 'строка', c = True):
    print(a,b,c)

print_params()
print_params(b=25)
print_params(c = [1,2,3])

print('**********************')

values_list = ['qweerty' , False , 3.14]
values_dict = {'a': True , 'b' : '123' , 'c' : 789}

print_params(*values_list)
print_params(**values_dict)

print('**********************')

values_list_2 = ['zxcvbn' , 48.16]
print_params(*values_list_2, 42)