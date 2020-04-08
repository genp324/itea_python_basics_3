import json


my_dict = {'A': 1, 'B': 2}
json_obj = json.dumps(my_dict)

print(json_obj)

with open('json_serialization.txt', 'w') as file:
    json.dump(my_dict, file)

with open('json_serialization.txt', 'r') as file:
    my_dict = json.load(file)


print(type(my_dict))
