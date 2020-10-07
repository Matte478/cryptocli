import sys


# from cryptography.fernet import Fernet

def main():
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))
    #
    # key = Fernet.generate_key()
    # f = Fernet(key)
    # token = f.encrypt(b"A really secret message. Not for prying eyes.")
    # print(token)

    print("Python version")
    print(sys.version)
    print(sys.version_info)
    # decrypt = f.decrypt(token)
    # print(decrypt)


if __name__ == '__main__':
    main()
