def custom_join(collection, ptrn=' '):

    string = ''

    for word in collection:
        string += word + ptrn

    string = string[:len(string) - len(ptrn)]

    return string


collection = ['I', 'live', 'in', 'Kyiv']
result = custom_join(collection)
print(result)
