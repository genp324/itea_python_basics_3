some_text = 'Uefa will hold a crisis conference call with its 55 members on \
            April 1 to discuss Champions League dates, transfer window and \
            player contracts. European football – just like sport across the \
            globe – is currently on hold due to the coronavirus pandemic, \
            with Spain and Italy the countries feeling the affects hardest.\
            But the governing body for Europe are keen to try and get a plan \
            in place so they are ready once football is able to resume again.\
            A statement read: Uefa has invited the general secretaries of its\
            55 members associations to a video conference on Wednesday 1 April\
            at midday to share an update on the progress made by the two working\
            groups that were created two weeks ago and to discuss options \
            identified with regards to the potential rescheduling of matches.\
            The meeting will look at developments across all Uefa national team\
            and club competitions, as well as discussing progress at Fifa and \
            European level on matters such as player contracts and the transfer\
            system.' 

block_words = ['as', 'a', 'an', 'to', 'is', 'are', 'was', 'were', 'will',
              'would', 'could', 'and', 'or', 'if', 'he', 'she', 'it',
              'this', 'my', 'i', 'am', 'at', 'and', 'on', 'for']



def clear_text(text):
    """
    Deleting in text punction marks and making a list with words
    :param text: text which you analyze
    :type text: str
    :return: create a list whith words in text
    :rtype: list
    """

    text = text.replace('.', ' ')
    text = text.replace(',', ' ')
    text = text.replace('?', ' ')
    text = text.replace('-', ' ')
    text = text.lower()
    text = text.split()

    return text


def checking_block_list(text, block_words):
    """
    Deleting words which in block_list in text
    :param text: list of words
    :param block_words: words which will be deleted in text
    :type text: list
    :type block_wordst: list
    :return: a list 
    :rtype: list
    """
    
    for i in text:
        if i in block_words or i.isdigit():
            text.remove(i)

    return text


def adding_to_dict(text):
    """
    Make a dict 
    :param text: list that you want to convert in dict
    type text: list
    :return: create a dict
    :rtype: dict
    """

    text_dict = {}

    for i in text:
        key = i
        value = text.count(i)
        text_dict[key] = value
    return text_dict


def calculate_words(some_dict):
    """
    Calculate value in dict
    :param some_dict: dictionary in which you want to sum value
    :type some_dict: dict
    :return: count of value 
    :rtype: int
    """

    summ_value = 0

    for key, value in some_dict.items():
        summ_value += value

    return summ_value


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
        new_value = value*100/sum_value
        dict_in_percent[key] = new_value

    return dict_in_percent

  
clear_text = clear_text(some_text)
without_block_words = checking_block_list(clear_text, block_words)
dictionary = adding_to_dict(without_block_words)
count_words = calculate_words(dictionary)
transform_dict = transform_in_percent(dictionary, count_words)

list_dictionary = []

for i, element in enumerate(dictionary):
    list_dictionary.append(element)

ptrn = ', '
str_dic = ptrn.join(list_dictionary)

print(f'quantity of words: {count_words}')
print(f'\nText dictionary: {str_dic}\n')
   
check_list = []

for key, value in transform_dict.items():
    check_list.append(value)

check_list.sort(reverse = True)

value_list = []
key_list = []
for k, v in transform_dict.items():
    if v in check_list[:3]:
      v = int(v)
      print(f'Most popular: {k} has {v} %')





