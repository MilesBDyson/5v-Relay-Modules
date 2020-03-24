#!/usr/bin/python

'''
This File is an example on how to use a Relay module board with the Beaglebone Black
please read the Arguments and Usage section below on how to use this file.

 Arguments...
  FIRST: argument is the relay number [1-16]
   example -1 for relay 1 and so on
   example -all will cycle threw all relays
  SECOND: argument is for timing, -p or -h
   example -p to simulate a button press for 1.5 seconds
   example -h to simulate a button press and hold for 10 seconds
 Usage...
  to run the program....
  python relay.py -1 -p       <-- will cycle relay 1 for 1.5 seconds
  python relay.py -all -h     <-- will cycle threw all relays for 10 seconds
'''

# Import the needed library's
import Adafruit_BBIO.GPIO as GPIO
import sys
from time import sleep

# Relay Module Pinout
# GND = "P9_1" [Ground]
# in1 = relay 01 - [GPIO] "P8_8"
# in2 = relay 02 - [GPIO] "P8_7"
# in3 = relay 03 - [GPIO] "P8_10"
# in4 = relay 04 - [GPIO] "P8_9"
# in5 = relay 05 - [GPIO] "P8_12"
# in6 = relay 06 - [GPIO] "P8_11"
# in7 = relay 07 - [GPIO] "P8_14"
# in8 = relay 08 - [GPIO] "P8_16"
# in9 = relay 09 - [GPIO] "P8_15"
# in10 = relay 10 - [GPIO] "P8_18"
# in11 = relay 11 - [GPIO] "P9_12"
# in12 = relay 12 - [GPIO] "P9_15"
# in13 = relay 13 - [GPIO] "P9_23"
# in14 = relay 14 - [GPIO] "P9_41"
# in15 = relay 15 - [GPIO] "P9_27"
# in16 = relay 16 - [GPIO] "P9_30"
# VCC = "P9_3" [3.3v]

# external power supply
# JD-VCC == 5v external power positive
# VCC == not used
# GND == 5v external power negative


# pins used to control each of the relays
# uncomment and comment as needed depending on how many relays your module has
# relay#    1       2
#relay = ["P8_8", "P8_7"]
# relay#    1       2       3        4
#relay = ["P8_8", "P8_7", "P8_10", "P8_9"]
# relay#    1       2       3        4       5        6        7        8
#relay = ["P8_8", "P8_7", "P8_10", "P8_9", "P8_12", "P8_11", "P8_14", "P8_16"]
# relay#    1       2       3        4       5        6        7        8        9       10       11       12       13       14       15       16
relay = ["P8_8", "P8_7", "P8_10", "P8_9", "P8_12", "P8_11", "P8_14", "P8_16", "P8_15", "P8_18", "P9_12", "P9_15", "P9_23", "P9_41", "P9_27", "P9_30"]

# setup relay pins used for relays
for i in range(len(relay)):
   GPIO.setup ( relay[i], GPIO.OUT )
   GPIO.output ( relay[i], GPIO.HIGH )

# Activate spacific relay
sys.argv[1] = sys.argv[1][1:]

if sys.argv[1].isdigit():
   if sys.argv[2] == "-p": # Button press
      GPIO.output(relay[abs(int(sys.argv[1]))-1], GPIO.LOW)
      sleep(1.5)  #<--- modify this to change timing for the -p argument
      GPIO.output(relay[abs(int(sys.argv[1]))-1], GPIO.HIGH)
   if sys.argv[2] == "-h": # Button hold
      GPIO.output(relay[abs(int(sys.argv[1]))-1], GPIO.LOW)
      sleep(10)  #<--- modify this to chenge the timing for the -h argument
      GPIO.output(relay[abs(int(sys.argv[1]))-1], GPIO.HIGH)

# Cycle threw all relays
if sys.argv[1] == "all":
   if sys.argv[2] == "-h": # Button hold
      for i in range(len(relay)):
         GPIO.output(relay[i], GPIO.LOW)
         sleep(10)  #<--- modify this to chenge the timing for the -h argument
         GPIO.output(relay[i], GPIO.HIGH)
         sleep(1)
   if sys.argv[2] == "-p": # Button press
      for i in range(len(relay)):
         GPIO.output(relay[i], GPIO.LOW)
         sleep(1.5)  #<--- modify this to change timing for the -p argument
         GPIO.output(relay[i], GPIO.HIGH)
         sleep(1)
