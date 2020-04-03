# from urllib import HTTPError
from time import sleep


while True:
    
    try:
        rest = urllib.request.urlopen('http://example.com')
    except HTTPError as error:
        print('Website is temoprary unavailable. Retying in 10 seconds')
        sleep(10)
    else:
        break


    

