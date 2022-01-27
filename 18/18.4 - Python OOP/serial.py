class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__ (self, start):
        self.init_num = start
        self.serial_num = start
        self.count = 0

    """Initializes or increments the serial number"""
    def generate(self):
        if self.count == 0:
            self.count += 1
            return self.init_num
        
        self.serial_num += 1
        return self.serial_num
    
    """Resets the serial number to start at the original number"""
    def reset(self):
        self.count = 0
        self.serial_num = self.init_num
        return
    

