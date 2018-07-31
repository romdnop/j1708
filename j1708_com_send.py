import serial, time, signal, sys, csv, re
from j1708 import Message
from j1708 import to_dec

def signal_handler(signal, handler):
    if 'com' in globals():
        if com.is_open:
            com.close()
    print('Script interrupted!\n')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


def load_from_csv(filename):
    messages = []
    input_file = open(filename,'r')
    reader = csv.reader(input_file,delimiter=';')
    for row in reader:
        content_list = row[4]
        content_list = content_list[1:-1]
        content_list = [int(i) for i in content_list.split(',')]
        message = Message(
                int(row[0]),
                content_list,
                int(row[3]),
                int(row[1]),
                int(row[2])
                )
        messages.append(message)
    input_file.close()
    return messages


def message_send(message):
    if com.is_open:
        for item in message.content:
            com.write(chr(item))
        #com.write('\r')
        



com = serial.Serial()
com.port = "COM20"
com.baudrate = 115200

if ~com.is_open:
    com.open()       

messages = load_from_csv('messages_dump.txt')
test = messages[0].content
print test

count = 0
for item in messages:
    message_send(item)
    print item.content
    count += 1
    time.sleep(0.2)
print(count)

com.close()

