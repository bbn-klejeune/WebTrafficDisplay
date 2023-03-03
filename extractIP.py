##########################################################################
#  Function GetIP: Extract the curent IP Address from the current line   #
##########################################################################

def GetIP(line, start_index):
    index = start_index
    ip    = ""

    while not line[index] == ' ':
        ip += line[index]
        index += 1
    ip += '\n'
    return ip

##########################################################################
#                                  Main                                  #
##########################################################################

# Open the server log that contains web traffic information
input = open('.\\log\\access.log', 'r')
ipList = []

#For each instance in the log
for instance in input:
    #Initialize the character index of the new instance
    index      = 0
    ip_index   = 0
    
    #Skips all instances that begin with a colon
    if instance[index] == ':':
        continue

    #Add IP Address from current line into IP List
    ipList.append(GetIP(instance, ip_index))

# Get rid of duplicate IP Addresses
ipList = list(set(ipList))

# Create the output file and write IP Addresses
output = open('.\\log\\cleanIP.txt', 'w')
output.writelines(ipList)

# Close files to finish reading and writings
input.close()
output.close()