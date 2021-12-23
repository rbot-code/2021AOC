numFall = 0
with open("input1") as file:
    dp1 = int(file.readline())
    dp2 = int(file.readline())
    dp3 = int(file.readline())
    for line in file:
        newDepth = int(line)
        if (dp2+dp3+newDepth) > (dp1+dp2+dp3):
            numFall = numFall + 1
        dp1 = dp2
        dp2 = dp3
        dp3 = newDepth

print(numFall)
