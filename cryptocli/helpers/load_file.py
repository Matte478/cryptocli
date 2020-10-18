import os.path


def load_file(filename):
    if not os.path.isfile(filename):
        return None

    with open(filename, 'rb') as file:
        content = file.read()
        return content
