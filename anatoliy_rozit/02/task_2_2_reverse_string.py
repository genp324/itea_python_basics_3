# Approach N_1

input_string = input('Enter some text for us to destor approach 1: ')

output_string = ''

index = len(input_string)

while index > 0:
    output_string += input_string[index - 1]
    index = index - 1

print(output_string)

# Approach N_2 (I am not quite sure it could be considered as a "different" approach)

input_string_2 = input('Enter some text for us to destor approach 2: ')

backward_list = []

index_2 = len(input_string_2)

while index_2 > 0:
    backward_list += input_string_2[index_2 - 1]
    index_2 = index_2 - 1

output_string_2 = ''

for i in range(len(backward_list)):
    output_string_2 += backward_list[i]

print(output_string)
