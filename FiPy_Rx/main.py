from network import LoRa
import socket
import time

# LoRa Setup
# Region AU915 
# Bandwidth 125 KHz
# Spreading Factor 8
# Coding Rate 4:5
lora = LoRa(mode=LoRa.LORA, region=LoRa.AU915, bandwidth=LoRa.BW_125KHZ, sf=8, coding_rate=LoRa.CODING_4_5)
lora_sock = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
lora_sock.setblocking(True)
coding_rate = lora.coding_rate()

success = 0
errors = 0
num_package = 5357
print("LoRa Coding Rate:", coding_rate)
print(lora.stats())
for i in range(0, num_package):
    # Set TimeOut for 60 Seconds
    lora_sock.settimeout(60)
    try:
        recv_pkg = lora_sock.recv(256)
        # If something was received, its reset
        lora_sock.settimeout(None)
    except socket.timeout:
        print("Timeout reached, finish execution")
        break
    if recv_pkg == b'50':
        success = success + 1
    else:
        errors = errors + 1
    if (i%1000 == 0 and i != 0):
        print(success, " Success")
        print(errors, " Errors")
    print(i)

losses = num_package - errors - success
print(success, " Success")
print(errors, " Errors")
print(losses, " Losses")
print("Error Rate: ", ((errors + losses)/num_package)*100 ,"%")