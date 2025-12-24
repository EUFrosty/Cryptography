from bits import xor, bits_to_blocks, bits_from_blocks, bits_to_bitstring

def feistel_round(left, right, key, F):
    L = right
    R = xor(left, F(right, key))
    return L, R

def feistel_inverse(left, right, key, F):
    R = left
    L = xor(right, F(left, key))
    return L, R

def feistel_encrypt(plaintext, keys, F, rounds):
    left, right = bits_to_blocks(plaintext, len(plaintext) // 2)
    for i in range(len(keys)):
        left, right = feistel_round(left, right, keys[i], F)
    return bits_from_blocks([left,right])

def feistel_decrypt(ciphertext, keys, F, rounds):
    left, right = bits_to_blocks(ciphertext, len(ciphertext) //2)
    for i in range(len(keys)-1, -1, -1):
        left, right = feistel_inverse(left, right, keys[i], F)
    return bits_from_blocks([left,right])


def example_F(right, key):
    return xor(right, key)

plaintext = [1, 0, 1, 0, 0, 1, 1, 0]
keys = [[1, 0, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]
rounds = 3

ciphertext = feistel_encrypt(plaintext, keys, example_F, rounds)
print("Ciphertext:", bits_to_bitstring(ciphertext))

decrypted = feistel_decrypt(ciphertext, keys, example_F, rounds)
print("Decrypted:", bits_to_bitstring(decrypted))