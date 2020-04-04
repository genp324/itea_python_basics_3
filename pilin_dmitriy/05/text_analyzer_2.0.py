import analyzer_module as analyzer


EXCLUDED_SYMBOLS = ('(',')',',', '-', '"', '.', '!', ':', '?', '\n')
EXCLUDED_WORDS = ('a', 'may', 'an', 'to', 'the', 'is', 'of', 'have', 'been', 'are', 'was', 'were', 'will', 'would', 'could', 'and', 'or', 'if', 'he', 'she', 'it', 'this', 'my', 'an', 'as', 'by', 'has', 'in', 'on')

READ_FILE = 'raw_text.txt'
WRITE_FILE = 'result_text.txt'


def pretify(text):
    """
    :param arg1: string
    :type arg1: str
    :return: return prettified list of words cleared with list of exluded_words 
    :rtype: return list
    """
    try:
        for i in EXCLUDED_SYMBOLS:

            text=text.replace(i,' ')

        texts = ''

        for i in text:

            if not i.isdigit() :
                texts += ''.join(i)

        texts=texts.lower().split()

        pretify_text = list(filter(lambda word: word not in EXCLUDED_WORDS, texts))

        return pretify_text

    except AttributeError:
        raise AttributeError('Only text string allowed.')


def count_words(txt):

    try:
        return str(len(txt))

    except TypeError as error:
        print(f'ERROR:{str(error)}')
    
    

def unique_words(text):
    """
    :param arg1: string
    :type arg1: str
    :return: return list of unique words occurring in the text
    :rtype: return dict
    """
    dict_with_quantity = {}
    
    try:
        for i in text:
            dict_with_quantity[i] = text.count(i)

    except TypeError as error:
        print(f'ERROR:{str(error)}')

    return dict_with_quantity


def frequent_words(dict_list):
    """
    :param arg1: dict
    :type arg1: dict
    :return: return list of words frequency in the text
    :rtype: return dict
    """
    try:
        freq_words = sorted(dict_list.items(), key=lambda x: x[1], reverse=True)

    except TypeError as error:
        print(f'ERROR:{str(error)}')

    return freq_words


def most_freq_words(freq_words,number_shown_words):
    most_freq ={}

    for key, value in freq_words[:number_shown_words]:
        most_freq[key] = value

    return most_freq



def frequency(dict_list):
    """
    :param arg1: dict
    :type arg1: dict
    :return: return list frequency of words in percents in the text
    :rtype: return dict
    """    
    percent_list = {}

    for key, value in dict_list.items():

        math = value * 100 / unique_num
        percent_list[key] = round(math, 3)

    return percent_list




if __name__ == "__main__":
 
    raw_text = analyzer.read_from_file(READ_FILE)

    try:
        analyzer.clear_file(WRITE_FILE)
    except TypeError as identifier:
        print(f'ERROR: {str(identifier)}')


    try:
        txt = pretify(raw_text)

    except TypeError as identifier:
        print(f'ERROR: {str(identifier)}')
    
    count = count_words(txt)

    try:
        analyzer.write_to_file(WRITE_FILE,'Words quantity:', count)

    except TypeError as identifier:
        print(f'ERROR: {str(identifier)}')

    unique_num = len(unique_words(txt))

    try:
        analyzer.write_to_file(WRITE_FILE,'Unique words quantity: ', str(unique_num))

    except TypeError as identifier:
        print(f'ERROR: {str(identifier)}')
    
    unique = unique_words(txt)
    sorted_dict = frequent_words(unique)

    number_shown_words = 5
    freq = most_freq_words(sorted_dict,number_shown_words)

    result = list()

    # it's for me  ^_^
    # for key ,value in freq.items():
    #     result.append(f'{key}: {value}')

    # joined_string=', '.join(result)
    #or

    joined_string = ', '.join([ f'{key}: {value}' for key, value in freq.items()])

    try:
        analyzer.write_to_file(WRITE_FILE,'Keywords: ', str(joined_string.title()))

    except TypeError as identifier:
        print(f'ERROR: {str(identifier)}')

    frequency_list = frequency(unique)

    joined_frequency = ', '.join([f'{key}: {value}' for key, value in frequency_list.items()])

    try:
        analyzer.write_to_file(WRITE_FILE,'Wirs on Percets: ', str(joined_frequency.title()))

    except TypeError as identifier:
        print(f'ERROR: {str(identifier)}')
  