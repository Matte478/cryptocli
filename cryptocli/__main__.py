import sys
from cryptocli.Cryptomator import Cryptomator


def main():
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    cryptomator: Cryptomator = Cryptomator()

    # cryptomator.encrypt_file('text.txt')
    # cryptomator.decrypt_file('text.txt.enc', 'text.txt.key', 'text3.txt')

if __name__ == '__main__':
    main()
