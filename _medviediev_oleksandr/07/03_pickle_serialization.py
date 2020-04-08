import pickle


my_dict = {'A': 1, 'B': 2}
my_dict_1 = {'C': 3, 'D': 4}
obj_to_serialize = {'my_dict': my_dict, 'my_dict_1': my_dict_1}

# Stream serialization
my_dict_serialized = pickle.dumps(my_dict)
print(my_dict_serialized)

my_dict_deserialized = pickle.loads(my_dict_serialized)
print(my_dict_deserialized)

# File serialization
with open('file.bin', 'wb') as file:
    pickle.dump(obj_to_serialize, file)

with open('file.bin', 'rb') as file:
    my_dict_deserialized = pickle.load(file)

print(my_dict_deserialized['my_dict'])
print(my_dict_deserialized['my_dict_1'])

# File func serialization
def func():
    return 1


def func_1():
    return 2


obj_to_serialize = [func, func_1]


with open('file_func.bin', 'wb') as file:
    pickle.dump(obj_to_serialize, file)

with open('file_func.bin', 'rb') as file:
    my_dict_deserialized = pickle.load(file)


func = my_dict_deserialized[0]
func_1 = my_dict_deserialized[1]

print(func())
print(func_1())
