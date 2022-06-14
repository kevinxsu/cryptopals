import base64
import binascii

# Convert hex to base64
def hex_to_b64(s : str) -> str:
    # interpret the hex as bytes
    # encode those bytes to base64
    return base64.b64encode(binascii.unhexlify(s))

# print(hex_to_b64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))
# assert('SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t' == hex_to_b64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))
