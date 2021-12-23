dataLen = 12 #Each data string is 12 bits long
total = [0]*dataLen
numOnes = [0]*dataLen
with open("input") as file:
    for line in file:
        data = list(line.strip())
        for i, dat in enumerate(data):
            total[i] = total[i] + 1
            if dat == "1":
                numOnes[i] = numOnes[i] + 1

#Create gamma rate
gamma = [0]*dataLen
for i, each in enumerate(total):
    print(each)
    print(numOnes[i])
    if numOnes[i] > (each/2):
        gamma[i] = 1

#Epsilon is just the opposite of gamma
epsilon = [0]*dataLen
for i, val in enumerate(gamma):
    if val == 0:
        epsilon[i] = 1

print(gamma)
print(epsilon)
#Not yet figured out how to convert to binary and ints from list

#gamma = ''.join(gamma)
#print(bytes(gamma))
#print(int.from_bytes(bytes(gamma)))
#print((int(bin(gamma))) * (int(bin(epsilon))))

#Converted by hand:
#gamma = 2663
#epsilon = 1432

#Helpful sites:
#https://stackoverflow.com/questions/38935169/convert-elements-of-a-list-into-binary
#https://wiki.python.org/moin/BitwiseOperators
#https://docs.python.org/3/library/stdtypes.html
