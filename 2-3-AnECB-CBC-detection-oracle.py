import random

from helper.random import random_bytes
from helper.AES import ecb_encrypt, cbc_encrypt, get_blocks


def encryption_oracle(input_):
    key = random_bytes(16)
    iv = random_bytes(16)
    prefix = random_bytes(random.randint(5, 10))
    suffix = random_bytes(random.randint(5, 10))
    plaintext = prefix + input_ + suffix

    use_cbc = random.choice([True, False])

    encrypted = (cbc_encrypt(key, iv, plaintext) if use_cbc
                 else ecb_encrypt(key, plaintext))
    answer = "CBC" if use_cbc else "ECB"

    return (encrypted, answer)


def guess_blockmode(oracle):
    input_ = bytes([0x42] * 100)
    encrypted, answer = oracle(input_)
    blocks = get_blocks(encrypted)

    unique_blocks = len(set(blocks))

    guess = "ECB" if unique_blocks != len(blocks) else "CBC"

    print("\nEncrypted : {} \n- Guess Type : {} - Answer Type : {}".format(encrypted, guess, answer))
    assert(guess == answer)

if __name__ == '__main__':
    # loop over 100
    for i in range(100):
        guess_blockmode(encryption_oracle)
