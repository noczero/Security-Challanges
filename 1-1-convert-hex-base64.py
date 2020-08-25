import codecs

# define variable
string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
actual_output = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

# using codecs
base64_output = codecs.encode(codecs.decode(string, 'hex'), 'base64').decode()
print('Output : {} - Compare : {}'.format(base64_output, base64_output.replace("\n",'') == actual_output))
