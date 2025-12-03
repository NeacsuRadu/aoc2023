def readInputFile(path):
    result = []
    with open(path, 'r') as f:
        for line in f:
            if line[len(line) - 1] == '\n':
                result.append(line[0: -1])
            else:
                result.append(line)
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

def main():
    task_3_2()

if __name__ == '__main__':
    main()