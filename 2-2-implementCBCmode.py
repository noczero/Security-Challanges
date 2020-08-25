from base64 import b64decode

from helper.AES import ecb_encrypt, ecb_decrypt, cbc_encrypt, cbc_decrypt

key = b"YELLOW SUBMARINE"

test_block = bytes([0x40] * 16)
assert(test_block == ecb_decrypt(key, ecb_encrypt(key, test_block)))

with open("data/data_10.txt") as f:
    ciphertext = b64decode(''.join([line.strip() for line in f.readlines()]))

iv = bytes([0x00] * 16)
decrypted = cbc_decrypt(key, iv, ciphertext)

print("Ouput : {} - Status : {}".format(decrypted.decode('ascii'), ciphertext == cbc_encrypt(key, iv, decrypted)))
