import pygame
import time

# Initialize Pygame mixer
pygame.mixer.init()

# Set the Bluetooth audio device name
device_name = 'JBL Flip 4'

# Set the audio file to play
audio_file = 'sound.m4a'

# Create the Bluetooth audio device with BlueALSA
device_addr = 'bluez_sink.' + device_name.replace(' ', '_')
os.system('sudo bluealsa-aplay -d {} {} &'.format(device_addr, audio_file))

# Wait for the device to connect
time.sleep(3)

# Load the audio file
sound = pygame.mixer.Sound(audio_file)

# Play the audio file
sound.play()

# Wait for the audio to finish playing
while pygame.mixer.get_busy():
    time.sleep(1)
