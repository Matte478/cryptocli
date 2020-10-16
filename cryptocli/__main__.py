import argparse
from cryptocli.Cryptomator import Cryptomator
from cryptocli.HybridCryptomator import HybridCryptomator

def main():
    # # Define the program description
    # description = 'A simple commandline app for encrypt / decrypt files in Python 3.'
    #
    # # Initiate the parser
    # parser = argparse.ArgumentParser(description=description)
    #
    # # Arguments
    # parser.add_argument('-v', '--version', help='Display this application version', action='version', version='%(prog)s (version 0.1.0)')
    #
    # mode = parser.add_mutually_exclusive_group(required=True)
    # mode.add_argument('-e', '--encrypt', action='store_true', help='Encrypt mode')
    # mode.add_argument('-d', '--decrypt', action='store_true', help='Decrypt mode')
    #
    # parser.add_argument('-i', '--input', metavar='', required=True, help='Input file')
    # parser.add_argument('-o', '--output', metavar='', required=True, help='Output file')
    # parser.add_argument('-k', '--key', metavar='', required=True, help='Key file')
    #
    # # Read arguments from the command line
    # args = parser.parse_args()
    #
    # cryptomator: Cryptomator = Cryptomator()
    #
    # if args.encrypt:
    #     cryptomator.encrypt_file(args.input, args.key, args.output)
    # elif args.decrypt:
    #     cryptomator.decrypt_file(args.input, args.key ,args.output)

    cryptomator: HybridCryptomator = HybridCryptomator()
    # cryptomator.generate_key_pair('private_key', 'public_key')
    # cryptomator.encrypt_file('public_key2', 'test.txt', 'test.txt.enc')
    cryptomator.decrypt_file('private_key2', 'test.txt.enc', 'test2.txt')

if __name__ == '__main__':
    main()
