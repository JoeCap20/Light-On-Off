#Created by Joseph Capuiso

import sys

switchCommand='{"system": {"set_relay_state": {"state": 0}}}' #command to turn the light off
#switchCommand='{"system": {"set_relay_state": {"state": 1}}}' #command to turn the light on

OffOnBytes = switchCommand.encode() #encode function applied to the command
commandLength = [00,00,00,45] #array to hold all the hex

ivNumber = 171 #iv value we use to XOR
for x in OffOnBytes: 
    ivNumber = x ^ ivNumber     #passing all the hex values in and applying the XOR      
    commandLength.append(ivNumber) # appemd all the XORed values to the array

stored = [] 
stored = bytearray(commandLength) #turn the hex array into bytes to pass through when file is run

sys.stdout.buffer.write(stored) #system command to pass the light on/off command

