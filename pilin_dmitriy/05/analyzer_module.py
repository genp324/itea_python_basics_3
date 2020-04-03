def read_from_file(read_filename):
    """
    :param arg1: filename
    :type arg1: str
    :return: read text from file 
    :rtype: return str
    """    
    try:
        with open(read_filename, 'r') as read_txt_file:
            return read_txt_file.read()
        
    except FileNotFoundError:
        raise FileNotFoundError(' Error, No such file. ' + read_filename)
    
    except PermissionError:
        raise PermissionError(' Permission denied. Check file permissions for ' + read_filename)


def write_to_file(write_filename, start_text='', arg=''):
    """
    :param arg1: filename 
    :param arg2: string
    :param arg3: string
    :type arg1: str
    :type arg1: str
    :type arg1: str
    :return: write text to file 
    """  
    try:
        with open(write_filename, 'a') as write_txt_file:

            if start_text != '' :
                return write_txt_file.write(start_text + arg '\n')

            else:
                return write_txt_file.write('Nothing to write\n')
                        
    except TypeError as Error:
        raise TypeError(Error)
    
    except PermissionError:
        raise PermissionError(' Permission denied. Check file permissions for ' + write_filename)


def clear_file(write_filename):
    """
    :param arg1: filename 
    :type arg1: str
    :return: clear file 
    """ 
        try:
            with open(write_filename, 'w') as write_txt_file:
                print('File is cleared')

        except TypeError as Error:
            raise TypeError(Error)
        
        except PermissionError:
            raise PermissionError(' Permission denied. Check file permissions for ' + write_filename)
