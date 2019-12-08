with open("input.txt", "r") as image_file:
    image = image_file.readline().strip()
w, h = 25, 6
num_layers = len(image) // (w * h)

for y in range(h):
    for x in range(w):
        for l in range(num_layers):
            pixel = image[w * h * l + w * y + x]
            if pixel != "2":
                print("█" if pixel == "1" else " ", end="")
                break
    print()
