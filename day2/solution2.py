horizPos = 0
depth = 0
aim = 0
with open("input") as file:
    for line in file:
        cmd = line.strip().split(" ")
        if cmd[0] == "forward":
            horizPos = horizPos + int(cmd[1])
            depth = depth + aim*int(cmd[1])
        elif cmd[0] == "up":
            aim = aim - int(cmd[1])
        elif cmd[0] == "down":
            aim = aim + int(cmd[1])

print(horizPos*depth)
