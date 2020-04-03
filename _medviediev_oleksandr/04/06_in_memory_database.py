in_memory_database = {}

while True:

    name = input('Name: ')

    if not name.isalpha():
        print('Name should consist of alphas only!')
        continue

    age = input('Age: ')

    if not age.isdigit() or not 0 <= int(age) <= 150:
        print('Age should be an integer in range from 0 to 150!')
        continue

    in_memory_database[name.capitalize()] = int(age)

    print(in_memory_database)
