import serial, time, csv, sys, signal, os
from j1708 import Message,checksum



def signal_handler(signal, handler):
    if 'com' in globals():
        if com.is_open:
            com.close()
    print('Script interrupted!\n')
    log_file.close()
    if os.path.getsize(abs_file_path)==0:
        os.remove(abs_file_path)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def handle_data(data):
    timestamp = time.strftime("%d/%m %H:%M:%S",time.gmtime())
    data = [ord(i) for i in data]
    check = checksum(data)
    log_string = timestamp +' SUM: '+str(check)+'  \t'+ str(data)
    if check == data[-1]:
        log_string = 'STATUS_OK ' + log_string
    else:
        log_string = 'WRONG_SUM! ' + log_string
    #data = ord(data)
    log_file.write(log_string+'\n')
    print(log_string)


com = serial.Serial()
com.port = "COM21"
com.baudrate = 115200
com.timeout= (1/115200)*3 + 0.005

if ~com.is_open:
    com.open()

if not os.path.exists('logs'):
    os.makedirs('logs')

log_stamp = time.strftime("%d_%m_%H_%M_%S",time.gmtime())
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "logs/log_"+log_stamp+'.txt'
abs_file_path = os.path.join(script_dir, rel_path)
log_file = open(abs_file_path,'w')

while True:
    #print("test")
    if com.inWaiting():
        time.sleep(0.001)
        reading = com.readline()
        handle_data(reading)

#receiver's code

        



com.close()
