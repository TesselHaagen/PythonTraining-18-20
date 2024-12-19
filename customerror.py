filename = 'a_file_that_does_not_exist.txt'

try: # Try to open a file
    with open(filename) as f:

        for line in f:
            print(line.strip())

except IOError: # If the file does not exist, print a message
    print('File "%s\" does not exist' % filename)