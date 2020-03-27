import serial

# Define a class
class Arduino:
    def __init__(self, serial_port, baud):
        self.port = serial_port
        self.baud = baud
        self.modules = {}
        try:
          self.serial = serial.Serial(self.port ,self.baud)
        except:
          print("Error occured while establishing connection")
    def readAll(self):
        return self.serial.read(self.serial.inWaiting())
    def configure(self, deviceName, prefix):
        self.modules[deviceName] = prefix
    def read(self, deviceName):
        data = str(self.serial.read(self.serial.inWaiting()))
        if data.startswith(self.modules[deviceName]):
          return self.serial.read(self.serial.inWaiting())
    def status(self):
        if hasattr(self, 'serial'):
          print("Serial Port: " + self.port)
          print("Listening at " + str(self.baud) + " baud")
        else:
          print("No active connections")
