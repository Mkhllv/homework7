# Exercise №1
persons = [{
    'name': 'Alex',
    'age': 25},
    {'name': 'Romaт',
     'age': 24},
    {'name': 'Vasya',
     'age': 21},
    {'name': 'Oleg',
     'age': 22
     }]

# a
age_min = persons[0]["age"]
names_min = [persons[0]["name"]]
for i in persons:
    if i["age"] < age_min:
        age_min = i["age"]
        names_min = [i["name"]]
    elif i["age"] == age_min:
        names_min.append(i["name"])
print(names_min, age_min)
# b
max_len = float('-inf')
for i in persons:
    if len(i['name']) > max_len:
        max_len = len(i['name'])
names_max_len = [p['name'] for p in persons if len(p['name']) == max_len]
print(names_max_len)
# v
sum = 0
for person in persons:
    sum += person.get('age')
print(sum / len(persons))

# Exercise №2

my_dict_1 = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1}  
my_dict_2 = {'f': 4, 'g': 1, 'h': 3, 'a': 5, 'e': 6}
# a
c = [{k: [my_dict_1.get(k), my_dict_2.get(k)] for k in my_dict_1 if k in my_dict_2}]
print(c)
# b
c = [{q: [my_dict_1.get(q), my_dict_2.get(q)] for q in my_dict_1 if q not in my_dict_2}]
print(c)
# v
my_dict_3 = dict(item for item in my_dict_1.items() if item[0] not in my_dict_2)
print(my_dict_3)
# g
my_dict_3 = {}
for item in my_dict_1.items():
    if item[0] in my_dict_2:
        my_dict_3[item[0]] = [item[1], my_dict_2[item[0]]]
    else:
        my_dict_3[item[0]] = item[1]
print(my_dict_3)
