def open_text(file_name):
    """
    Open txt text
    :param file_name: text which you want to open
    :type text: str
    :return: str
    :rtype: str
    """

    try:
        with open(file_name, 'r') as file:
            text = file.read()

        return text

    except FileNotFoundError as error:
        print('Wrong name of  txt file')



print(open_text)


def write_text(file_name, result):
    """
    Write a new text file
    :param file_name: name of text file 
    :type text: str
    :return: str
    :rtype: str
    """

    try:
        with open(file_name, 'a') as file:
            file.write(result)

    except TypeError as error:
        print('only string can be used')



