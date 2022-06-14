from challenge1 import hex_to_b64
import binascii

# fixed XOR
def fixed_xor(buf1, buf2):
    if len(buf1) == len(buf2):
        b1 = binascii.unhexlify(buf1)
        b2 = binascii.unhexlify(buf2)
        # b1 = hex_to_b64(buf1)
        # b2 = hex_to_b64(buf2)
        result = [x ^ y for x, y in zip(b1, b2)]
        return bytes(result).hex()

print(fixed_xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965'))
print('746865206b696420646f6e277420706c6179')
