import sys
from cryptocli.Cryptomator import Cryptomator
from cryptocli.HybridCryptomator import HybridCryptomator
from cryptocli.helpers.arg_parser import get_arg_parser

def main():
    parser = get_arg_parser()

    # Read arguments from the command line
    args = parser.parse_args()

    if not args.command:
        parser.parse_args(['--help'])
        sys.exit(0)

    elif args.command == 'symmetric-mode':
        cryptomator: Cryptomator = Cryptomator()

        if args.encrypt:
            cryptomator.encrypt_file(args.input, args.key, args.output)
        elif args.decrypt:
            cryptomator.decrypt_file(args.input, args.key, args.output)

    elif args.command == 'hybrid-mode':
        cryptomator: HybridCryptomator = HybridCryptomator()

        if args.encrypt:
            cryptomator.encrypt_file(args.input, args.output, args.key)
        elif args.decrypt:
            cryptomator.decrypt_file(args.input, args.output, args.key)

    if args.command == 'generate-key':
        print('generate key pair')
        print(args)


if __name__ == '__main__':
    main()
