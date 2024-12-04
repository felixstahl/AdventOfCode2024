inputFile = open('AOC1input.txt').read().strip()

listOfLines = inputFile.split('\n')

listOfLefts = []
listOfRights = []

for line in listOfLines:
    left, right = line.split()
    listOfLefts.append(left)
    listOfRights.append(right)

listOfLefts = sorted(left)
listOfRights = sorted(right)


#no more time today. got to go

