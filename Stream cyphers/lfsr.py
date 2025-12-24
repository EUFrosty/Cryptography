import sys

def lfsr_step(seed, taps):
    state = seed[:]
    result = 0
    output = seed[-1]
    for i in range(len(taps)):
        result = result ^ state[taps[i]-1]
    tmp = state[0]
    state[0] = result
    for i in range(1, len(state)):
        tmptmp = state[i]
        state[i] = tmp
        tmp = tmptmp
        
    return state, output

def run_lfsr(seed, taps, bit_count):
    state = seed[:]
    result = []
    for i in range(bit_count):
        state, output = lfsr_step(state, taps)
        result.append(output)
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python lfsr.py <bit_count>")
        sys.exit(1)

    bit_count = int(sys.argv[1])

    seed = [1, 0, 0, 1]
    taps = [1, 4]

    encription = run_lfsr(seed, taps, bit_count)

    for i in range(len(encription)):
        print(encription[i], end="")
    print()