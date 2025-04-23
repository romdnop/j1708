import serial, time
from .Message import Message
from .settings import *

class MessageWorker():

    #Expects a callback function external to this class.
    #The callback function receieves Message object as an argument
    def __init__(self, callback):
        self.com = serial.Serial()
        self.com.port = CONF_SERIAL_RX_NAME
        self.com.baudrate = CONF_SERIAL_BAUDRATE
        self.com.timeout= CONF_SERIAL_CHARACTERS_TIMEOUT
        self.com.STOPBITS = CONF_SERIAL_STOP_BITS
        self.com.PARITIES = CONF_SERIAL_PARITY
        self.com.set_buffer_size = CONF_MESSAGE_LEN
        self.com.interCharTimeout = CONF_SERIAL_INTER_CHAR_TIMEOUT
        self.callbackFcn = callback
        return
    
    def createLog(self,logFilePath):
        return
    
    #run() is expected to be run inside __main__, or a thread
    def run(self):
        #function to be executed in a thread
        if ~self.com.is_open:
            self.com.open()
        print(f"Awaiting messages on {self.com.port}...")
        while True:
            if self.com.inWaiting():
                time.sleep(0.001) #0.005
                data = bytes(self.com.readline())
                print(data)
                self.dataHandler(data)
        return
    
    #Processes the data package and returns Message object
    def dataHandler(self, data):
        msg = Message(data)
        #example of data manipulation internally
        test_data(data)
        print(f"MID: {msg.mid} Content: {msg.content} CRC: {msg.checksum} Status: {msg.is_crc_correct}")
        return self.callbackFcn(msg)
    
    def __del__(self):
        if self.com.is_open:
            print(f"Closing serial port {self.com.port}...")
            self.com.close()
        return
    


def test_data(data):
    timestamp = time.strftime("%d/%m %H:%M:%S",time.gmtime())
    #data = [ord(i) for i in data]
    check = Message.CRC(data)
    log_string = timestamp +' SUM: '+str(check)+'  \t'+ str(data)
    if check == data[-1]:
        log_string = 'STATUS_OK ' + log_string
    else:
        log_string = 'WRONG_SUM! ' + log_string
    #data = ord(data)
    #log_file.write(log_string+'\n')
    print(log_string)
    parse_for_fuel(data)


def parse_for_fuel(array):
    if array[0] == 128:
        for i in range(0,(len(array)-1)):
            if (array[i] == 133): #avarage fuel rate L/s
                step = 16.428E-6
                dataH = array[i+1]
                dataL = array[i+2]
                data = (dataH<<8)|dataL
                print("Current fuel rate: ="+str(data)+"\n")
                break;       
