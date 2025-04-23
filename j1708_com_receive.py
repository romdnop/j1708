import serial, time, csv, sys, signal, os

from j1708.MessageWorker import MessageWorker
from j1708.Message import Message

def signal_handler(signal, handler):
    #if 'com' in globals():
    #    if com.is_open:
    #        com.close()
    print('Script interrupted!\n')
    #log_file.close()
    #if os.path.getsize(abs_file_path)==0:
    #    os.remove(abs_file_path)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)



def callback_example(msg):
    print(f"Message received from {msg.mid}")
    return


if __name__ == "__main__":
    worker = MessageWorker(callback_example)
    worker.run()