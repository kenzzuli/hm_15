from copy import deepcopy

a = {'name': 'liulei', 'age': 18}

age_list = range(5)

for age in age_list:
    b = deepcopy(a)
    b['age'] = age
    print(b)

print("-" * 50)
print(a)
