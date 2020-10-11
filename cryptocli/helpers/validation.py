import os.path


def input_validation(filename):
    valid = True
    if not os.path.exists(filename):
        valid = False
        print('Input file does not exists')
    elif os.path.isdir(filename):
        valid = False
        print('Input can not be directory')

    return valid


def output_validation(filename, type="Output"):
    valid = True
    if os.path.isdir(filename):
        valid = False
        print(type + ' can not be directory')

    return valid


def key_validation(key=None):
    valid = True
    if not key:
        print('Key file does not exists')
        valid = False

    elif len(key) != 16:
        print('Invalid key length')
        valid = False

    return valid
