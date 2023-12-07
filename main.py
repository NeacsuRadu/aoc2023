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

day_7()