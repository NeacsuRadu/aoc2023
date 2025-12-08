from functools import reduce
from re import A
from turtle import left

def readInputFile(path):
    result = []
    with open(path, 'r') as f:
        for line in f:
            if line[len(line) - 1] == '\n':
                result.append(line[0: -1])
            else:
                result.append(line)
    return result

def readInputFileToMatrix(path):
    input = readInputFile(path)

    result = []

    i = 0
    for line in input:
        result.append([])

        for c in line:
            result[i].append(c)
        
        i += 1
    
    return result

def task_1_1():
    input = readInputFile("./input/input_1_1.txt")

    # test input
    # input = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

    current = 50
    zero_counter = 0

    for line in input:
        direction = line[0]
        steps = int(line[1:])

        current = (current + steps if direction == "R" else current - steps) % 100
        if current == 0:
            zero_counter += 1

    print(zero_counter)

def task_1_2():
    input = readInputFile("./input/input_1_2.txt")

    # test input
    # input = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

    current = 50
    zero_counter = 0

    for line in input:
        direction = line[0]
        steps = int(line[1:])

        # print(f'current: {current}, direction: {direction}, steps: {steps}, zero_counter: {zero_counter}')

        # new_current = current + steps if direction == "R" else current - steps
        # if new_current <= 0 or new_current >= 100:
        #     zero_counter += abs(new_current // 100)
        #     if new_current == 0:
        #         zero_counter += 1
        
        # if current == 0 and direction == "L":
        #     zero_counter -= 1

        # current = new_current % 100
        for _ in range(steps):
            current = (current + 1 if direction == "R" else current - 1) % 100
            if current == 0:
                zero_counter += 1

    print(zero_counter) # 5899 (5791 on the faster solution, not sure why yet)

def task_2_1():
    input = readInputFile("./input/input_2_1.txt")[0]

    # test input
    # input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

    sum_of_invalids = 0
    for r in input.split(","):
        [first, second] = r.split("-")

        for n in range(int(first), int(second) + 1):
            s = str(n)
            # print(s)
            if len(s) % 2 == 1:
                continue

            is_invalid = True
            for i in range(0, len(s) // 2):
                if s[i] != s[i + len(s) // 2]:
                    is_invalid = False
                    break
            
            if is_invalid is True:
                sum_of_invalids += n

    print(sum_of_invalids)

def task_2_2_is_invalid(p):
    # print(f'doing {p}')
    for l in range(1, len(p) // 2 + 1):
        # print(f'l is {l}')
        if len(p) % l != 0:
            continue
            
        d = len(p) // l
        # print(f'd is {d}')

        is_invalid = True
        for i in range(l):
            for j in range(1, d):
                if p[i] != p[i + j * l]:
                    is_invalid = False
                    break
            
            if is_invalid is False:
                break
                
        if is_invalid is False:
            continue
    
        return True

    return False   

def task_2_2():
    input = readInputFile("./input/input_2_1.txt")[0]

    # test input
    # input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

    sum_of_invalids = 0
    for r in input.split(","):
        [first, second] = r.split("-")

        for n in range(int(first), int(second) + 1):
            s = str(n)

            if task_2_2_is_invalid(s):
                # print(n)
                sum_of_invalids += n

    print(sum_of_invalids)

def task_3_1_find_leftmost_max(s, start, end):
    max_digit = int(s[end])
    max_digit_position = end

    for i in range(end - 1, start - 1, -1):
        if int(s[i]) >= max_digit:
            max_digit = int(s[i])
            max_digit_position = i
    
    return [max_digit, max_digit_position]

def task_3_resolve(input, number_of_batteries):
    s = 0
    for line in input:

        position = 0
        digits = []
        for battery in range(number_of_batteries, 0, -1):
            [max_digit, max_position] = task_3_1_find_leftmost_max(line, position, len(line) - battery)

            position = max_position + 1
            digits.append(max_digit)

        n = 0
        for digit in digits:
            n = n * 10 + digit
        
        s+= n
    
    return s

def task_3_1():
    input = readInputFile("./input/input_3.txt")
    # test input
    # input = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]

    s = task_3_resolve(input, 2)

    print(s)

def task_3_2():
    input = readInputFile("./input/input_3.txt")

    s = task_3_resolve(input, 12)

    print(s)

def task_4_can_access_paper_roll(input, i, j):
    positions = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
    max_adjacent_rolls = 4

    adjacent_rolls = 0

    input_len = len(input)
    line_len = len(input[i])
    adjacent_rolls = 0
    for position in positions:
        if i + position[0] < 0 or i + position[0] >= input_len or j + position[1] < 0 or j + position[1] >= line_len:
            continue

        if input[i + position[0]][j + position[1]] == '@':
            adjacent_rolls += 1
    
    return adjacent_rolls < max_adjacent_rolls

def task_4_remove_paper_roll(input, i, j):
    input[i][j] = "."

    positions = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]

    input_len = len(input)
    line_len = len(input[i])
    rolls_to_be_removed = []
    for position in positions:
        if i + position[0] < 0 or i + position[0] >= input_len or j + position[1] < 0 or j + position[1] >= line_len:
            continue

        if task_4_can_access_paper_roll(input, i + position[0], j + position[1]):
            rolls_to_be_removed.append([i + position[0], j + position[1]])
    
    return rolls_to_be_removed

def task_4_1():
    input = readInputFile("./input/input_4.txt")

    number_of_rolls = 0

    input_len = len(input)
    for i in range(input_len):
        line_len = len(input[i])
        for j in range(line_len):
            if input[i][j] != '@':
                continue
            
            if task_4_can_access_paper_roll(input, i, j):
                number_of_rolls += 1

    print(number_of_rolls)

def task_4_2():
    input = readInputFileToMatrix("./input/input_4.txt")

    rolls_to_be_removed = []
    input_len = len(input)
    for i in range(input_len):
        line_len = len(input[i])
        for j in range(line_len):
            if input[i][j] != '@':
                continue
            
            if task_4_can_access_paper_roll(input, i, j):
                rolls_to_be_removed.append([i, j])

    number_of_rolls = 0

    while rolls_to_be_removed:
        [i, j] = rolls_to_be_removed.pop(0)
        if input[i][j] != "@":
            continue

        number_of_rolls += 1

        other_rolls_to_be_removed = task_4_remove_paper_roll(input, i, j)

        rolls_to_be_removed.extend(other_rolls_to_be_removed)

    print(number_of_rolls)

def task_5_1():
    input = readInputFile("./input/input_5.txt")

    read_available_items = False
    fresh_items = 0
    ranges = []
    for line in input:
        if line == '':
            read_available_items = True
            continue
    
        if read_available_items:
            item = int(line)

            is_fresh = False
            for r in ranges:
                if item >= r[0] and item <= r[1]:
                    is_fresh = True
                    break
            
            if is_fresh:
                fresh_items += 1
            
            continue
            
        aux = line.split('-')
        left = int(aux[0])
        right = int(aux[1])

        ranges.append([left, right])
    
    print(fresh_items)

def task_5_2():
    input = readInputFile("./input/input_5.txt")

    fresh_items = 0
    ranges = []
    for line in input:
        if line == '':
            break
    
        aux = line.split('-')
        left = int(aux[0])
        right = int(aux[1])

        ranges.append([left, right])

    ranges.sort(key = lambda r: r[0])

    leftmost_left = ranges[0][0]
    rightmost_right = ranges[0][1]
    fresh_items += rightmost_right - leftmost_left + 1
    for i in range(1, len(ranges)):
        r = ranges[i]

        if r[0] > rightmost_right:
            leftmost_left = r[0]
            rightmost_right = r[1]
            fresh_items += rightmost_right - leftmost_left + 1
            continue
            
        if r[0] == rightmost_right:
            fresh_items += r[1] - rightmost_right
            rightmost_right = r[1]
            continue

        if r[1] <= rightmost_right:
            continue

        fresh_items += r[1] - rightmost_right
        rightmost_right = r[1]
    
    print(fresh_items)

def task_6_1():
    input = readInputFile('./input/input_6.txt')

    result = 0
    series = []
    for line in input:
        if line.find('*') != -1 or line.find('+') != -1:
            operators = line.split()

            for i in range(len(operators)):
                add = lambda x, y: x + y
                multiply = lambda x, y: x * y

                operation = add if operators[i] == '+' else multiply

                aux = reduce(operation, series[i])
                # print(aux)
                result += aux
            continue

        numbers = list(map(lambda n: int(n), line.split()))
        for i in range(len(numbers)):
            if i >= len(series):
                series.append([])
            
            series[i].append(numbers[i])
    
    print(result)

def task_6_2():
    input = readInputFile('./input/input_6.txt')

    result = 0
    better_input = []
    for line in input:
        better_input.append(line)
    
    length = len(better_input[0])
    number_of_operands = len(better_input) - 1

    p = length - 1
    series = []
    while p >= 0:
        n = 0

        for j in range(number_of_operands):
            c = better_input[j][p]
            if c == ' ':
                continue

            n = n * 10 + int(c)
        
        series.append(n)

        if better_input[number_of_operands][p] == '*' or better_input[number_of_operands][p] == '+':
            add = lambda x, y: x + y
            multiply = lambda x, y: x * y

            op = add if better_input[number_of_operands][p] == '+' else multiply
            res = reduce(op, series)
            result += res

            p -= 2
            series = []
        else:
            p -= 1
    
    print(result)

def task_7_1_insert_if_not_exists(beams, x, y):
    found = False
    for beam in beams:
        if beam[0] == x and beam[1] == y:
            found = True
            break
    
    if not found:
        beams.append([x, y])

def task_7_1():
    input = readInputFileToMatrix('./input/input_7.txt')

    start_character = 'S'
    splitter_character = '^'

    start_i = 0
    start_j = None
    for j in range(len(input[0])):
        if input[0][j] == start_character:
            start_j = j
    
    beams = [[start_i + 1, start_j]]
    splits = 0

    while beams:
        beam = beams.pop(0)
        # print(beam)
        if beam[0] + 1 >= len(input):
            continue

        if input[beam[0] + 1][beam[1]] != splitter_character:
            task_7_1_insert_if_not_exists(beams, beam[0] + 1, beam[1])
            continue
        
        splits += 1

        if beam[1] - 1 >= 0:
            task_7_1_insert_if_not_exists(beams, beam[0] + 1, beam[1] - 1)
        
        if beam[1] + 1 < len(input[beam[0] + 1]):
            task_7_1_insert_if_not_exists(beams, beam[0] + 1, beam[1] + 1)
    
    print(splits)

task_7_2_mem = {}

def task_7_2_solve(input, x, y):
    if task_7_2_mem.get(f'{x}-{y}') is not None:
        return task_7_2_mem.get(f'{x}-{y}')

    if x == len(input) - 1:
        return 1
    
    if input[x + 1][y] == '.':
        down = task_7_2_solve(input, x + 1, y)
        task_7_2_mem[f'{x}-{y}'] = down
        return down
    
    left = 0 if y == 0 else task_7_2_solve(input, x + 1, y - 1)
    right = 0 if y == len(input[x + 1]) - 1 else task_7_2_solve(input, x + 1, y + 1)

    task_7_2_mem[f'{x}-{y}'] = left + right
    return left + right

def task_7_2():
    input = readInputFileToMatrix('./input/input_7.txt')

    start_character = 'S'

    start_i = 0
    start_j = None
    for j in range(len(input[0])):
        if input[0][j] == start_character:
            start_j = j
    
    timelines = task_7_2_solve(input, start_i + 1, start_j)
    
    print(timelines)

def task_8_1():
    input = readInputFile('./input/input_8.txt')
    iterations = 1000

    points = []
    for line in input:
        aux = line.split(',')

        points.append([int(aux[0]), int(aux[1]), int(aux[2])])
    
    edges = []
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            edges.append([points[i], points[j]])
    
    distance_fnc = lambda x: (x[1][0] - x[0][0]) * (x[1][0] - x[0][0]) + (x[1][1] - x[0][1]) * (x[1][1] - x[0][1]) + (x[1][2] - x[0][2]) * (x[1][2] - x[0][2])

    edges.sort(key=distance_fnc)

    components = []

    for i in range(iterations):
        edge = edges[i]

        left_found = -1
        right_found = -1
        for j in range(len(components)):
            component = components[j]
            for point in component:

                if point[0] == edge[0][0] and point[1] == edge[0][1] and point[2] == edge[0][2]:
                    left_found = j
            
                if point[0] == edge[1][0] and point[1] == edge[1][1] and point[2] == edge[1][2]:
                    right_found = j
            
            if left_found >= 0 and right_found >= 0:
                break
        
        if left_found == -1 and right_found == -1:
            components.append([edge[0], edge[1]])
            continue
            
        if left_found >= 0 and right_found == -1:
            components[left_found].append(edge[1])
            continue
        
        if right_found >= 0 and left_found == -1:
            components[right_found].append(edge[0])
            continue
        
        if left_found == right_found:
            continue
        
        components[left_found].extend(components[right_found])
        components.pop(right_found)
    
    sizes = list(map(lambda c: len(c), components))
    sizes.sort(reverse=True)

    print(sizes[0] * sizes[1] * sizes[2])

def task_8_2():
    input = readInputFile('./input/input_8.txt')

    points = []
    for line in input:
        aux = line.split(',')

        points.append([int(aux[0]), int(aux[1]), int(aux[2])])
    
    edges = []
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            edges.append([points[i], points[j]])
    
    distance_fnc = lambda x: (x[1][0] - x[0][0]) * (x[1][0] - x[0][0]) + (x[1][1] - x[0][1]) * (x[1][1] - x[0][1]) + (x[1][2] - x[0][2]) * (x[1][2] - x[0][2])

    edges.sort(key=distance_fnc)

    components = []

    i = -1
    last_edge = None
    while True:
        if len(components) == 1 and len(components[0]) == len(points):
            break
        i += 1
        edge = edges[i]
        last_edge = edge

        left_found = -1
        right_found = -1
        for j in range(len(components)):
            component = components[j]
            for point in component:

                if point[0] == edge[0][0] and point[1] == edge[0][1] and point[2] == edge[0][2]:
                    left_found = j
            
                if point[0] == edge[1][0] and point[1] == edge[1][1] and point[2] == edge[1][2]:
                    right_found = j
            
            if left_found >= 0 and right_found >= 0:
                break
        
        if left_found == -1 and right_found == -1:
            components.append([edge[0], edge[1]])
            continue
            
        if left_found >= 0 and right_found == -1:
            components[left_found].append(edge[1])
            continue
        
        if right_found >= 0 and left_found == -1:
            components[right_found].append(edge[0])
            continue
        
        if left_found == right_found:
            continue
        
        components[left_found].extend(components[right_found])
        components.pop(right_found)
    
    sizes = list(map(lambda c: len(c), components))
    sizes.sort(reverse=True)

    print(last_edge[0][0] * last_edge[1][0])

def main():
    task_8_2()

if __name__ == '__main__':
    main()