from network import LoRa
import socket
import time

# LoRa Setup
# Region AU915 
# Bandwidth 125 KHz
# Spreading Factor 8
# Coding Rate 4:5
lora = LoRa(mode=LoRa.LORA, region=LoRa.AU915, bandwidth=LoRa.BW_125KHZ, sf=8, coding_rate=LoRa.CODING_4_5)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(True)

# Define message to send
mensaje = "50"

for i in range(0, 250):
    try:
        # Send the message
        s.send(mensaje)
        print("Message Send:", mensaje)
        if i % 3 == 0:
            time.sleep(1)
    except Exception as e:
        print("Error sendind message: ", e)