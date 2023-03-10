import bluetooth
import time 
# Search for nearby Bluetooth devices
devices = bluetooth.discover_devices()

# Print the names of the nearby devices
for device in devices:
    print(device, bluetooth.lookup_name(device))


# MAC address of the Bluetooth speaker
#speaker_addr = '6C:47:60:A9:C2:B8' # JBL
speaker_addr = '50:DE:06:F2:7E:7E' # Power Beats
print(1)
# Connect to the Bluetooth speaker
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((speaker_addr, 1))
print(2)
time.sleep(10)
# Play audio on the speaker
sock.send(b'Hello, world!')

# Disconnect from the speaker
sock.close()
