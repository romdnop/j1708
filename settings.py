
CONF_SERIAL_RX_NAME = "COM9"
CONF_SERIAL_BAUDRATE = 9600
CONF_SERIAL_CHARACTERS_SPAN = 22 #number of characters between the messages

CONF_SERIAL_CHARACTERS_TIMEOUT = (1/(CONF_SERIAL_BAUDRATE))*CONF_SERIAL_CHARACTERS_SPAN #number of characters 

CONF_SERIAL_INTER_CHAR_TIMEOUT = 0.01
CONF_SERIAL_STOP_BITS = 1
CONF_SERIAL_PARITY = 0

#TX serial is used for replaying the recorded logs
CONF_SERIAL_TX_NAME = "COM3"
CONF_REPLAY_TIMEOUT = 500 #delay between the messages when replaying a log file

#number of bytes in one message
CONF_MESSAGE_LEN = 21



