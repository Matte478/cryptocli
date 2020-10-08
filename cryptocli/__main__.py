import argparse
from cryptocli.Cryptomator import Cryptomator

# Define the program description
description = 'A simple commandline app for encrypt / decrypt files in Python 3.'

# Initiate the parser
parser = argparse.ArgumentParser(description=description)

# Arguments
parser.add_argument('-v', '--version', help='Display this application version', action='version', version='%(prog)s (version 0.1.0)')

mode = parser.add_mutually_exclusive_group(required=True)
mode.add_argument('-e', '--encrypt', action='store_true', help='Encrypt mode')
mode.add_argument('-d', '--decrypt', action='store_true', help='Decrypt mode')

parser.add_argument('-i', '--input',  metavar='', required=True, help='Input file')
parser.add_argument('-o', '--output', metavar='', required=True, help='Output file',)
parser.add_argument('-k', '--key',    metavar='', required=True, help='Key file')

# Read arguments from the command line
args = parser.parse_args()

def main():
    cryptomator: Cryptomator = Cryptomator()

    if args.encrypt:
        cryptomator.encrypt_file(args.input, args.key, args.output)
    elif args.decrypt:
        print(args.key)
        cryptomator.decrypt_file(args.input, args.key ,args.output)

if __name__ == '__main__':
    main()
