def prettify_text(text_to_pretty, list_2_subtract, ptrn=''):
    """
    This is a function witch clean string from signs of punctuation
    :param text_to_pretty: input string
    :param list_2_subtract: list or tuple sign punctuation witch will substring
    :param ptrn: pattern
    :type text_to_pretty: str
    :type list_2_subtract: list or tuple
    :type ptrn: str
    :return: string
    :rtype: str
    """
    for simbol in list_2_subtract:
        text_to_pretty = text_to_pretty.replace(simbol, ptrn).lower()

    return text_to_pretty


def prettify_text2(input_str):
    '''
    :param input_str: input text
    :return: list of words
    '''
    list_sign_punctuation = [',', '...', ';', ':', '- ', '(', ')', '"']
    result = prettify_text(input_str, list_sign_punctuation)

    list_sign_punctuation2 = ('.', '?', '!')
    result = prettify_text(result, list_sign_punctuation2, ' ')

    list_pretext = [' a ', ' an ', ' to ', ' is ', ' are ', ' was ', ' were ', ' will ', ' would ', ' could ', ' and ',
                    ' or ', ' if ', ' he ', ' she ', ' it ', ' this ', ' my ', ' the ', ' on ', ' of ', ' in ', ' no ',
                    ' with ', ' but ', ' that ', ' than ',  'the ', 'on ', 'of ', 'with ', 'but ', 'that ', 'than ']
    result = prettify_text(result, list_pretext, ' ')

    clean_text_list = result.split(" ")
    white_space = ''
    while white_space in clean_text_list:
        clean_text_list.remove(white_space)

    white_space = '\n'
    while white_space in clean_text_list:
        clean_text_list.remove(white_space)

    return clean_text_list


def create_list_uniq_words(list_a):
    """
    This is a function witch create text list with unique words from list_a.
    :param list_a: list words
    :type list_a: list or tuple
    :return: list_c
    :rtype: list
    """
    list_c = []
    for element in list_a:
        if element not in list_c:
            list_c.append(element)

    return list_c


def count_keywords(list_a, list_b):
    """
    This is a function witch count keywords in list and return dictionary with count value .
    :param list_a: list words
    :param list_b: dictionary of key words
    :type list_a: list or tuple
    :type list_b: list or tuple
    :return: dictionary
    :rtype: dict
    """
    dict_out = {}
    for val in list_b:
        dict_out[val] = list_a.count(val)

    return dict_out


def show_top_keywords(dict_in, top=3):
    """
    This is a function witch take dictionary and return only top value.
    :param dict_in: dictionary list words as a key and frequency as value
    :param top: top value
    :type dict_in: dict
    :type top: int
    :return: dictionary
    :rtype: dict
    """
    dict_1 = {}
    dict_out = {}

    for k in sorted(dict_in, key=dict_in.get, reverse=True):
        dict_1[k] = dict_in[k]

    for key, value in dict_1.items():
        if top == 0:
            break
        dict_out[key] = value
        top -= 1

    return dict_out


def format_result(input_str):
    """
    This is a function witch take input string and return result of text analyze
    in special format.
    :param input_str: input string
    :type input_str: str
    :return: output text
    :rtype: str
    """

    clean_text_list = prettify_text2(input_str)

    words_quantity = len(clean_text_list)
    print(f'- words quantity: {words_quantity}')

    uniq_words = create_list_uniq_words(clean_text_list)
    string = ', '.join(uniq_words)
    print(f'- text dictionary: {string}')

    count_words = count_keywords(clean_text_list, uniq_words)

    top_words = show_top_keywords(count_words, 3)

    new_list = [key + ' - ' + str(value) for key, value in top_words.items()]
    string4 = ', '.join(new_list)
    print(f'- keywords: {string4}')

    new_list2 = [key + ' - ' + str(int(int(value) / int(words_quantity) * 100)) + '%'
                 for key, value in count_words.items()]
    string3 = ', '.join(new_list2)
    print(f'- frequency: {string3}')

    return


if __name__ == '__main__':

    my_string = 'The owners of the Zaandam, Holland America, said that more than 130 people on board had reported ' \
                'suffering "flu-like symptoms" and respiratory issues.' \
                'Nobody has left the ship since it docked in Chile two weeks ago.' \
                'Holland America said it planned to transfer passengers to a sister ship.' \
                'The Zaandam and the Rotterdam are both off the western, Pacific coast of Panama.' \
                'The Zaandam is trying to sail to Florida. But the Panamanian authorities have said no vessel with ' \
                'confirmed coronavirus cases on board can pass through the Panama Canal.'
    format_result(my_string)
