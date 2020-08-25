from helper.AES import pad

string = "YELLOW SUBMARINE"
actual_output = "YELLOW SUBMARINE\x04\x04\x04\x04"

padded_output = pad(string.encode('ascii'), 20)

print("Output : {} - Status : {}".format(padded_output, actual_output.encode('ascii') == padded_output))