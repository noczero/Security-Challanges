from base64 import b64decode
from helper.xor import *

if __name__ == '__main__':
    with open("data/data_6.txt") as f:
        lines = f.readlines()

    # decode text using b64decode
    cipher = b64decode(''.join(lines))
    #print("Cipher : {} ".format(cipher))

    # get the key length
    key_length = guess_key_lengths(cipher)[0]
    print("Guessed Key Length : {}".format(key_length))

    # get the key
    key = break_xor_repeating_key(cipher, key_length)
    print("Key : {}". format(key.decode('ascii')))

    # decrypt the mesage
    decrypted = xor_repeating_key(cipher, key)
    message = decrypted.decode('ascii')

    print("Result : {}".format(message))


