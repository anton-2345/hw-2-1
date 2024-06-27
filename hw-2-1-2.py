a = []
n = []
try:
    with open('input.txt', 'r') as text_file:
        for line in text_file:
            line = line.strip()
            line = line.replace(' ', '')
            line = line.split(',')
            name, grade = line
            a.append(int(grade))
            n.append(name)
    b = sum(a)
    average = b / len(a)
    i = 0
    with open('output.txt', 'w') as txt_file:
        while i < len(a):
            if int(a[i]) > int(average):
                txt_file.write(n[i] + ',' + str(a[i]))
            i = i+1
except FileNotFoundError:
    print('This file does not exist, please come back later')