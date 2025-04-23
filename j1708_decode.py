import serial, time, re, csv
from j1708.Message import Message, checksum


def to_dec(string):
    array = []
    n = 2
    array = [string[i:i+n] for i in range(0,len(string),n)]
    array = [int(x, 16) for x in array]
    return array
'''
def checksum(array):
    checksum = 0
    for x in range(0,(len(array)-1)):
        checksum = checksum+array[x]
    checksum = checksum & 255
    return checksum
'''
def slice_on_packages(array):
    messages = []
    pStart = 0
    pEnd = 21
    lastEnd = pEnd
    while pStart < (len(array)-3):
        while (pEnd-pStart)>3:
            sub_array = array[pStart:pEnd]
            if checksum(sub_array)==sub_array[-1]:
                mess = Message(sub_array[0],
                               sub_array[0:len(sub_array)],
                               sub_array[-1],
                               pStart,
                               len(sub_array))
                #if len(sub_array)!=0:
                messages.append(mess)
                #print(sub_array)
                lastEnd = pEnd
            pEnd = pEnd - 1
        pStart = pStart + 1
        pEnd = pStart + 21
    return messages

def slice_message(messages, start, end):
    return messages[start:end]

def check_message_exist(message):
    maxPossibleLen = 21
    while maxPossibleLen > 0:
        if checksum(message) == message[-1]
            maxPossibleLen -= 1
            return True
    return False
    

def slice_on_packages2(array):
    messages = []
    pStart = 0
    pEnd = 21
    while pStart < (len(array)-3):
        mess = slice_message(array,pStart, pEnd)
        if check_message_exist(mess):
            
        
        

def compaction(messages):
    #Searching for message wich repeats more then 5 times.
    #If near this message exist other message 
    #and founded messsage contains the first element of that message
    #then delete this message
    for item in messages:
        if messages.count(item) == 1:
            ind = messages.index(item)
            del messages[ind]
    return messages


    

def find_lost_packages(messages, input_dump):
    lost_packages = []
    for item in range(0,len(messages)-1):
        startP = messages[item].pos + messages[item].length
        endP = messages[item+1].pos -1
        if startP == endP or endP < startP:
            continue
        lost = input_dump[startP:endP]
        #print startP,endP
        lost = Message(
                        lost[0],
                        lost,
                        "WRONG!",
                        startP,
                        len(lost)
                        )
        lost_packages.append(lost)
    #lost_packages = [cleanlist.append(x) for x in lost_packages if x not in cleanlist]
    return lost_packages
    

def write_in_log(log_file, data):
    writedContent = 0
    for item in range(0,len(data)):
        writedContent = writedContent+len(data[item].content)
        log_file.write("Pos: "+str(data[item].pos)+
                     " \tPosEnd: "+str(data[item].pos+data[item].length)+
                     " \tLength: "+str(data[item].length)+
                     " \tMID: "+str(data[item].mid)+" "+
                     " \tCHECKSUM: " +str(data[item].checksum)+
                     "  \tContent: " +str(data[item].content)+
                     "\n")
    return writedContent

def save_messages_to_csv(messages):
    messages_dump = open("messages_dump.txt","wb")
    writer = csv.writer(messages_dump,
                        delimiter=';',
                        quotechar='|',
                        quoting=csv.QUOTE_MINIMAL)
    for item in messages:
        writer.writerow(
            [str(item.mid)]+
            [str(item.pos)]+
            [str(item.length)]+
            [str(item.checksum)]+
            [str(item.content)]
            )
    messages_dump.close()

input_dump = open("dump_10_08.txt","r")
dump_array = input_dump.readlines()
dump_array = str(dump_array)
dump_array = re.sub('[^A-Za-z0-9]+', '', dump_array)
dump_array = to_dec(dump_array)
inputDumpLen =len(dump_array)
print("Length of input dump: "+str(inputDumpLen))
input_dump.close()

messages = slice_on_packages(dump_array)
output = open("decode.txt","w")
contentLen = 0
messages = compaction(messages)
messages.sort(key=lambda x:x.pos)
#messages = [i for i in messages if i.content[0]!=0]
#messages = [i for i in messages if i.content[0]!=255]

#write messages to file
save_messages_to_csv(messages)


#np.savetxt('messages_dump.csv',messages,delimeter=';',)


write_in_log(output, messages)
output.write("\n\n\n\t\t\t\t\t\t\t================= LOST PACKAGES =================\n\n\n")
lost_pkg = find_lost_packages(messages, dump_array)
write_in_log(output, lost_pkg)
output.close()

#messages = compaction(messages)
#lost = find_lost_packages(messages, dump_array)
#print(len(lost))
print("Length of output dump: "+str(contentLen))
print("Missed bytes total: "+ str(inputDumpLen - contentLen))


