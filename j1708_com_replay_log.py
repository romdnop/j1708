import serial, time, signal, sys, csv, re
from j1708 import Message
from j1708 import to_dec
from settings import *

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
        print(content_list)
        #content_list = [int(i) for i in content_list.split(',')]
        #print(content_list)
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
        print(f"MID: {message.mid} LEN: {message.length} CRC: {message.checksum} CONTENT: {message.content}")
        #print(type(message.content))

        com.write(bytes(message.content,'utf-8'))
        #com.write(b'\r')
        

if __name__ == "__main__":

    com = serial.Serial()
    com.port = CONF_SERIAL_TX_NAME
    com.baudrate = CONF_SERIAL_BAUDRATE

    if ~com.is_open:
        com.open()       

    messages = load_from_csv('messages_dump.txt')
    test = messages[0].content
    total_messages = len(messages)
    print(f"{total_messages} messages loaded.")

    print(f"Starting transmission on {com.port}...")

    #count = 0
    for ind, msg in enumerate(messages):
        print(f"Transmitting {ind+1}/{total_messages}...")
        print(list(msg.content.split(',')))
        message_send(msg)
        #count += 1
        time.sleep(0.2)
    
    print(f"All mesages has been transmitted.\rExiting...")
    #print(count)

    com.close()

