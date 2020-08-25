from helper.xor import *

if __name__ == '__main__':
    encoded_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

    # get bytes cipher from text
    cipher = bytes.fromhex(encoded_string)
    print('Cipher : {}'.format(cipher))

    # get key from cipher using xor
    key = break_xor_char_key(cipher)
    print('Key : {}'.format(key))

    # decode the message based on cipher and key
    message = xor_single_char_key(cipher, key).decode('ascii')
    print('Message : {}'.format(message))

