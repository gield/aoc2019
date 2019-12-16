from itertools import cycle, repeat


def run_phase(signal):
    base_pattern = [0, 1, 0, -1]
    for i in range(len(signal)):
        pattern = [k for j in base_pattern for k in repeat(j, i + 1)]
        total_sum = sum(a * b for a, b in zip([0] + signal, cycle(pattern)))
        signal[i] = abs(total_sum) % 10
    return signal


with open("input.txt") as f:
    signal = list(map(int, list(f.read().strip())))

for i in range(100):
    signal = run_phase(signal)
print("".join(map(str, signal[:8])))
