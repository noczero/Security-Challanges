from helper.xor import *

if __name__ == '__main__':
    string = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal""".encode('ascii')

    output_actual = ("0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a262263"
                     "24272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b2028"
                     "3165286326302e27282f")

    key = "ICE".encode('ascii')

    encrypt = xor_repeating_key(string, key).hex()

    print("Encrypted : {} - Status : {}".format(encrypt, output_actual == encrypt))

