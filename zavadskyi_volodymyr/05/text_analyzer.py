from my_module import reading, writing

try:
    text = reading('text.txt')
except FileNotFoundError as error:
    print(error)
except OSError as error:
    print(error)


def convert(string):
    """
    This is a function to convert string into the list
    :param string: string is the text to convert
    :type string: str
    :return: converted_list
    :rtype: list
    """
    low = string.lower()
    converted_list = list(low.split(" "))
    return converted_list


def punctuation(puncList):
    """
    This is a function to delete punctuation from the list
    :param puncList: puncList is the list, you want to see without punctuation
    :type puncList: list
    :return: new_list
    :rtype: list
    """
    punctuation_list = ['.',',',':',';','!','?','(',')'] 

    new_list = []
    for word in puncList:
        if word[-1] in punctuation_list:
            new_list.append(word[:-1])
        elif word[0] in punctuation_list:
            new_list.append(word[1:])
        else:
            new_list.append(word)

    return new_list


def stopwords(string):
    """
    This is a function to delete specific words from the list
    :param string: string is the text, you want to see without specific words
    :type string: str
    :return: new_string
    :rtype: str
    """
    stopwords_list = ['a', 'an', 'to', 'is', 'are', 'was', 'were', 'will', 'would', 'could', 'and', 'or', 'if', 'he', 'she', 'it', 'this', 'my', 'etc']

    stringwords = string.split()
    
    resultwords  = [word for word in stringwords if word.lower() not in stopwords_list]
    new_string = ' '.join(resultwords)
    
    return new_string


def quantity(wordList):
    """
    This is a function to count words from text
    :param wordList: wordList is the list of words, where you want to count quantity
    :type wordList: list
    :return: quantity_list
    :rtype: list
    """
    quantity_list = len(wordList)

    return quantity_list


def dictionary(wordList):
    """
    This is a function to count words from text
    :param wordList: wordList is the list of words, where you want to count quantity
    :type wordList: list
    :return: quantity_list
    :rtype: list
    """
    dictionary_list = list(dict.fromkeys(wordList))

    return dictionary_list


def keywords(dictionary):
    """
    This is a function to find keywords from text
    :param dictionary: dictionary, where you want to find all the keywords
    :type dictionary: dict
    :return: new_dict
    :rtype: dict
    """
    new_dict = {}
    a = 0
    for key, value in sorted(dictionary.items(), key=lambda item: item[1], reverse = True):
        new_dict[key] = value
        a +=1
        if a >= 3:
            break
        
    return new_dict


def frequency(wordList):
    """
    This is a function to count frequency
    :param wordList: wordList is the list, which you want to count percentege of words
    :type wordList: list
    :return: new_dict
    :rtype: dict
    """
    wordfreq = []
    
    for i in wordList:
        wordfreq.append(wordList.count(i) / len(wordList) * 100)

    new_dict = {}

    for j in range(len(wordList)):
        new_dict[wordList[j]] = str(round(wordfreq[j], 3)) + '%'

    return new_dict

if __name__ == '__main__':
    
    try:
        no_stopwords = stopwords(text)
    except NameError as error:
        print(error)
    except AttributeError as error:
        print(error)
        
    try:
        list_with_punc = convert(no_stopwords)
    except NameError as error:
        print(error)
    except AttributeError as error:
        print(error)
        
    try:
        full_list = punctuation(list_with_punc)
    except NameError as error:
        print(error)
    except AttributeError as error:
        print(error)

    try:
        my_dict = {i:full_list.count(i) for i in full_list}
    except NameError as error:
        print(error)
    except TypeError as error:
        print(error)

    try:
        print(f"Words quantity: {quantity(full_list)}\n"
            f"Text dictionary:  {', '.join(dictionary(full_list))}\n"
            f"Keywords: {', '.join(' - '.join((str(k),str(v))) for k,v in keywords(my_dict).items())}\n"
            f"Frequency: {', '.join(' - '.join((str(k),str(v))) for k,v in frequency(full_list).items())}")
    except NameError as error:
        print(error)
    except TypeError as error:
        print(error)

    try:
        writing(f"Words quantity: {quantity(full_list)}\n"
                f"Text dictionary:  {', '.join(dictionary(full_list))}\n"
                f"Keywords: {', '.join(' - '.join((str(k),str(v))) for k,v in keywords(my_dict).items())}\n"
                f"Frequency: {', '.join(' - '.join((str(k),str(v))) for k,v in frequency(full_list).items())}", 'new_file.txt')
    except NameError as error:
        print(error)
    except TypeError as error:
        print(error)
