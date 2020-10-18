import sys
import timeit
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from cryptocli.helpers.load_file import load_file
from cryptocli.helpers.validation import *


class HybridCryptomator:
    CHUNK_SIZE = 64 * 1024

    def __init__(self):
        pass

    def generate_key_pair(self, path, private_key_filename="key.priv", public_key_filename="key.pub"):
        # TODO validation

        path = path + '/' if path[-1] != '/' else path

        key = RSA.generate(2048)

        with open(path + private_key_filename, 'wb') as private_key:
            private_key.write(key.export_key('PEM'))

        with open(path + public_key_filename, 'wb') as public_key:
            public_key.write(key.publickey().export_key('PEM'))

        print(f'Private and public key successfully generated in {path}')

    def encrypt_symmetric_key(self, symmetric_key, public_key):
        cipher_rsa = PKCS1_OAEP.new(RSA.import_key(public_key))
        symmetric_key_enc = cipher_rsa.encrypt(symmetric_key)

        return symmetric_key_enc


    def decrypt_symmetric_key(self, symmetric_key_enc, private_key):
        cipher_rsa = PKCS1_OAEP.new(RSA.import_key(private_key))
        symmetric_key = cipher_rsa.decrypt(symmetric_key_enc)

        return symmetric_key


    def get_tag_from_file(self, infile):
        infile.seek(-16, os.SEEK_END)
        tag = infile.read()
        infile.seek(-16, os.SEEK_END)
        infile.truncate()

        return tag

    # output file format: [ nonce (12) | enc_symmetric_key (256) | encrypted_data (len(data)) | tag (16) ]
    def encrypt_file(self, in_filename, out_filename, public_key_filename):
        # TODO validation

        public_key = load_file(public_key_filename)

        nonce = get_random_bytes(12)
        symmetric_key = get_random_bytes(16)
        symmetric_key_enc = self.encrypt_symmetric_key(symmetric_key, public_key)
        header = nonce + symmetric_key_enc

        cipher = AES.new(symmetric_key, AES.MODE_GCM, nonce=nonce)

        timer_start = timeit.default_timer()
        with open(in_filename, 'rb') as infile:
            with open(out_filename, 'wb') as outfile:

                cipher.update(header)
                outfile.write(header)

                while True:
                    chunk = infile.read(self.CHUNK_SIZE)
                    if len(chunk) == 0:
                        break
                    outfile.write(cipher.encrypt(chunk))

                # write TAG
                outfile.write(cipher.digest())

                time = round((timeit.default_timer() - timer_start), 4)

                print(f'File {in_filename} successfully encrypted (time: {str(time)}s)')

    # input file format: [ nonce (12) | enc_symmetric_key (256) | encrypted_data (len(data)) | tag (16) ]
    def decrypt_file(self, in_filename, out_filename, private_key_filename):
        # TODO validation

        timer_start = timeit.default_timer()
        with open(in_filename, 'rb+') as infile:
            nonce = infile.read(12)
            symmetric_key_enc = infile.read(256)
            header = nonce + symmetric_key_enc

            private_key = load_file(private_key_filename)

            symmetric_key = self.decrypt_symmetric_key(symmetric_key_enc, private_key)

            cipher = AES.new(symmetric_key, AES.MODE_GCM, nonce=nonce)
            cipher.update(header)

            tag = self.get_tag_from_file(infile)
            infile.seek(12 + 256)

            with open(out_filename, 'wb') as outfile:
                while True:
                    chunk = infile.read(self.CHUNK_SIZE)
                    if len(chunk) == 0:
                        break
                    outfile.write(cipher.decrypt(chunk))

                infile.write(tag)

            try:
                cipher.verify(tag)
            except ValueError as e:
                print(e)

            time = round((timeit.default_timer() - timer_start), 4)

            print(f'File {in_filename} successfully decrypted (time: {str(time)}s)')
