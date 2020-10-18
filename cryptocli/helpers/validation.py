import os.path


def input_validation(filename, type='Input'):
    valid = True
    if not os.path.exists(filename):
        valid = False
        print(f'{type} file does not exists')
    elif os.path.isdir(filename):
        valid = False
        print(f'{type} can not be directory')

    return valid


def output_validation(filename, type='Output'):
    valid = True
    if os.path.isdir(filename):
        valid = False
        print(f'{type} can not be directory')

    return valid


def dir_validation(path):
    valid = os.path.isdir(path)

    if not valid:
        print(f'{path} must be directory')

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
