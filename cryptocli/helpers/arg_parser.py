import argparse


def get_arg_parser():
    # Define the program description
    description = 'A simple commandline app for encrypt / decrypt files in Python 3.'

    # Initiate the parser
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        '-v', '--version',
        help='Display this application version',
        action='version',
        version='%(prog)s (version 0.2.0)'
    )

    subparsers = parser.add_subparsers(dest='command')

    # Command: symmetric mode
    parser_symmetric_mode = subparsers.add_parser(
        'symmetric-mode',
        help='symmetric mode for encryption / decryption',
    )
    symmetric_action = parser_symmetric_mode.add_mutually_exclusive_group(required=True)
    symmetric_action.add_argument(
        '-e', '--encrypt',
        action='store_true',
        help='Encrypt action',
    )
    symmetric_action.add_argument(
        '-d', '--decrypt',
        action='store_true',
        help='Decrypt action',
    )
    parser_symmetric_mode.add_argument(
        '-i', '--input',
        help='Input file',
        required=True,
    )
    parser_symmetric_mode.add_argument(
        '-o', '--output',
        help='Output file',
        required=True,
    )
    parser_symmetric_mode.add_argument(
        '-k', '--key',
        help='Symmetric key file',
        required=True,
    )

    # Command: hybrid mode
    parser_hybrid_mode = subparsers.add_parser(
        'hybrid-mode',
        help='hybrid mode for encryption / decryption',
    )
    hybrid_action = parser_hybrid_mode.add_mutually_exclusive_group(required=True)
    hybrid_action.add_argument(
        '-e', '--encrypt',
        action='store_true',
        help='Encrypt action',
    )
    hybrid_action.add_argument(
        '-d', '--decrypt',
        action='store_true',
        help='Decrypt action',
    )
    parser_hybrid_mode.add_argument(
        '-i', '--input',
        help='Input file',
        required=True,
    )
    parser_hybrid_mode.add_argument(
        '-o', '--output',
        help='Output file',
        required=True,
    )
    parser_hybrid_mode.add_argument(
        '-k', '--key',
        help='Public key file',
        required=True,
    )

    # Command: generate key
    parser_generate_key = subparsers.add_parser(
        'generate-key',
        help='generate key pair (public and private) for hybrid mode',
    )
    parser_generate_key.add_argument(
        '-p', '--path',
        help='Path where the key pair will be stored',
        required=True,
    )

    return parser
