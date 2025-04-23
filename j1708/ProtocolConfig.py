import json

class ProtocolConfig():
    def __init__(self):

        self.baudrate = 9600
        self.characters_span = 22
        self.char_timeout = (1 / self.baudrate) * self.characters_span

        self.config = {
            "CONF_SERIAL_RX_NAME": "COM9",
            "CONF_SERIAL_BAUDRATE": self.baudrate,
            "CONF_SERIAL_CHARACTERS_SPAN": self.characters_span,
            "CONF_SERIAL_CHARACTERS_TIMEOUT": self.char_timeout,
            "CONF_SERIAL_INTER_CHAR_TIMEOUT": 0.01,
            "CONF_SERIAL_STOP_BITS": 1,
            "CONF_SERIAL_PARITY": 0,
            "CONF_SERIAL_TX_NAME": "COM3",
            "CONF_REPLAY_TIMEOUT": 500,
            "CONF_MESSAGE_LEN": 21
        }
        return
    
    def save(self, path):
        with open(path, "w") as f:
            json.dump(self.config, f, indent=4)
    
    def load(self, path):
        with open(path, "r") as f:
            self.config = json.load(f)
