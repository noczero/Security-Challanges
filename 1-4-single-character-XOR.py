from helper.xor import *

if __name__ == '__main__':
    # open data_4.txt
    with open('data/data_4.txt') as f:
        ciphers = []
        for line in f.readlines():
            ciphers.append(bytes.fromhex(line.strip())) # read lines and append it

    # Decrpyt the message
    list_msgs = []
    for cipher in ciphers:
        key = break_xor_char_key(cipher)
        list_msg = xor_single_char_key(cipher , key)
        list_msgs.append(list_msg)

    # find max
    find_msg = max(list_msgs, key=english_test).decode('ascii')

    print("Encrypted single-chars XOR : {}".format(find_msg))
