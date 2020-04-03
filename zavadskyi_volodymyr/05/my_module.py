def reading(file):
    with open(file, 'r') as file:
        text = file.read()

    return text

def writing(result, file):
    with open(file, 'w') as file:
        file.write(result)
