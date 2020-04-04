def my_extract_text(file_to_read):
    with open(file_to_read, 'r') as f:
        raw_text = f.read()

    return raw_text


def save_results(obj, file_name):

    with open(file_name, 'a') as w:
        w.write(str(obj))
