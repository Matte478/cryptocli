import sys
import timeit
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Random import get_random_bytes
from cryptocli.helpers.load_file import load_file
from cryptocli.helpers.validation import *


class SymmetricCryptomator:
    CHUNK_SIZE = 64 * 1024

    def __init__(self):
        pass

    def encrypt_file(self, in_filename, out_filename, key_filename):
        if not input_validation(in_filename) or not output_validation(out_filename):
            sys.exit()

        key = get_random_bytes(16)

        nonce = get_random_bytes(8)
        counter = Counter.new(64, nonce)

        cipher = AES.new(key, AES.MODE_CTR, counter=counter)

        with open(in_filename, 'rb') as infile:
            with open(out_filename, 'wb') as outfile:
                timer_start = timeit.default_timer()

                outfile.write(nonce)

                while True:
                    chunk = infile.read(self.CHUNK_SIZE)
                    if len(chunk) == 0:
                        break
                    outfile.write(cipher.encrypt(chunk))

                with open(key_filename, 'wb') as keyfile:
                    keyfile.write(key)

                    time = round((timeit.default_timer() - timer_start), 4)

                    print(f'File {in_filename} successfully encrypted (time: {str(time)}s)')

    def decrypt_file(self, in_filename, out_filename, key_filename):
        if not input_validation(in_filename) or not output_validation(out_filename) or not output_validation(key_filename, "Key"):
            sys.exit()

        key = load_file(key_filename)
        if not key_validation(key):
            sys.exit()

        with open(in_filename, 'rb') as infile:
            nonce = infile.read(8)
            counter = Counter.new(64, nonce)

            cipher = AES.new(key, AES.MODE_CTR, counter=counter)

            timer_start = timeit.default_timer()
            with open(out_filename, 'wb') as outfile:
                while True:
                    chunk = infile.read(self.CHUNK_SIZE)
                    if len(chunk) == 0:
                        break
                    outfile.write(cipher.decrypt(chunk))

                time = round((timeit.default_timer() - timer_start), 4)

                print(f'File {in_filename} successfully decrypted (time: {str(time)}s)')
