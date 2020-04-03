def serialize_list(obj, file_name):

    with open(file_name, 'w') as file:
        file.write(str(obj))


def deserialize_list(file_name):

    with open(file_name, 'r') as file:
        text = file.read()

    return text[1:-1].split(', ')


test_list = [1, 2, 3, 'asd', ['asd', 123]]
file_name = 'serialized_data.txt'

serialize_list(test_list, file_name)
new_test_list = deserialize_list(file_name)

print(type(new_test_list))
print(new_test_list)
