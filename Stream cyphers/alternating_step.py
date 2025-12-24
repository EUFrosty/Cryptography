from lfsr import lfsr_step, run_lfsr

def alternating_step(seed1, taps1, seed2, taps2, seed3, taps3, steps):
    state1 = seed1
    state2 = seed2
    state3 = seed3
    counter = 0
    
    while counter != steps:
        state1, output1 = lfsr_step(state1, taps1)
        if output1 == 0:
            state2, output2 = lfsr_step(state2, taps2)
            output3 = state3[0]

        if output1 == 1:
            state3, output3 = lfsr_step(state3, taps3)
            output2 = state2[0]

        print(output2^output3, end="")
        counter += 1

if __name__ == "__main__":
    seed1 = [1, 0, 1]
    taps1 = [1, 3]
    seed2 = [1, 1, 0, 1]
    taps2 = [2, 4]
    seed3 = [0, 1, 1, 0, 1]
    taps3 = [1, 2, 5]

    steps = 20

    alternating_step(seed1, taps1, seed2, taps2, seed3, taps3, steps)
    print()