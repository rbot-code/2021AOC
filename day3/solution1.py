dataLen = 12 #Each data string is 12 bits long
total = [0]*dataLen
numOnes = [0]*dataLen
with open("input") as file:
    for line in file:
        data = list(line.strip())
        for i, dat in enumerate(data):
            total[i] = total[i] + 1
            if dat == "1":
                numOnes[i] = numOnes[1] + 1

#Create gamma rate
gamma = [0]*dataLen
for i, each in enumerate(total):
    print(each)
    print(numOnes[i])
    if numOnes[i] > (each/2):
        gamma[i] = 1

print(gamma)
#epsilon
