from digi.xbee.devices import XBeeDevice

# Serial port for XBee receiver
XBEE_PORT = '/dev/ttyUSB0'
XBEE_BAUD_RATE = 9600

# Initialize XBee device
xbee = XBeeDevice(XBEE_PORT, XBEE_BAUD_RATE)
xbee.open()

def data_receive_callback(xbee_message):
    print(f"Received: {xbee_message.data.decode('ascii', errors='replace').strip()}")

# Add the callback
xbee.add_data_received_callback(data_receive_callback)

print("Waiting for data...")

try:
    while True:
        pass  # Keep the script running
except KeyboardInterrupt:
    print("Terminated by user")
finally:
    if xbee is not None and xbee.is_open():
        xbee.close()
