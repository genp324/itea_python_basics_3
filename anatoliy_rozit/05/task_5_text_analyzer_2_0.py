from my_mod_for_import import my_extract_text, save_results


def pretify(raw_text):
    """
    Current function prepares text for further processing by:
    1. Removing punctuation symbolls
    2. Creating a list of words filtered by exclusion list
    :param raw_text: Any text to be processed
    :type raw_text: string
    :return: list of words
    :rtype: list
    """
    excluded = ['as', 'a', 'an', 'to', 'is', 'are', 'was', 'were', 'will', 'would', 'could', 'and', 'or', 'if', 'he',
                'she', 'it', 'this', 'my', 'i', 'there', 'some', 'but', '\'d', 'how', 'lets', 'with', 'we', 'of',
                'going', 'the', 'for', 'be', 'in', 'am']

    x = ''

    for i in raw_text:

        if i.isalpha() or i.isspace() or i == '\'':

            x += ''.join(i)

    pre_formatted_list = x.lower().split()

    formatted_list = []

    for i in pre_formatted_list:

        if i not in excluded:
            formatted_list.append(i)

    return formatted_list


def count_words(formatted_list):
    """
    Current function counts elements in provided list
    :param formatted_list: list of elements to be processed
    :type formatted_list: list
    :return: count of elements
    :rtype: int
    """
    return len(formatted_list)


def return_dictionary(formatted_list):
    """
    Current function creates a set of unique elements
    :param formatted_list: list of elements to be processed
    :type formatted_list: list
    :return: set of objects
    :rtype: set
    """
    dictionary_to_set = set(formatted_list)

    separator = ', '
    text_dictionary = separator.join(dictionary_to_set)

    return text_dictionary


def return_keywords(formatted_list):
    """
    Current function creates set of elements with count for each element
    :param formatted_list: list of elements to be processed
    :type formatted_list: list
    :return: element with its' count
    :rtype: string
    """
    dict_with_quantity = {}

    for i in formatted_list:
        dict_with_quantity[i] = formatted_list.count(i)

    list_of_tuples = list(dict_with_quantity.items())
    sorted_list_by_desc = sorted(list_of_tuples, key=lambda x: x[1], reverse=True)
    three_top_values = sorted_list_by_desc[0:3]
    each_top_value = lambda x: ' - '.join(map(str, x))
    print_values = ', '.join(each_top_value(x) for x in three_top_values)

    return print_values


def return_statistics(formatted_list, total_words):
    """
    Current function creates set of elements with percentage of each element
    :param formatted_list: list of elements to be processed
    :param total_words: total number of elements in the list
    :type formatted_list: list
    :type total_words: int
    :return: each element with its' percentage
    :rtype: string
    """

    statistics = {}

    for i in formatted_list:
        statistics[i] = (str(int(formatted_list.count(i) / total_words * 100)) + '%')

    my_list = list(statistics.items())

    each_value = lambda x: ' - '.join(map(str, x))

    print_statistics = ', '.join(each_value(x) for x in my_list)

    return print_statistics


if __name__ == '__main__':

    print('Here we loaded some text file'
          '\nand tried to count statistics.\n'
          'You can find details in \'results\' file')

    file_to_read = 'text.txt'

    file_name = 'results.txt'

    raw_text = my_extract_text(file_to_read)

    beautiful_text = pretify(raw_text)

    counted_words = count_words(beautiful_text)
    save_results(f'Wards Quantity: {counted_words}\n', file_name)

    returned_dictionary = return_dictionary(beautiful_text)
    save_results(f'Text Dictionary: {returned_dictionary}\n', file_name)

    returned_keywords = return_keywords(beautiful_text)
    save_results(f'Keywords: {returned_keywords}\n', file_name)

    returned_statistics = return_statistics(beautiful_text, counted_words)
    save_results(f'Frequency: {returned_statistics}\n', file_name)
