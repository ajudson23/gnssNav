from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice, XBee64BitAddress
import serial

# Serial port for GNSS receiver
GNSS_SERIAL_PORT = '/dev/ttyUSB0'
GNSS_BAUD_RATE = 9600
# Serial port for XBee transmitter
XBEE_PORT = '/dev/ttyUSB1'
XBEE_BAUD_RATE = 9600
# Remote XBee address (SH + SL of the receiving XBee)
REMOTE_XBEE_ADDRESS = "0013A20040XXXXXX"  # Replace with your receiver's SH + SL

# Initialize GNSS serial
gnss_serial = serial.Serial(GNSS_SERIAL_PORT, GNSS_BAUD_RATE)

# Initialize XBee device
xbee = XBeeDevice(XBEE_PORT, XBEE_BAUD_RATE)
xbee.open()

# Initialize remote XBee device
remote_xbee = RemoteXBeeDevice(xbee, XBee64BitAddress.from_hex_string(REMOTE_XBEE_ADDRESS))

try:
    while True:
        if gnss_serial.in_waiting > 0:
            nmea_sentence = gnss_serial.readline().decode('ascii', errors='replace')
            print(f"Sending: {nmea_sentence.strip()}")
            xbee.send_data(remote_xbee, nmea_sentence)
except KeyboardInterrupt:
    print("Terminated by user")
finally:
    if xbee is not None and xbee.is_open():
        xbee.close()
    gnss_serial.close()
