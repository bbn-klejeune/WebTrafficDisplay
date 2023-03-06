#Read the log file
fileLocation = 'access.log'
log = open(fileLocation, 'r')

###############################################################################
#                                  Functions                                  #
###############################################################################
# Returns the length of an IP address in a log instance
def GetIPLength(line, start_index):
    index = start_index
    while not line[index] == ' ': 
        index += 1
        print(line[index],end='')
    return index - 1

index = 0

for line in log:
    #Skips all instances that begin with a colon
    if line[index] == ":":
        continue

    ip_end_index = GetIPLength(line, index) - 1
    line[1:ip_end_index]