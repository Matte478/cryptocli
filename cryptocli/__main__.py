import sys
from cryptocli.SymmetricCryptomator import SymmetricCryptomator
from cryptocli.HybridCryptomator import HybridCryptomator
from cryptocli.helpers.arg_parser import get_arg_parser

def main():
    parser = get_arg_parser()
    args = parser.parse_args()

    if not args.command:
        parser.parse_args(['--help'])
        sys.exit(0)

    if args.command == 'symmetric-mode':
        cryptomator: SymmetricCryptomator = SymmetricCryptomator()
    else:
        cryptomator: HybridCryptomator = HybridCryptomator()

    if args.command == 'generate-key':
        cryptomator.generate_key_pair(args.path)
    elif args.encrypt:
        cryptomator.encrypt_file(args.input, args.output, args.key)
    elif args.decrypt:
        cryptomator.decrypt_file(args.input, args.output, args.key)


if __name__ == '__main__':
    main()
