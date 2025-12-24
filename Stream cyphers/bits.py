def bits_to_bitstring(b):
    return "".join(map(str, b))


def bits_to_int(b):
    return int(bits_to_bitstring(b), 2)


def bits_to_blocks(b, size):
    padded = b[:]
    pad_bits = (-len(b)) % size
    padded.extend([0] * pad_bits)
    return [padded[i : i + size] for i in range(0, len(padded), size)]


def bits_to_bytes(b):
    return bytes([bits_to_int(byte) for byte in bits_to_blocks(b, 8)])


def bits_to_string(b):
    return bits_to_bytes(b).decode("utf-8")


def bits_to_hex(b):
    return bits_to_bytes(b).hex()


def bits_from_bitstring(s):
    return [int(bit) for bit in s]


def bits_from_bytes(s):
    return [int(bit) for byte in s for bit in format(byte, "08b")]


def bits_from_string(s):
    return bits_from_bytes(s.encode("utf-8"))


def bits_from_int(s, size):
    return bits_from_bitstring(format(s, "0" + str(size) + "b"))


def bits_from_blocks(s):
    return [int(bit) for block in s for bit in block]


def bits_from_hex(s):
    return bits_from_bytes(bytes.fromhex(s))


def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]
