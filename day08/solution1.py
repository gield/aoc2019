with open("input.txt", "r") as image_file:
    image = image_file.readline().strip()
w, h = 25, 6

least_zeros = float('inf')
layers = [image[i:i + w * h] for i in range(0, len(image), w * h)]
for layer in layers:
    if (num_zeros := layer.count("0")) < least_zeros:
        least_zeros = num_zeros
        final_count = layer.count("1") * layer.count("2")
print(final_count)
