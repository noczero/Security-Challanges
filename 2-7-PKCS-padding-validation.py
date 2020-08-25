from helper.AES import unpad, BadPaddingException


padded = "ICE ICE BABY\x04\x04\x04\x04".encode('ascii')
unpadded = "ICE ICE BABY".encode('ascii')

assert(unpadded == unpad(padded))
print("Padded : {} - Unpadded : {} - Status : {}".format(padded, unpadded, unpadded == unpad(padded)))

try:
    result = unpad("ICE ICE BABY\x05\x05\x05\x05".encode('ascii'))
    assert False
except BadPaddingException:
    pass

try:
    unpad("ICE ICE BABY\x01\x02\x03\x04".encode('ascii'))
    assert False
except BadPaddingException:
    pass
