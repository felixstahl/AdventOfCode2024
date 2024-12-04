inputFile = open('AOC1input.txt').read().strip()

listOfLines = inputFile.split('\n')

listOfLefts = []
listOfRights = []

for line in listOfLines:
    print(line)
    left, right = line.split()
    left, right = int(left), int(right)
    listOfLefts.append(left)
    listOfRights.append(right)

listOfLefts = sorted(listOfLefts)
listOfRights = sorted(listOfRights)

answer = 0
for l, r in zip(listOfLefts,listOfRights):
    answer += abs(l-r)

print(answer)
#part 1 complete, no more time today.

