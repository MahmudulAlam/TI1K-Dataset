file_name = 'Participant 01.txt'

f = open('../Annotation/Evaluation/' + file_name, 'r')
lines = f.readlines()
f.close()

for line in lines:
    line = line.strip().split()
    name = line[0]

    xt = float(line[1])
    yt = float(line[2])
    xi = float(line[3])
    yi = float(line[4])
    new_line = '{0} {1:.7f} {2:.7f} {3:.7f} {4:.7f}\n'.format(name, xt, yt, xi, yi)
    print(new_line)

    with open(file_name, 'a+') as f:
        f.write(new_line)
