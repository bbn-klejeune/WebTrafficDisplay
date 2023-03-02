class Record:
    def __init__(self, ip, time):
        self.ip   = ip
        self.time = time

fileLocation = 'access.log'
log = open(fileLocation, 'r')

#For each instance in the log
for instance in log:
    #Initialize the character index of the new instance
    index      = 0
    ip_index   = 0
    date_index = 0
    ip         = ""
    date       = ""
    
    #Skips all instances that begin with a colon
    if instance[index] == ":":
        continue

    #Print every character of the IP Address until the dash is reached
    while not instance[index] == "-":
        ip       += instance[index]
        index    += 1
    print(ip, end=" -")

    GetIP(log, index, ip_index)

    #Skip the remaining delimiting dashes and spaces
    index += 5
    print(' ', end='')


    while not instance[index] == ":":
        date += instance[index]
        index += 1
    print(date, end='')
    print('\n')

def GetIP(line, start_index):
    index = start_index
    while not line[index] == ' ': 
        index += 1
        print(line[index],end='')
    