class Digit:
    
    def __init__(self, value=0):
        self.value = value

    def set_value(self, val):
        self.value = val

    def get_value(self):
        return self.value

    def to_octal(self):
        return oct(self.value)

    def to_hex(self):
        return hex(self.value)

    def to_binary(self):
        return bin(self.value)
