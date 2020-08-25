from Crypto.Cipher import AES
from base64 import b64decode

if __name__ == '__main__':
    # open file
    with open("data/data_7.txt") as f:
        lines = f.readlines()

    # decode base64
    cipher = b64decode(''.join(lines))

    # define key
    key = "YELLOW SUBMARINE"

    # initiate AES key with ECB mode
    decryption = AES.new(key, AES.MODE_ECB)

    # Decrypt cipher
    message = decryption.decrypt(cipher).decode('utf-8')
    print("Result : {} ".format(message))
