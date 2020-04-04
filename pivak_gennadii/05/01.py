import text_analyzer


def read_txt_file(file_name):
    """
    This function read text file and return string
    :param file_name: input txt file
    :type file_name: str
    :return: string
    :rtype: str
    """
    with open(file_name, 'r') as file:
            data = file.read()

    return data


def write_log_file(file_name, text_2_write):
    """
    This is a function witch write log to text file.
    :param file_name: txt file for output results
    :param text_2_write: results for output
    :type file_name: str
    :type text_2_write: str
    """
    with open(file_name, 'w') as file:
            file.write(text_2_write)

    return


if __name__ == '__main__':

    file_name = 'input_txt.txt'
    try:
        input_str = read_txt_file(file_name)
    except IOError:
        print(f'Error open file - {file_name}')
    else:
        clean_text_list = text_analyzer.prettify_text2(input_str)

        words_quantity = len(clean_text_list)
        string1 = '- words quantity: ' + str(words_quantity)

        uniq_words = text_analyzer.create_list_uniq_words(clean_text_list)
        string = ', '.join(uniq_words)
        string2 = '- text dictionary: ' + string

        count_words = text_analyzer.count_keywords(clean_text_list, uniq_words)

        top_words = text_analyzer.show_top_keywords(count_words, 5)

        new_list = [key + ' - ' + str(value) for key, value in top_words.items()]
        string4 = ', '.join(new_list)
        string3 = '- keywords: ' + string4

        try:
            new_list2 = [key + ' - ' + str(round(int(value) / int(words_quantity) * 100, 1)) + '%'
                         for key, value in count_words.items()]
        except ZeroDivisionError as error:
            print('Zero Division. Word quantity = 0')
        else:
            string5 = ', '.join(new_list2)
            string6 = '- frequency: ' + string5

            write_log_file('results.txt', string1 + '\n' + string2 + '\n' + string3 + '\n' + string6)
