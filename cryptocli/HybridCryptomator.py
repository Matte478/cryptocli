import sys
import timeit
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from cryptocli.helpers.load_file import load_file
from cryptocli.helpers.validation import *


class HybridCryptomator:
    def __init__(self):
        pass

    def generate_key_pair(self, filename_private_key, filename_public_key):
        # TODO validation

        key = RSA.generate(2048)

        with open(filename_private_key, 'wb') as private_key:
            private_key.write(key.export_key('PEM'))

        with open(filename_public_key, 'wb') as public_key:
            public_key.write(key.publickey().export_key('PEM'))

        print('Private and public key successfully generated')

    # output file format: [ nonce (12) | enc_symmetric_key (256) | encrypted_data (len(data)) | tag (16) ]
    def encrypt_file(self, filename_public_key, in_filename, out_filename):
        # TODO validation

        symmetric_key = get_random_bytes(16)
        nonce = get_random_bytes(12)

        with open(filename_public_key, 'rb') as pk:
            # Encrypt the session key with the public RSA key
            cipher_rsa = PKCS1_OAEP.new(RSA.import_key(pk.read()))
            enc_symmetric_key = cipher_rsa.encrypt(symmetric_key)

        cipher = AES.new(symmetric_key, AES.MODE_GCM, nonce=nonce)

        with open(in_filename, 'rb') as infile:
            with open(out_filename, 'wb') as outfile:
                chunksize = 64 * 1024
                # timer_start = timeit.default_timer()

                header = nonce + enc_symmetric_key
                cipher.update(header)
                outfile.write(header)

                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    outfile.write(cipher.encrypt(chunk))

                # write TAG
                outfile.write(cipher.digest())

                # time = round((timeit.default_timer() - timer_start), 4)
                time = -1
                print('File ' + in_filename + ' successfully encrypted (time: ' + str(time) + 's)')

    # input file format: [ nonce (12) | enc_symmetric_key (256) | encrypted_data (len(data)) | tag (16) ]
    def decrypt_file(self, filename_private_key, in_filename, out_filename):
        # TODO validation

        with open(in_filename, 'rb+') as infile:
            nonce = infile.read(12)
            enc_symmetric_key = infile.read(256)
            header = nonce + enc_symmetric_key

            with open(filename_private_key, 'rb') as pk:
                cipher_rsa = PKCS1_OAEP.new(RSA.import_key(pk.read()))

            symmetric_key = cipher_rsa.decrypt(enc_symmetric_key)

            cipher = AES.new(symmetric_key, AES.MODE_GCM, nonce=nonce)
            cipher.update(header)

            infile.seek(-16, os.SEEK_END)
            tag = infile.read()
            infile.seek(-16, os.SEEK_END)
            infile.truncate()
            infile.seek(12 + 256)

            chunksize = 64 * 1024
            # timer_start = timeit.default_timer()
            with open(out_filename, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    outfile.write(cipher.decrypt(chunk))

            try:
                print(len(tag))
                cipher.verify(tag)
            except ValueError as e:
                print(e)

            # time = round((timeit.default_timer() - timer_start), 4)
            time = -1
            print('File ' + in_filename + ' successfully decrypted (time: ' + str(time) + 's)')
