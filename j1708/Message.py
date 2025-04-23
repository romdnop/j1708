import json, os

class Message():
    def __init__(self, array=None, pos=0):
        if array == None:
            #self.__init__(0,0,0,0,3)
            return
        elif not isinstance(array, (bytes, bytearray)) or len(array) < 3:
            raise ValueError("Message cannot be shorter then 3 bytes. Reffer to https://kvaser.com/about-can/can-standards/j1708/")
        self.mid = array[0]
        self.checksum = array[-1]
        self.content = array[1:-2]
        self.raw_content = array
        self.pos = pos
        self.len = len(array)
        self.is_crc_correct = self.isChecksumCorrect()

    def getDeviceName(self):
        try:
            with open(os.path.join(os.path.dirname(__file__), "device_id_map.json"), "r") as f:
                device_id_map = json.load(f)
            return device_id_map.get(str(self.mid), "Unknown")
        except FileNotFoundError:
            return "Device ID map not found"
    
    @classmethod
    def CRC(cls, array):
        return cls(array, 0).calcChecksum()
    
    def calcChecksum(self,array = None): #requires refactoring!
        if(array == None):
            array = self.raw_content
        checksum = 0
        for x in range(0, (len(array)-1)):
            checksum += array[x]
        checksum &= 255
        checksum = 256 - checksum
        return checksum
    def isChecksumCorrect(self):
        if self.calcChecksum(self.raw_content) == self.raw_content[-1]:
            return True
        return False
    def __eq__(self,other):
        return self.content == other.content
    def __hash__(self):
        return hash(('content',str(self.content)))
    

'''
#can be converted to @classmethod
def to_dec(string):
    array = []
    n = 2
    array = [string[i:i+n] for i in range(0,len(string),n)]
    array = [int(x, 16) for x in array]
    return array
'''