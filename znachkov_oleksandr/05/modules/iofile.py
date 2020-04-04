import sys


def gettext (filepath):
    try:
        with open (filepath, 'r') as myfile:
            data = myfile.read()
    except FileNotFoundError:
        print (f'File {filepath} not Found!')
        sys.exit(1)

    return (data)

def writetext (filepath, output):
    with open (filepath, 'a') as myfile:
        myfile.write(output)

def truncatetext (filepath):
    myfile = open (filepath, 'w')
    myfile.close()

if __name__ == "__main__":
    print ("Dirrect run is not allowed")

