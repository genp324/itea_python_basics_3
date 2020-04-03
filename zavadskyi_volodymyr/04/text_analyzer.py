some_text = "In the near future, everyone has access to a memory implant that records everything they do, see and hear. \
You need never forget a face again, but is that always a good thing? In a world where people's \
lives consist of riding exercise bikes to gain credits, Bing tries to help a woman get on to a singing competition show. \
This is my favourite text. Let's try to analyze it. I love this text. I love Python."

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

def stopwords(stopList):
    """
    This is a function to delete specific words from the list
    :param stopList: stopList is the list, you want to see without specific words
    :type stopList: list
    :return: new_list
    :rtype: list
    """
    stopwords_list = ['a', 'an', 'to', 'is', 'are', 'was', 'were', 'will', 'would', 'could', 'and', 'or', 'if', 'he', 'she', 'it', 'this', 'my', 'etc']
    for word in list(stopList):
        if word in stopwords_list:
            stopList.remove(word)
     
    newList = stopList
    
    return newList

def frequency(wordList):
    """
    This is a function to count frequency
    :param wordList: wordList is the list, which you want to count percentege of words
    :type wordList: list
    :return: wordfreq
    :rtype: list
    """
    wordfreq = []
    
    for i in wordList:
        wordfreq.append(wordList.count(i) / len(wordList) * 100)

    return wordfreq

list_of_words = convert(some_text)
no_punctuation = punctuation(list_of_words)
no_stopwords = stopwords(no_punctuation)

print('Words quantity: ', len(no_stopwords))
print('Text dictionary: ', ', '.join(list(dict.fromkeys(no_stopwords))))

my_dict = {i:no_stopwords.count(i) for i in no_stopwords}

print('Keywords:', end = ' ') 
j = 0
a = ',' #This was made for printing dot in the end of the keyword, cause I couldn`t find another way
for key, value in sorted(my_dict.items(), key=lambda item: item[1], reverse = True):
    print("%s - %s" % (key, value), end = f'{a} ')
    j += 1
    if j == 2:
        a = '.'
    if j >= 3:
        break
    
print('\nFrequency:', end = ' ')
freq = frequency(no_stopwords)
for i in range(len(no_stopwords)):
    print(f'{no_stopwords[i]} - {freq[i]}%', end = ', ')
    



