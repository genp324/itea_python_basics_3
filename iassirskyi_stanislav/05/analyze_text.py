import with_open_module 

block_words = ['as', 'a', 'an', 'to', 'is', 'are', 'was', 'were', 'will',
              'would', 'could', 'and', 'or', 'if', 'he', 'she', 'it',
              'this', 'my', 'i', 'am', 'at', 'and', 'in', 'on', 'for',
               'by', 'the', 'of', 'with']



def clear_text(text):
    """
    Deleting in text punction marks and making a list with words
    :param text: text which you analyze
    :type text: str
    :return: deletting punctuation in text
    :rtype: str
    """

    punc_list = ['.', ',', '!', '?', ':', ';', '-', '"']

    for i in punc_list:
        text = text.replace(i, ' ')
    
    return text


def checking_block_list(text, block_words):
    """
    Deleting words which in block_list in text
    :param text: list of words
    :param block_words: words which will be deleted in text
    :type text: str
    :type block_wordst: list
    :return: a text without words in block_words 
    :rtype: str
    """
    
    text = text.lower().split()
    clear_list = []
    for i in text:
        if i not in block_words and i.isalpha():
            clear_list.append(i)
        clear_text = ' '.join(clear_list)

    return clear_text


def adding_to_dict(text):
    """
    Make a dict 
    :param text: Text that you want to convert in dict
    type text: str
    :return: create a dict
    :rtype: dict
    """

    text = text.split()
    text_dict = {}

    for i in text:
        key = i
        value = text.count(i)
        text_dict[key] = value
    return text_dict


def calculate_words(some_dict):
    """
    Calculate value in dict
    :param some_dict: dictionary in which you want to sum words
    :type some_dict: dict
    :return: count of words 
    :rtype: int
    """

    summ_words = []

    for key, value in some_dict.items():
        summ_words.append(key)

    len_words = len(summ_words)

    return len_words


def transform_in_percent(some_dict, sum_value):
    """
    Convert values to percent in dict
    :param some_dict: dictionary which you want to convert
    :param sum_value: count of value
    :type some_dict: dict
    :type sum_value: int
    :return: a dict 
    :rtype: dict

    """

    dict_in_percent = {}

    for key, value in some_dict.items():
        new_value = value* 100 / sum_value
        dict_in_percent[key] = new_value

    return dict_in_percent


def making_str_dict(some_dict):
    '''
    Composes a string dictionary of soame dict
    :param some_dict: dictionary which you want to convert
    :type some_dict: dict
    :return: a string 
    :rtype: str
    '''

    dict_list = []
    for i, element in enumerate(some_dict):
        dict_list.append(element)

    ptrn = ', '
    str_dict = ptrn.join(dict_list)

    return str_dict


if __name__ == '__main__':

    some_text = with_open_module.open_text('my_text.txt')
    
    clear_text = clear_text(some_text)
    without_block_words = checking_block_list(clear_text, block_words)
    dictionary = adding_to_dict(without_block_words)
    str_dict = making_str_dict(dictionary)
    count_words = calculate_words(dictionary)
    transform_dict = transform_in_percent(dictionary, count_words)

       
    value_list = []
    top_three = ''

    for key, value in transform_dict.items():
        value_list.append(value)

    value_list.sort(reverse = True)

    for k, v in transform_dict.items():
        if v in value_list[:3]:
          v = round(v, 3)
          top_three += f'\n{k} has {v} percent '             

    len_words = f'Count of words: {count_words} \nDictionary: {str_dict}'
    my_dictionary = f'\nDictionary: {str_dict}'
    
with_open_module.write_text('result_text.txt', len_words)
with_open_module.write_text('result_text.txt', my_dictionary)
with_open_module.write_text('result_text.txt', top_three)




