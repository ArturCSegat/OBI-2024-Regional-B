N = int(input())
instructions = input()

sala = 1

for i in instructions:
    if i == "E":
        sala = sala << 1
    elif i == "D":
        sala = (sala << 1) + 1

print(sala)

