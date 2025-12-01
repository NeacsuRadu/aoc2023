def readInputFile(path):
    output = []
    with open(path, 'r') as file:
        for line in file:
            output.append(line)
    
    return output

def day1_1():
    lines = readInputFile('./input/input1_1.txt')

    list_a = []
    list_b = []
    for line in lines:
        tokens = line.split()
        list_a.append(int(tokens[0]))
        list_b.append(int(tokens[1]))
    
    list_a.sort()
    list_b.sort()

    diff = 0
    for i in range(0, len(list_a)):
        diff += abs(list_a[i] - list_b[i])
    
    print(diff) # 1197984

def day1_2():
    lines = readInputFile('./input/input1_1.txt')

    list_a = []
    list_b = []
    for line in lines:
        tokens = line.split()
        list_a.append(int(tokens[0]))
        list_b.append(int(tokens[1]))
    
    similarity = 0
    for i in range(0, len(list_a)):
        elem_a = list_a[i]
        count = 0
        for j in range(0, len(list_b)):
            elem_b = list_b[j]
            if elem_a == elem_b:
                count += 1
        
        similarity += elem_a * count
    
    print(similarity) # 23387399

if __name__ == '__main__':
    day1_2()