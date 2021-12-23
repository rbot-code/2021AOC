numFall = 0
with open("input1") as file:
    currentDepth = int(file.readline())
    for line in file:
        newDepth = int(line)
        if newDepth > currentDepth:
            numFall = numFall + 1
        currentDepth = newDepth

print(numFall)
    
