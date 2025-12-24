from lfsr import run_lfsr, lfsr_step

def shrinking_generator(seed1, taps1, seed2, taps2, steps):
    counter = 0
    state1 = seed1[:]
    state2 = seed2[:]
    while counter != 20:
        state1, output1 = lfsr_step(state1, taps1)
        state2, output2 = lfsr_step(state2, taps2)
        if output1 == 1:
            counter += 1
            print(output2, end="")
    return


if __name__ == "__main__":
    seed1 = [1, 0, 1, 1]
    taps1 = [1, 3]
    seed2 = [1, 1, 0, 1]
    taps2 = [2, 4]

    steps = 20

    shrinking_generator(seed1, taps1, seed2, taps2, steps)