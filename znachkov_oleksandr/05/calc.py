from modules.iofile import *


OUTPUT = "results.txt"
truncatetext(OUTPUT)

rawtext = gettext("text.txt")

EXCEPTION = ("a an to is are was were will would could and or if he she it this my offer").split()

def rempunctuation (text):
    retext = [] 
    for symbol in text:
        if symbol.isalpha() or symbol.isspace():
            retext.append (symbol)


    listtostr = "".join(map(str, retext))
    return listtostr.split()

def filldict (list_):
    wdict = {}
    for word in list_:
        if word in EXCEPTION:
            continue
        if word not in wdict.keys():
            wdict[word] = 0 
            wdict[word] = wdict.get(word) + 1
        else:
            wdict[word] = wdict.get(word) + 1
    return wdict

def findtop (dict_):
    rdict = {}
    sorted_ = sorted (list (dict_.values()), reverse = True)
    for index in range (3):
        for key, value in dict_.items():
            if value == sorted_[index]:
                rdict[key] = value
    return rdict

def freq (dict_):
    size = len (dict_.values())
    for key, value in dict_.items():
        try:
            dict_[key] = value * 100 / size 
        except ZeroDivisionError as error:
            print ("Zero devision is forbiden, check size variable")
            sys.exit()
    return dict_


list_of_words = rempunctuation(rawtext.lower()) 

output = f'- words quantity: {len(list_of_words)} \n'
writetext(OUTPUT, output)

mydict = filldict (list_of_words)
output = f'- text dictionary: '
writetext(OUTPUT, output)

wordlist = []
for word in mydict.keys():
    wordlist.append(word)

writetext (OUTPUT, " ".join(map(str, wordlist)))

output = f'- keywords: '
writetext(OUTPUT, output)

for key, value in (findtop (mydict)).items():
    output = f'{key} - {value} '
    writetext(OUTPUT, output)

output = "\n- frequency: " 
writetext(OUTPUT, output)

for key, value in (freq (mydict)).items():
    output = f'{key} - {round(value,2)} '
    writetext(OUTPUT, output)
