import re

def readInputFile(path):
    result = []
    with open(path, 'r') as f:
        for line in f:
            if line[len(line) - 1] == '\n':
                result.append(line[0: -1])
            else:
                result.append(line)
    return result

def isDigit(c):
    return c.isdigit()

def getFirstDigitInString(s):
    for i in range(len(s)):
        ch = s[i]
        if ch == '0':
            return 0
        if ch == '1':
            return 1
        if ch == '2':
            return 2
        if ch == '3':
            return 3
        if ch == '4':
            return 4
        if ch == '5':
            return 5
        if ch == '6':
            return 6
        if ch == '7':
            return 7
        if ch == '8':
            return 8
        if ch == '9':
            return 9
        if ch == 'o' and i <= len(s) - 3 and s[i+1] == 'n' and s[i+2] == 'e':
            return 1
        if ch == 't' and i <= len(s) - 3 and s[i+1] == 'w' and s[i+2] == 'o':
            return 2
        if ch == 't' and i <= len(s) - 5 and s[i+1] == 'h' and s[i+2] == 'r' and s[i+3] == 'e' and s[i+4] == 'e':
            return 3
        if ch == 'f' and i <= len(s) - 4 and s[i+1] == 'o' and s[i+2] == 'u' and s[i+3] == 'r':
            return 4
        if ch == 'f' and i <= len(s) - 4 and s[i+1] == 'i' and s[i+2] == 'v' and s[i+3] == 'e':
            return 5
        if ch == 's' and i <= len(s) - 3 and s[i+1] == 'i' and s[i+2] == 'x':
            return 6
        if ch == 's' and i <= len(s) - 5 and s[i+1] == 'e' and s[i+2] == 'v' and s[i+3] == 'e' and s[i+4] == 'n':
            return 7
        if ch == 'e' and i <= len(s) - 5 and s[i+1] == 'i' and s[i+2] == 'g' and s[i+3] == 'h' and s[i+4] == 't':
            return 8
        if ch == 'n' and i <= len(s) - 4 and s[i+1] == 'i' and s[i+2] == 'n' and s[i+3] == 'e':
            return 9
        if ch == 'z' and i <= len(s) - 4 and s[i+1] == 'e' and s[i+2] == 'r' and s[i+3] == 'o':
            return 0
    print(f'first {s}')

def getLastDigitInString(s):
    for i in range(len(s) - 1, -1, -1):
        ch = s[i]
        if ch == '0':
            return 0
        if ch == '1':
            return 1
        if ch == '2':
            return 2
        if ch == '3':
            return 3
        if ch == '4':
            return 4
        if ch == '5':
            return 5
        if ch == '6':
            return 6
        if ch == '7':
            return 7
        if ch == '8':
            return 8
        if ch == '9':
            return 9
        if ch == 'e' and i >= 2 and s[i-1] == 'n' and s[i-2] == 'o':
            return 1
        if ch == 'e' and i >= 3 and s[i-1] == 'n' and s[i-2] == 'i' and s[i-3] == 'n':
            return 9
        if ch == 'e' and i >= 3 and s[i-1] == 'v' and s[i-2] == 'i' and s[i-3] == 'f':
            return 5
        if ch == 'e' and i >= 4 and s[i-1] == 'e' and s[i-2] == 'r' and s[i-3] == 'h' and s[i-4] == 't':
            return 3
        if ch == 'o' and i >= 2 and s[i-1] == 'w' and s[i-2] == 't':
            return 2
        if ch == 'o' and i >= 3 and s[i-1] == 'r' and s[i-2] == 'e' and s[i-3] == 'z':
            return 0
        if ch == 'r' and i >= 3 and s[i-1] == 'u' and s[i-2] == 'o' and s[i-3] == 'f':
            return 4
        if ch == 'x' and i >= 2 and s[i-1] == 'i' and s[i-2] == 's':
            return 6
        if ch == 'n' and i >= 4 and s[i-1] == 'e' and s[i-2] == 'v' and s[i-3] == 'e' and s[i-4] == 's':
            return 7
        if ch == 't' and i >= 4 and s[i-1] == 'h' and s[i-2] == 'g' and s[i-3] == 'i' and s[i-4] == 'e':
            return 8
    print(f'last {s}')

def day_1():
    lines = readInputFile("./input/input1_2.txt")

    calibrationSum = 0
    for line in lines:
        firstDigit = getFirstDigitInString(line)
        lastDigit = getLastDigitInString(line)

        calibrationValue = lastDigit if firstDigit == 0 else firstDigit * 10 + lastDigit
        calibrationSum += calibrationValue

    print(calibrationSum)

def day_2():
    lines = readInputFile("./input/input2_1.txt")

    sum = 0

    for line in lines:
        maxRed = None
        maxGreen = None
        maxBlue = None
        game, rounds = line.split(":")
        for round in rounds.split(";"):
            cubes = round.split(",")
            for cube in cubes:
                if "blue" in cube:
                    blueCubes = int(cube.split(" blue")[0])
                    if maxBlue is None or blueCubes > maxBlue:
                        maxBlue = blueCubes
                if "red" in cube:
                    redCubes = int(cube.split(" red")[0])
                    if maxRed is None or redCubes > maxRed:
                        maxRed = redCubes
                if "green" in cube:
                    greenCubes = int(cube.split(" green")[0])
                    if maxGreen is None or greenCubes > maxGreen:
                        maxGreen = greenCubes
        sum += maxRed * maxGreen * maxBlue
    print(sum)

def day_3():
    lines = readInputFile("./input/input3_1.txt")

    partNumbers = []
    starSymbols = {}

    lineCount = len(lines)
    columnCount = len(lines[0])

    for l in range(lineCount):
        partNumber = None
        numberStart = None
        numberEnd = None
        for c in range(columnCount):
            if lines[l][c].isdigit():
                if partNumber is None:
                    partNumber = int(lines[l][c])
                    numberStart = c
                    numberEnd = c
                else:
                    partNumber = partNumber * 10 + int(lines[l][c])
                    numberEnd = c
            
            if not lines[l][c].isdigit() or c == columnCount - 1:
                if partNumber is not None:
                    # print(f'{partNumber} - {numberStart} - {numberEnd}')
                    minLine = max(l - 1, 0)
                    maxLine = min(l + 1, lineCount - 1)

                    minColumn = max(numberStart - 1, 0)
                    maxColumn = min(numberEnd + 1, columnCount - 1)

                    # print(partNumber)
                    # print(f'line {minLine} {maxLine} col {minColumn} {maxColumn}')
                    isPartNumber = False
                    for i in range(minLine, maxLine + 1):
                        for j in range(minColumn, maxColumn + 1):
                            if lines[i][j] == "*":
                                if starSymbols.get(f'{i}_{j}') is None:
                                    starSymbols[f'{i}_{j}'] = [partNumber]
                                else:
                                    starSymbols.get(f'{i}_{j}').append(partNumber)
                                
                            if not lines[i][j].isdigit() and lines[i][j] != '.':
                                isPartNumber = True
                    
                    # print(isPartNumber)
                    if isPartNumber:
                        partNumbers.append(partNumber)

                    partNumber = None
                    numberStart = None
                    numberEnd = None
    sum = 0
    for n in partNumbers:
        sum += n
    
    print(sum)
    
    sum2 = 0
    for key in starSymbols:
        if len(starSymbols.get(key)) == 2:
            sum2 += starSymbols.get(key)[0] * starSymbols.get(key)[1]
    print(sum2)

def day_4():
    lines = readInputFile("./input/input4.txt")

    sum = 0
    multipliers = {}
    for i in range(len(lines)):
        card = lines[i]
        winningNumbersString = ((card.split(':')[1]).split("|")[0])
        winningNumbers = [int(x) for x in re.split(r' +', winningNumbersString)[1:-1]]

        chosenNumbersString = ((card.split(':')[1]).split("|")[1])
        chosenNumbers = [int(x) for x in re.split(r' +', chosenNumbersString)[1:]]

        matchingNumbers = 0
        for winningNumber in winningNumbers:
            if winningNumber in chosenNumbers:
                matchingNumbers += 1

        currentCardMultiplier = multipliers.get(i) if multipliers.get(i) is not None else 1
        sum += currentCardMultiplier
        if matchingNumbers > 0:
            for j in range(i + 1, i + matchingNumbers + 1):
                if multipliers.get(j) is None:
                    multipliers[j] = 1 + currentCardMultiplier
                else:
                    multipliers[j] += currentCardMultiplier
    
    print(sum)

def sortingFunction(r):
    return r[1]

def day_5():
    lines = readInputFile("./input/input5.txt")

    # seeds = [int (x) for x in lines[0].split(":")[1].split(" ") if x != ""]
    seedPairsRaw = [int (x) for x in lines[0].split(":")[1].split(" ") if x != ""]
    # seeds = []
    # for i in range(0, len(seedPairs), 2):
    #     start = seedPairs[i]
    #     seedRangeLength = seedPairs[i + 1]
    #     for j in range(seedRangeLength):
    #         seeds.append(start + j)
    seedPairs = []
    for i in range(0, len(seedPairsRaw), 2):
        seedPairs.append([seedPairsRaw[i], seedPairsRaw[i] + seedPairsRaw[i+1] - 1])
    
    maps = []
    ranges = {}
    current_range = None
    for i in range(2, len(lines)):
        line = lines[i]

        if "map" in line:
            if current_range is not None:
                ranges.get(current_range).sort(key=sortingFunction)

            current_range = line.split(" ")[0]
            ranges[current_range] = []
            maps.append(current_range)
        elif line == "":
            continue
        else:
            numbers = [int(x) for x in line.split(" ") if x != ""]
            ranges.get(current_range).append(numbers)

    ranges.get(current_range).sort(key=sortingFunction)

    # print(ranges)   
    # print(maps)

    # closestLocation = None
    # print(len(seeds))
    # for seed in seeds:
    #     convertedNumber = seed

    #     for m in maps:
    #         rangesForMap = ranges.get(m)

    #         for currentRange in rangesForMap:
    #             # print(currentRange)
    #             if currentRange[1] <= convertedNumber and (currentRange[1] + currentRange[2]) >= convertedNumber:
    #                 # print("found")
    #                 convertedNumber = currentRange[0] + (convertedNumber - currentRange[1])
    #                 break
            
    #         # print(convertedNumber)
        
    #     if closestLocation is None or convertedNumber < closestLocation:
    #         closestLocation = convertedNumber

    pairs = []
    closestLocation = None
    for seedPair in seedPairs:
        # print(f"processing seed pair {seedPair}")
        pairs = [seedPair]

        for m in maps:
            # print(f"input for map {m}: {pairs}")
            rangesForMap = ranges.get(m)

            newPairs = []

            for pair in pairs:
                left = pair[0]
                right = pair[1]

                for currentRange in rangesForMap:
                    if currentRange[1] + currentRange[2] - 1 < left:
                        continue
                    elif right < currentRange[1]:
                        continue
                    else:
                        # uncovered left
                        if currentRange[1] > left:
                            newPairs.append([left, currentRange[1] - 1])

                        newLeft = max(left, currentRange[1])
                        newRight = min(right, currentRange[1] + currentRange[2] - 1)

                        newPairs.append([currentRange[0] + newLeft - currentRange[1], currentRange[0] + newRight - currentRange[1]])

                        left = newRight + 1
                        if left > right:
                            break
                
                if left <= right:
                    newPairs.append([left, right])
                
            pairs = newPairs
        for pair in pairs:
            if closestLocation is None or pair[0] < closestLocation:
                closestLocation = pair[0]
            
        
    # print(pairs)
    print(f"closest location is {closestLocation}")
    # closest location is 227653707


def day_6():
    lines = readInputFile("./input/input6.txt")

    # times = [int(x) for x in re.split(r" +", lines[0].split(":")[1])[1:]]
    # distances = [int(x) for x in re.split(r" +", lines[1].split(":")[1])[1:]]
    # print(times)
    # print(distances)

    time = int("".join(re.split(r" +", lines[0].split(":")[1])))
    recordDistance = int("".join(re.split(r" +", lines[1].split(":")[1])))

    
    # product = 1
    # for i in range(len(times)):
    #     time = times[i]
    #     recordDistance = distances[i]

    #     count = 0

    #     for j in range(0, time + 1, 1):
    #         distance = (time - j) * j
    #         if distance > recordDistance:
    #             count += 1
        
    #     product *= count
    
    # print(product)
    count = 0
    for j in range(0, time + 1, 1):
        distance = (time - j) * j
        if distance > recordDistance:
            count += 1
    
    print(count)

import functools
def day7sort(a, b):
    if a.get("typeN") > b.get("typeN"):
        return 1
    if a.get("typeN") < b.get("typeN"):
        return -1

    cardsValues = "J23456789TQKA"
    for i in range(5):
        ca = cardsValues.index(a.get("cards")[i])
        cb = cardsValues.index(b.get("cards")[i])
        if ca < cb:
            return -1
        if ca > cb:
            return 1
    return 0
            
        

def day_7():
    lines = readInputFile("./input/input7.txt")

    hands = []
    for line in lines:
        cards = line.split(" ")[0]
        bid = int(line.split(" ")[1])

        aux = {}
        for c in cards:
            if aux.get(c) is None:
                aux[c] = 0

            aux[c] += 1
        
        handType = None
        handTypeN = None
        if len(aux) == 1:
            handType = "five"
            handTypeN = 6
        elif len(aux) == 2:
            if 1 in aux.values() or 4 in aux.values():
                if "J" in aux:
                    handType = "five"
                    handTypeN = 6
                else:
                    handType = "four"
                    handTypeN = 5
            else:
                if "J" in aux:
                    handType = "five"
                    handTypeN = 6
                else:
                    handType = "full"
                    handTypeN = 4
        elif len(aux) == 3:
            if 3 in aux.values():
                if "J" in aux:
                    handTypeN = "four"
                    handTypeN = 5
                else:
                    handType = "three"
                    handTypeN = 3
            else:
                if "J" in aux:
                    if aux.get("J") == 1:
                        handType = "full"
                        handTypeN = 4
                    else:
                        handType = "four"
                        handTypeN = 5
                else:
                    handType = "two"
                    handTypeN = 2
        elif len(aux) == 4:
            if "J" in aux:
                handType = "three"
                handTypeN = 3
            else:
                handType = "one"
                handTypeN = 1
        else:
            if "J" in aux:
                handType = "one"
                handTypeN = 1
            else:
                handType = "high"
                handTypeN = 0

        hands.append({
            "cards": cards,
            "bid": bid,
            "type": handType,
            "typeN": handTypeN
        })
    
    hands.sort(key=functools.cmp_to_key(day7sort))
    
    sum = 0
    for i in range(len(hands)):
        sum += (i + 1) * hands[i]["bid"]

    print(sum)

def gdc(a, b):
    # if a == b:
    #     return a

    # if a > b:
    #     return gdc(a - b, b)
    # else:
    #     return gdc(a, b - a)
    while a != b:
        if a > b:
            a, b = a - b, b
        else:
            a, b = a, b - a 
    
    return a

def lca(a, b):
    return (a * b) / gdc(a, b)

def day8():
    lines = readInputFile("./input/input8.txt")

    sequence = lines[0]
    elements = {}

    startingElements = []

    for i in range(2, len(lines)):
        line = lines[i]
        element, moves = line.split(" = (")
        leftMove, rightMove = moves.split(", ")

        elements[element] = {
            "left": leftMove,
            "right": rightMove[:-1]
        }

        if element[-1] == 'A':
            startingElements.append(element)
    
    stepsForEachElem = []
    for startingElement in startingElements:
        index = 0
        steps = 0
        currentElement = startingElement


        found = 0

        while True:
            steps += 1
            move = sequence[index]

            currentElementMoves = elements.get(currentElement)
            if move == "L":
                currentElement = currentElementMoves["left"]
            else:
                currentElement = currentElementMoves["right"]
            
            if currentElement[-1] == "Z":
                found += 1
                if found == 1:
                    stepsForEachElem.append(steps)
                    break
            
            if index == len(sequence) - 1:
                index = 0
            else:
                index += 1

    print (stepsForEachElem)
    result = lca(stepsForEachElem[0], stepsForEachElem[1])
    i = 2
    while i < len(stepsForEachElem):
        print(result)
        currentSteps = stepsForEachElem[i]

        result = lca(result, currentSteps)
        i += 1

    print(result)

def day9():
    lines = readInputFile("./input/input9.txt")

    sum = 0
    firstSum = 0
    for line in lines:
        numbers = [int(x) for x in line.split(" ")]

        firstValues = []
        lastValues = []
        
        while True:
            firstValues.append(numbers[0])
            lastValues.append(numbers[-1])

            shouldStop = True

            newNumbers = []
            for i in range(1, len(numbers)):
                diff = numbers[i] - numbers[i-1]
                
                newNumbers.append(diff)

                if diff != 0:
                    shouldStop = False
            
            if shouldStop:
                break
                
            numbers = newNumbers
        
        currentSum = 0
        for l in lastValues:
            currentSum += l
        
        sum += currentSum

        currentFirstSum = 0
        for i in range(len(firstValues) - 1, -1, -1):
            f = firstValues[i]

            currentFirstSum = f - currentFirstSum

        firstSum += currentFirstSum

    print(sum)
    print(firstSum)

# def day10():
#     nextPositions = {
#         "|": [[-1, 0], [1, 0]],
#         "-": [[0, -1], [0, 1]],
#         "L": [[-1, 0], [0, 1]],
#         "J": [[-1, 0], [0, -1]],
#         "7": [[0, -1], [1, 0]],
#         "F": [[0, 1], [1, 0]],
#         # "S": [[0, 1], [1, 0]]
#         "S": [[-1, 0], [0, 1]]
#     }

#     lines = readInputFile("./input/input10.txt")

#     startLine = None
#     startColumn = None
#     for i in range(len(lines)):
#         for j in range(len(lines[i])):
#             if lines[i][j] == "S":
#                 startLine = i
#                 startColumn = j
    
#     maxD = 1
#     q = [{"l": startLine, "c": startColumn, "d": 0}]
#     vis = {
#         f"{startLine}_{startColumn}": 1
#     }

#     while len(q) > 0:
#         e = q.pop(0)

#         l = e.get("l")
#         c = e.get("c")
#         dist = e.get("d")
#         pipeType = lines[e.get("l")][e.get("c")]

#         nextMoves = nextPositions.get(pipeType)
#         for next in nextMoves:
#             key = f"{l + next[0]}_{c + next[1]}"

#             if vis.get(key) == 1:
#                 continue
                
            
#             vis[key] = 1
#             q.append({"l": l + next[0], "c": c + next[1], "d": dist + 1})
#             if dist + 1 > maxD:
#                 maxD = dist + 1       
    
#     print(maxD)

# def day10():
#     nextPositions = {
#         "|": [[-1, 0, None, None], [1, 0, None, None]],
#         "-": [[0, -1, None, None], [0, 1, None, None]],
#         "L": [[-1, 0, "r", {"r": [0, 1], "l": [0, -1]}], [0, 1, "l", {"r": [1, 0], "l": [-1, 0]}]],
#         "J": [[-1, 0, "l", {"r": [0, 1], "l": [0, -1]}], [0, -1, "r", {"r": [-1, 0], "l": [1, 0]}]],
#         "7": [[0, -1, "l", {"r": [-1, 0], "l": [1, 0]}], [1, 0, "r", {"r": [0, -1], "l": [0, 1]}]],
#         "F": [[0, 1, "r", {"r": [1, 0], "l": [-1, 0]}], [1, 0, "l", {"r": [0, -1], "l": [0, 1]}]],
#         "S": [[1, 0, None, {"r": [0, -1], "l": [0, 1]}], [0, 1, None, {"r": [1, 0], "l": [-1, 0]}]] # test 1 and 3 and 4 and 5
#         # "S": [[-1, 0, None, {"r": [0, -1], "l": [0, 1]}], [0, 1, None, {"r": [1, 0], "l": [-1, 0]}]] # test 2
#     }

#     lines = readInputFile("./input/input10test5.txt")

#     startLine = None
#     startColumn = None
#     for i in range(len(lines)):
#         for j in range(len(lines[i])):
#             if lines[i][j] == "S":
#                 startLine = i
#                 startColumn = j
    
#     # to be init by input, test 1&3&4 counter clockwise
#     q = [{"l": startLine + 1, "c": startColumn}]
#     vis = {
#         f"{startLine}_{startColumn}": 1,
#         f"{startLine + 1}_{startColumn}": 1
#     }
#     turns = {
#         "l": 1,
#         "r": 0
#     }
#     # to be init by input, test 1&3&4 clockwise
#     # q = [
#     #     {"l": startLine, "c": startColumn + 1}
#     # ]
#     # vis = {
#     #     f"{startLine}_{startColumn}": 1,
#     #     f"{startLine}_{startColumn + 1}": 1
#     # }
#     # turns = {
#     #     "l": 0,
#     #     "r": 1
#     # }
#     while len(q) > 0:
#         e = q.pop(0)

#         l = e.get("l")
#         c = e.get("c")
#         pipeType = lines[e.get("l")][e.get("c")]

#         nextMoves = nextPositions.get(pipeType)
#         for next in nextMoves:
#             key = f"{l + next[0]}_{c + next[1]}"

#             if vis.get(key) == 1:
#                 continue
                
            
#             vis[key] = 1
#             q.append({"l": l + next[0], "c": c + next[1]})   
#             if next[2] is not None:
#                 turns[next[2]] += 1
    
#     side = "r" if turns["r"] > turns["l"] else "l"
#     print(side)
#     print(turns)

#     finalQ = []
#     finalVis = {}
#     finalCount = 0

#     # q2 = [
#     #     {"l": startLine, "c": startColumn + 1}
#     # ]
#     # vis2 = {
#     #     f"{startLine}_{startColumn}": 1,
#     #     f"{startLine}_{startColumn + 1}": 1
#     # }
#     q2 = [{"l": startLine + 1, "c": startColumn}]
#     vis2 = {
#         f"{startLine}_{startColumn}": 1,
#         f"{startLine + 1}_{startColumn}": 1
#     }

#     s = nextPositions.get("S")[0]
#     whereToLook = [s[3].get(side)[0], s[3].get(side)[1]]
#     while len(q2) > 0:
#         e = q2.pop(0)

#         l = e.get("l")
#         c = e.get("c")
#         pipeType = lines[e.get("l")][e.get("c")]

#         if pipeType == "-" or pipeType == "|":
#             newL = l + whereToLook[0]
#             newC = c + whereToLook[1]
#             newKey = f"{newL}_{newC}"
#             if newL >= 0 and newL < len(lines) and newC >= 0 and newC < len(lines[0]) and vis.get(newKey) == None and finalVis.get(newKey) == None:
#                 finalQ.append({"l": newL, "c": newC})
#                 finalVis[newKey] = 1
#                 finalCount += 1
        
#         nextMoves = nextPositions.get(pipeType)
#         for next in nextMoves:
#             key = f"{l + next[0]}_{c + next[1]}"

#             if vis2.get(key) == 1:
#                 continue

#             vis2[key] = 1

#             q2.append({"l": l + next[0], "c": c + next[1]})

#             if next[3] is not None:
#                 whereToLook = [next[3].get(side)[0], next[3].get(side)[1]]
    
#     moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#     print(f"final q {finalQ}")
#     while len(finalQ):
#         e = finalQ.pop(0)

#         l = e.get("l")
#         c = e.get("c")

#         for move in moves:
#             newL = l + move[0]
#             newC = c + move[1]
            
#             newKey = f"{newL}_{newC}"

#             if vis.get(newKey) == 1 or finalVis.get(newKey) == 1:
#                 continue
            
#             finalVis[newKey] = 1

#             finalCount += 1
#             finalQ.append({"l": newL, "c": newC})
   

#     print(finalCount)

def day10():
    nextPositions = {
        "|": [[-1, 0], [1, 0]],
        "-": [[0, -1], [0, 1]],
        "L": [[-1, 0], [0, 1]],
        "J": [[-1, 0], [0, -1]],
        "7": [[0, -1], [1, 0]],
        "F": [[0, 1], [1, 0]],
        "S": [[0, 1], [1, 0]]
        # "S": [[-1, 0], [0, 1]]
    }

    lines = readInputFile("./input/input10.txt")

    startLine = None
    startColumn = None
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "S":
                startLine = i
                startColumn = j
    sVal = "L"
    
    q = [{"l": startLine, "c": startColumn, "d": 0}]
    vis = {
        f"{startLine}_{startColumn}": 1
    }

    while len(q) > 0:
        e = q.pop(0)

        l = e.get("l")
        c = e.get("c")
        dist = e.get("d")
        pipeType = lines[e.get("l")][e.get("c")]

        nextMoves = nextPositions.get(pipeType)
        for next in nextMoves:
            key = f"{l + next[0]}_{c + next[1]}"

            if vis.get(key) == 1:
                continue
                
            
            vis[key] = 1
            q.append({"l": l + next[0], "c": c + next[1], "d": dist + 1})

    count = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            key = f"{i}_{j}"

            if vis.get(key) == 1:
                continue
            
            intersections = 0
            lastIntersection = None
            for k in range(j + 1, len(lines[i])):
                newKey = f"{i}_{k}"

                val = sVal if lines[i][k] == "S" else lines[i][k]
                if vis.get(newKey) == 1:
                    if val == "|":
                        intersections += 1
                    elif val == "F":
                        intersections += 1
                        lastIntersection = "F"
                    elif val == "7" and lastIntersection == "F":
                        intersections += 1
                        lastIntersection = None
                    elif val == "L":
                        intersections += 1
                        lastIntersection = "L"
                    elif val == "J" and lastIntersection == "L":
                        intersections += 1
                        lastIntersection = None

            if intersections % 2 == 1:
                print(f"{i} {j}")
                count += 1

    print(count)

def printMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(f"{m[i][j]} ", end="")
        
        print("\n")

def day11():
    inputLines = readInputFile("./input/input11.txt")

    lines = {}
    columns = {}

    for i in range(len(inputLines)):
        for j in range(len(inputLines[0])):
            if inputLines[i][j] == "#":
                lines[i] = 1
                columns[j] = 1
    
    # print(lines.keys())
    # print(columns.keys())
    # printMatrix(inputLines)

    newImage = []
    numberOfColumns = 2 * len(inputLines[0]) - len(columns.keys())
    for i in range(len(inputLines)):
        if lines.get(i) == None:
            for _ in range(2):
                newImage.append([])
                currentLine = len(newImage) - 1

                for _ in range(numberOfColumns):
                    newImage[currentLine].append(".")
        else:
            newImage.append([])
            currentLine = len(newImage) - 1
            for j in range(len(inputLines[0])):
                if columns.get(j) == None:
                    newImage[currentLine].append(".")
                
                newImage[currentLine].append(inputLines[i][j])
    
    stars = []
    for i in range(len(newImage)):
        for j in range(len(newImage[i])):
            if newImage[i][j] == "#":
                stars.append([i, j])
    
    sum = 0
    for i in range(len(stars) - 1):
        for j in range(i + 1, len(stars)):
            sum += abs(stars[i][0] - stars[j][0]) + abs(stars[i][1] - stars[j][1])

    print(sum)

def day11_2():
    inputLines = readInputFile("./input/input11.txt")

    lines = {}
    columns = {}
    stars = []

    expansion = 1000000 # later 10, 100, 1000000

    for i in range(len(inputLines)):
        for j in range(len(inputLines[0])):
            if inputLines[i][j] == "#":
                lines[i] = 1
                columns[j] = 1

                
                stars.append([i, j])
    
    emptyLines = []
    for i in range(len(inputLines)):
        if lines.get(i) is None:
            emptyLines.append(i)
    
    emptyColumns = []
    for i in range(len(inputLines[0])):
        if columns.get(i) is None:
            emptyColumns.append(i)
    
    # print(lines.keys())
    # print(columns.keys())
    # printMatrix(inputLines)

    sum = 0
    for i in range(len(stars) - 1):
        for j in range(i + 1, len(stars)):
            minLine = min(stars[i][0], stars[j][0])
            maxLine = max(stars[i][0], stars[j][0])
            eL = len(list(filter(lambda x: x > minLine and x < maxLine, emptyLines)))

            minColumn = min(stars[i][1], stars[j][1])
            maxColumn = max(stars[i][1], stars[j][1])
            eC = len(list(filter(lambda x: x > minColumn and x < maxColumn, emptyColumns)))

            sum += abs(stars[i][0] - stars[j][0]) + abs(stars[i][1] - stars[j][1]) + (expansion - 1) * eL + (expansion - 1) * eC

    print(sum)

def myPrint(s, t):
    prefix = ""
    for i in range(t):
        prefix += " "
    
    print(f"{prefix}{s}")

def iterate(firstNotation, secondNotation, t):
    # myPrint(f"{firstNotation} - {secondNotation}", t)
    firstIndex = 0
    secondIndex = 0
    while firstIndex < len(firstNotation) and firstNotation[firstIndex] != "?":
        # print(firstIndex)
        if firstNotation[firstIndex] == ".":
            firstIndex += 1
            continue

        if secondIndex == len(secondNotation):
            return 0
        
        nextGroup = secondNotation[secondIndex]

        for i in range(firstIndex, firstIndex + nextGroup):
            if i == len(firstNotation) or firstNotation[i] == ".":
                return 0
        
        if firstIndex + nextGroup == len(firstNotation):
            firstIndex = len(firstNotation)
            secondIndex += 1
        else:
            if firstNotation[firstIndex + nextGroup] == "#":
                return 0

            firstIndex = firstIndex + nextGroup + 1
            secondIndex += 1
    
    if firstIndex == len(firstNotation):
        if secondIndex == len(secondNotation):
            return 1
        return 0

    # if secondIndex == len(secondNotation):
    #     if "#" in firstNotation[firstIndex:]:

    # case 1 make ? as .
    # print("making ? as .")
    result1 = iterate(firstNotation[firstIndex + 1:], secondNotation[secondIndex:], t + 1)
    # myPrint(f"result1: {result1}", t)

    # case 2 make ? as #
    # but we need to make sure that everything else after this is correct
    
    # print("making ? as #")
    result2 = 0
    if secondIndex == len(secondNotation):
        result2 = 0 # just reassign it
    else:
        nextGroup = secondNotation[secondIndex]

        valid = True
        for i in range(firstIndex, firstIndex + nextGroup):
            if i == len(firstNotation) or firstNotation[i] == '.':
                valid = False
                break
        
        if valid is True:
            if firstIndex + nextGroup < len(firstNotation) and firstNotation[firstIndex + nextGroup] != "#":
                result2 = iterate(firstNotation[firstIndex + nextGroup + 1:], secondNotation[secondIndex + 1:], t + 1)
            elif firstIndex + nextGroup == len(firstNotation):
                result2 = iterate([], secondNotation[secondIndex + 1:], t+1)
                
    # myPrint(f"result2 {result2}", t)

    return result1 + result2

def day12():
    input = readInputFile("./input/input12.txt")

    notations = []
    for line in input:
        firstNotation, numbers = line.split(" ")
        secondNotation = [int(x) for x in numbers.split(",")]

        firstNotation2 = [c for c in firstNotation]
        secondNotation2 = [x for x in secondNotation]
        for i in range(1):
            firstNotation2.append("?")
            for c in firstNotation:
                firstNotation2.append(c)
            
            for x in secondNotation:
                secondNotation2.append(x)
        
        firstNotation3 = [c for c in firstNotation]
        secondNotation3 = [x for x in secondNotation]
        for i in range(2):
            firstNotation3.append("?")
            for c in firstNotation:
                firstNotation3.append(c)
            
            for x in secondNotation:
                secondNotation3.append(x)
        
        notations.append({
            "first": firstNotation,
            "second": secondNotation,
            "first2": firstNotation2,
            "second2": secondNotation2,
            "first3": firstNotation3,
            "second3": secondNotation3,
        })
    
    sum = 0
    print(len(notations))
    i = 0
    for notation in notations:
        i += 1
        firstNotation = notation["first"]
        secondNotation = notation["second"]

        possibilities = iterate(firstNotation, secondNotation, 0)
        # print(f'row result {possibilities ** 5}')

        poss2 = iterate(notation["first2"], notation["second2"], 0)
        y = poss2 // possibilities

        poss3 = iterate(notation["first3"], notation["second3"], 0)
        print(f"input {firstNotation} and {secondNotation} = {possibilities} - {poss2} ({poss2 / possibilities}) - {poss3} ({poss3 / poss2})")

        sum += possibilities * y ** 4
    
    print(sum)

def day13():
    input = readInputFile("./input/input13.txt")

    patterns = []
    lastIndex = 0
    index = 0
    for line in input:
        if line == "":
            patterns.append(input[lastIndex:index])
            lastIndex = index + 1
        index += 1
    patterns.append(input[lastIndex:])

    sum = 0
    index = 0
    for index in range(len(patterns)):
        pattern = patterns[index]
        index += 1

        lines = len(pattern)
        columns = len(pattern[0])
        
        maxLines = len(pattern)
        resultLines = None
        for i in range(lines - 1):
            linesUp = i + 1
            linesDown = maxLines - i - 1
            l = min(linesUp, linesDown)

            # valid = True
            invalidCells = 0
            for j in range(l):
                for k in range(columns):
                    if pattern[i - j][k] != pattern[i + j + 1][k]:
                        invalidCells += 1
            
            if invalidCells == 1:
                if resultLines is not None:
                    print(f"found pattern with two lines mirror - {index}")
                else:
                    resultLines = i + 1

        resultColumns = None
        for i in range(columns - 1):
            columnsLeft = i + 1
            columnsRight = columns - i - 1
            c = min(columnsLeft, columnsRight)

            invalidCells = 0
            for j in range(c):
                for k in range(lines):
                    if pattern[k][i - j] != pattern[k][i + j + 1]:
                        invalidCells += 1

            if invalidCells == 1:
                if resultLines is not None:
                    print(f"found pattern with both line and column - {index}")
                if resultColumns is not None:
                    print(f"found pattern with two columns mirror - {index}")
                else:
                    resultColumns = i + 1

        if resultColumns is not None:
            sum += resultColumns
        if resultLines is not None:
            sum += 100 * resultLines

    print(sum)

def computeLoad(m):
    sum = 0

    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == "O":
                sum += len(m) - i

    return sum

def inclineUp(input):
    for j in range(len(input)):
        whereWillStop = 0
        for i in range(len(input)):
            if input[i][j] == ".":
                continue
            elif input[i][j] == "#":
                whereWillStop = i + 1
            else: # will be O
                input[i][j] = "."
                input[whereWillStop][j] = "O"
                whereWillStop += 1

def rotateClockWise(m):
    result = []

    for j in range(len(m[0])):
        result.append([])
        for i in range(len(m) - 1, -1, -1):
            result[j].append(m[i][j])

    return result

def printMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end="")
        print("")

def day14():
    input = readInputFile("./input/input14.txt")
    m = []
    index = 0
    for line in input:
        m.append([])

        for c in line:
            m[index].append(c)
        
        index += 1
    # load 87
    # load 69
    # load 69
    # load 69
    # load 65
    # load 64
    # load 65
    # load 63
    # load 68
    # load 69
    # load 69
    # load 65
    # load 64
    # load 65
    # load 63
    # load 68
    # load 69
    # load 69
    # l 7
    # p 2
    # 
    # north, west, south, east
    # for _ in range(1000000000):
    for i in range(100000):
        # printMatrix(m)
        # print("")
        inclineUp(m) # north
        m = rotateClockWise(m)
        inclineUp(m) # west
        m = rotateClockWise(m)
        inclineUp(m) # south
        m = rotateClockWise(m)
        inclineUp(m) # east
        m = rotateClockWise(m)

        load = computeLoad(m)
        
        print(load)

    # 92, 155, 218, 281, 344 
    # ciclu l 63
    # prefix 91
        
    # 

    # for i in range(len(m)):
    #     for j in range(len(m[i])):
    #         print(m[i][j], end="")
    #     print("")

    # print("")
    # for i in range(len(m)):
    #     for j in range(len(m[i])):
    #         print(m[i][j], end="")
    #     print("")

def hash(s):
    current_value = 0

    for c in s:
        asc = ord(c)

        current_value += asc
        current_value *= 17
        current_value = current_value % 256

    return current_value

def computeFocusingPower(boxes):
    focusingPower = 0

    for key in boxes.keys():
        # print(f"box - {key}")
        box = boxes.get(key)

        for i in range(len(box)):
            lens = box[i]
            # print(f"box - {box}")
            focusingPower += (key + 1) * (i + 1) * lens[1]

    return focusingPower

def day15():
    input = readInputFile("./input/input15.txt")

    seq = []
    for line in input:
        # print(line)

        steps = line.split(",")
        for step in steps:
            seq.append(step)
    
    # print(seq)
    # print(len(seq))
    boxes = {}
    for s in seq:
        if "-" in s:
            parts = s.split("-")
            label = parts[0]

            boxIndex = hash(label)

            box = boxes.get(boxIndex)
            if box is None:
                continue
            
            found = None
            for i in range(len(box)):
                lens = box[i]
                if label == lens[0]:
                    found = i
                    break
            
            if found is not None:
                box.pop(found)
        elif "=" in s:
            parts = s.split("=")
            label = parts[0]
            focal = int(parts[1])

            boxIndex = hash(label)

            box = boxes.get(boxIndex)
            if box is None:
                boxes[boxIndex] = [[label, focal]]
                continue
            
            found = None
            for i in range(len(box)):
                lens = box[i]
                if label == lens[0]:
                    found = i
                    break
            
            if found is not None:
                box[found][1] = focal
                continue
            
            box.append([label, focal])

    print(computeFocusingPower(boxes))

def day16():
    nextMove = {
        "/": {
            "0_1": [[-1, 0]],
            "0_-1": [[1, 0]],
            "1_0": [[0, -1]],
            "-1_0": [[0, 1]]
        },
        "\\": {
            "0_1": [[1, 0]],
            "0_-1": [[-1, 0]],
            "1_0": [[0, 1]],
            "-1_0": [[0, -1]]
        },
        "|": {
            "0_1": [[-1, 0], [1, 0]],
            "0_-1": [[-1, 0], [1, 0]],
            "1_0": [[1, 0]],
            "-1_0": [[-1, 0]]
        },
        "-": {
            "0_1": [[0, 1]],
            "0_-1": [[0, -1]],
            "1_0": [[0, -1], [0, 1]],
            "-1_0": [[0, -1], [0, 1]]
        },
        ".": {
            "0_1": [[0, 1]],
            "0_-1": [[0, -1]],
            "1_0": [[1, 0]],
            "-1_0": [[-1, 0]]
        }
    }
    input = readInputFile("./input/input16.txt")

    energizedCells = {"0_0": 1}
    q = [[0, 0, 0, 1]]
    vis = {
        "0_0_0_1": 1
    }

    while len(q) > 0:
        current = q.pop(0)
        i = current[0]
        j = current[1]
        i_dir = current[2]
        j_dir = current[3]

        nm = nextMove.get(input[i][j])
        if nm is None:
            print(f"weird {i} {j} is {input[i][j]}")
            return 0

        dirKey = f"{i_dir}_{j_dir}"
        nextDirs = nm.get(dirKey)
        if nextDirs is None:
            print(f"very weird {dirKey} and {input[i][j]}")
            return 0

        for nextDir in nextDirs:
            next_i = i + nextDir[0]
            next_j = j + nextDir[1]

            if next_i < 0 or next_i >= len(input) or next_j < 0 or next_j >= len(input[0]):
                continue

            if vis.get(f"{next_i}_{next_j}_{nextDir[0]}_{nextDir[1]}") is not None:
                continue

            energizedCells[f"{next_i}_{next_j}"] = 1
            vis[f"{next_i}_{next_j}_{nextDir[0]}_{nextDir[1]}"] = 1
            q.append([next_i, next_j, nextDir[0], nextDir[1]])

    print(len(energizedCells.keys()))

day16()
