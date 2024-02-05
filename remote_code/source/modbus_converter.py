import json

def to_word(integer):
    msb = (integer>>8)&0xff
    lsb = integer&0xff
    return [msb, lsb]

def to_byte(integer):
    return [integer]

class modbus_maker:
    analog_overheads = []
    digital_overheads = []

    def __init__(self):
        file = open("./settings/modbus_frame.json", "r")
        jsonF = json.load(file)

        self.analog_overheads += to_word(jsonF["analog"]["transaction id"])
        self.analog_overheads += to_word(jsonF["analog"]["protocol id"])
        self.analog_overheads += to_word(jsonF["analog"]["length"])
        self.analog_overheads += to_byte(jsonF["analog"]["device address"])
        self.analog_overheads += to_byte(jsonF["analog"]["function code"])
        self.analog_overheads += to_word(jsonF["analog"]["register"])
        self.analog_overheads += to_word(jsonF["analog"]["register count"])
        self.analog_overheads += to_byte(jsonF["analog"]["byte count"])

        self.digital_overheads += to_word(jsonF["digital"]["transaction id"])
        self.digital_overheads += to_word(jsonF["digital"]["protocol id"])
        self.digital_overheads += to_word(jsonF["digital"]["length"])
        self.digital_overheads += to_byte(jsonF["digital"]["device address"])
        self.digital_overheads += to_byte(jsonF["digital"]["function code"])
        self.digital_overheads += to_word(jsonF["digital"]["register"])
        self.digital_overheads += to_word(jsonF["digital"]["register count"])
        self.digital_overheads += to_byte(jsonF["digital"]["byte count"])
        file.close()

    def create_new(self, can_data, type):
        data = []

        for value in can_data:
            data += to_word(value)
        if(type == 104):
            return self.analog_overheads + data
        return self.digital_overheads + data

