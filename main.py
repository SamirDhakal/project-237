input = int(input("enter number: "))

while input > 0:
    with open(f"file{input}.txt", "w+") as f:
        f.write(str(input))
        input -= 1