def get_blocks(bytes_, blocksize=16):
    return [bytes_[i:i+blocksize] for i in range(0, len(bytes_), blocksize)]

if __name__ == '__main__':
    ciphertexts = []
    with open('data/data_8.txt') as f:
        for line in f.readlines():
            ciphertexts.append(bytes.fromhex(line.strip()))

    ciphertexts_blocks = []
    for ciphertext in ciphertexts:
        ciphertexts_blocks.append(get_blocks(ciphertext))

    uniques = []
    for block in ciphertexts_blocks:
        uniques.append(len(set(block)))

    least_unique_idx = uniques.index(min(uniques))

    ecb_encrypted = ciphertexts[least_unique_idx]

    print("ECB : {}".format(ecb_encrypted))
    print("{} unique blocks out of {}".format(uniques[least_unique_idx], len(ciphertexts[least_unique_idx])/16))

    assert(ecb_encrypted.startswith(b'\xd8\x80a\x97@\xa8\xa1\x9bx@\xa8\xa3\x1c\x81\n=\x08d\x9a\xf7'))