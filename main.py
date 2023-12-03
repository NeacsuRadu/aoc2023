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

day_3()