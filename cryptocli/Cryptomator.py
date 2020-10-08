import os
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Random import get_random_bytes


class Cryptomator:
    def encrypt_file(self, in_filename, out_filename=None, key_file=None):
        if not out_filename:
            out_filename = in_filename + '.enc'
        if not key_file:
            key_file = in_filename + '.key'

        key = os.urandom(16)

        # iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))

        first_part = get_random_bytes(8)
        counter = Counter.new(64, first_part)

        encryptor = AES.new(key, AES.MODE_CTR, counter=counter)

        chunksize = 64 * 1024

        with open(in_filename, 'rb') as infile:
            with open(out_filename, 'wb') as outfile:

                outfile.write(first_part)

                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break

                    outfile.write(encryptor.encrypt(chunk))

                with open(key_file, 'wb') as keyfile:
                    keyfile.write(key)

                    print('Encrypted')

    def decrypt_file(self, in_filename, key_filename, out_filename=None):
        if not out_filename:
            out_filename = os.path.splitext(in_filename)[0]

        with open(in_filename, 'rb') as infile:
            # iv = infile.read(16)
            first_part = infile.read(8)
            counter = Counter.new(64, first_part)

            with open(key_filename, 'rb') as keyfile:
                key = keyfile.read()

                decryptor = AES.new(key, AES.MODE_CTR, counter=counter)

                chunksize = 64 * 1024

                with open(out_filename, 'wb') as outfile:
                    while True:
                        chunk = infile.read(chunksize)

                        if len(chunk) == 0:
                            break

                        outfile.write(decryptor.decrypt(chunk))

                    print('Decrypted')
