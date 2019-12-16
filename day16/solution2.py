from itertools import cycle, repeat


def run_phase(signal):
    # The first digit is based on the total sum
    # The second digit is based on the total sum minus the first digit
    # The third digit is based on the total sum minus first and second digit
    # e.g. 4, 1, 2 --> 7, 3, 2
    total_sum = sum(signal)
    for i in range(len(signal)):
        single_digit = abs(total_sum) % 10
        total_sum -= signal[i]
        signal[i] = single_digit
    return signal


with open("input.txt") as f:
    signal = list(map(int, list(f.read().strip())))
    signal = signal * 10_000

offset = int("".join(map(str, signal[:7])))
if offset > len(signal):
    print("The offset is larger than the signal")
elif offset > len(signal) // 2:
    print("The offset is larger than half of the signal")
    print("The first `offset` digits will be 0 at line `offset` (and further)")
    print("So we skip those and just multiply the remaining digits with 1")
else:
    print("The offset is not larger than half of the signal")

signal = signal[offset:]
for i in range(100):
    signal = run_phase(signal) 
print("".join(map(str, signal[:8])))
