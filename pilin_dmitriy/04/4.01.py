text = ('''The 2019-2020 coronavirus pandemic is an ongoing pandemic of coronavirus disease 2019 (COVID-19), caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). 
        The outbreak was first identified in Wuhan, Hubei, China, in December 2019, and was recognized as a pandemic by the World Health Organization (WHO) on 11 March. As of 28 March 2020,
        more than 614,000 cases of COVID-19 have been reported in over 200 countries and territories, resulting in approximately 28,200 deaths.More than 137,000 people have since recovered.
        The virus is mainly spread during close contact and via respiratory droplets discharged when people cough or sneeze. Respiratory droplets may be produced during breathing but the virus 
        is not considered airborne. People may also catch COVID-19 by touching a contaminated surface and then their face. It is most contagious when people are symptomatic, although 
        spread may be possible before symptoms appear. The time between exposure and symptom onset is typically around five days, but may range from 2 to 14 days.Common symptoms include fever, 
        cough, and shortness of breath. Complications may include pneumonia and acute respiratory distress syndrome. There is no known vaccine or specific antiviral treatment. Primary treatment 
        is symptomatic and supportive therapy. Recommended preventive measures include hand washing, covering one's mouth when coughing, maintaining distance from other people, and monitoring and 
        self-isolation for people who suspect they are infected. Efforts to prevent the virus spreading include travel restrictions, quarantines, curfews, workplace hazard controls, event postponements 
        and cancellations, and facility closures. These include the first (arguably successful) quarantine of Hubei, national or regional quarantines elsewhere in the world, curfew measures in China 
        and South Korea, various border closures or incoming passenger restrictions, screening at airports and train stations, and outgoing passenger travel bans.Schools and 
        universities have closed either on a nationwide or local basis in more than 124 countries, affecting more than 1.2 billion students.
        The pandemic has led to severe global socioeconomic disruption, the postponement or cancellation of sporting, religious, and cultural events, and widespread fears of supply shortages which have 
        spurred panic buying. Misinformation and conspiracy theories about the virus have spread online, and there have been incidents of xenophobia and racism against Chinese and other 
        East and Southeast Asian people. ''')


exluded_symbols = ('(',')',',', '-', '.', '!', ':', '?', '\n')
exluded_words = ('a', 'may', 'an', 'to', 'the', 'is', 'of', 'have', 'been', 'are', 'was', 'were', 'will', 'would', 'could', 'and', 'or', 'if', 'he', 'she', 'it', 'this', 'my', 'an', 'as', 'by', 'has', 'in', 'on')


def pretify(text):
    """
    :param arg1: string
    :type arg1: str
    :return: return prettified list of words cleared with list of exluded_words 
    :rtype: return list
    """

    for i in exluded_symbols:

        text=text.replace(i,' ')

    texts = ''
    for i in text:

        if not i.isdigit() :
            texts += ''.join(i)

    texts=texts.lower().split()

    pretify_text = list(filter(lambda word: word not in exluded_words, texts))

    return pretify_text


def count_words(text):
    return (len(text))
    

def unique_words(text):
    """
    :param arg1: string
    :type arg1: str
    :return: return list of unique words occurring in the text
    :rtype: return dict
    """
    dict_with_quantity={}

    for i in text:
        dict_with_quantity[i] = text.count(i)

    return dict_with_quantity


def  frequent_words(dict_list):
    """
    :param arg1: dict
    :type arg1: dict
    :return: return list of words frequency in the text
    :rtype: return dict
    """

    freq_words = sorted(dict_list.items(), key=lambda x: x[1], reverse=True)

    return freq_words


def frequency(dict_list):
    """
    :param arg1: dict
    :type arg1: dict
    :return: return list frequency of words in percents in the text
    :rtype: return dict
    """    
    percent_list={}

    for key, value in dict_list.items():

        math = value*100/unique
        percent_list[key] =math

    return percent_list



txt = pretify(text)
count = count_words(txt)
print(f'words quantity: {count}')

unique = len(unique_words(txt))

print(f'unique words quantity: {unique}')

sorted_dict = frequent_words(unique_words(txt))

print('keywords: ', end='')

for i in range(3):
    print(f'{sorted_dict[i][0]} - {sorted_dict[i][1]}, ', end='')

print('\n')

frequency_list = frequency(unique_words(txt))
print ('frequency: ', end='')

for key, value in frequency_list.items():
    print(f'{key} : %.1f'% value ,  end='% ')
