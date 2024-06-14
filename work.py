# XBee is 802.15.4 protocol --> class RemoteRaw802Device

### _____________________ TRANSMITTER.PY _____________________ ###
from digi.xbee.devices import XBeeDevice
# from digi.xbee.devices import  RemoteXBeeDevice                   # DELETE
# from digi.xbee.models.address import xBee64BitAddress             # DELETE

xbee = XBeeDevice('/dev/ttyUSB0', 9600)                             # Instantiate a local XBee node
xbee.open()
xbee.send_data_broadcast("Hello XBee World")
xbee.close()



# Instantiate a remote XBee node.                                   # DELETE    
# remote = RemoteXBeeDevice(xbee, XBee64BitAddress.from_hex_string("0013A20040XXXXXX")) # DELETE 
# Send data using the remote object.
# xbee.send_data(remote, "Hello XBee!")

### _____________________ RECEIVER.PY _____________________ ###
from digi.xbee.devices import XBeeDevice

# Instantiate a local XBee node.
xbee = XBeeDevice("COM1", 9600)
xbee.open()

# Read data.
xbee_message = xbee.read_data()