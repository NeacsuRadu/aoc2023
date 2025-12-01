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


def main():
    task_1_2()

if __name__ == '__main__':
    main()