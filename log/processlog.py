class Record:
    def __init__(self, ip, time):
        self.ip   = ip
        self.time = time

fileLocation = 'access.log'
file = open(fileLocation, 'r')

for line in file:
    n=0
    if line[n] == ":":
        continue
    while not line[n] == "-":
        print(line[n], end='')
        n += 1
    print('\n')