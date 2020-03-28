def split_string(string, ptrn=' '):

    splitted_string = []

    for _ in range(string.count(ptrn)):
        
        ptrn_start_index = string.find(ptrn)
        ptrn_end_index = ptrn_start_index + len(ptrn)

        splitted_string.append(string[:ptrn_start_index])

        string = string[ptrn_end_index:]

    splitted_string.append(string)

    return splitted_string



my_string = 'I live in Kyiv'
result = split_string(my_string, 'in')
print(result)
