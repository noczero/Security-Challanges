# define variable
string = '1c0111001f010100061a024b53535009181c'
xor_agains = '686974207468652062756c6c277320657965'
actual_output = '746865206b696420646f6e277420706c6179'


def xor_hex(input, xor_againts):
    '''
    """Takes two equal-length hex encoded buffers and produces their XOR combination."""
    :param input: hex input
    :param xor_againts: xor againts
    :return: XOR fixed
    '''
    # xor ^ operator against xor and string
    xor = int(string, 16) ^ int(xor_agains, 16)

    # convert to hex, remove 0x
    xor_hex = hex(xor)[2:]
    return xor_hex


# invoke function
output = xor_hex(string, xor_agains)
# output
print("Output : {} - Status : {}".format(output, xor_hex == actual_output))
