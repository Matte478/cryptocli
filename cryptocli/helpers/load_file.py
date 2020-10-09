import os.path


def load_file(filename):
    if not os.path.isfile(filename):
        return None

    with open(filename, 'rb') as keyfile:
        key = keyfile.read()
        return key
