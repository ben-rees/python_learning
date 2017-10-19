Some scribbles showing GPIO functions

import RPi.GPIO as GPIO
# This imports the GPIO stuff.

GPIO.setmode(GPIO.BOARD)
# This sets the bin numbering. Board is as you see, BCM is how the CPU sees.
			  
# Note below: Pin = Your pin number			  
GPIO.setup(pin,GPIO.OUT)
# Sets the pin up as an output
			  
GPIO.output(pin,GPIO.HIGH/LOW)
# HIGH = On, LOW = Off


# GPIO input will go here once I've played with it more. It's more complex than
# simply writing "IN".


GPIO.cleanup()
# Resets any pins used during the code. Good practive to finsh with.
		 
GPIO.PWM(pin,50).start(0)
# Starts Pulse Width Modulation. Used for setting LED brightness. 50 is the
# frequency in Hz. The 0 after start is the beginning brightness as a percentage.
# The brightness is called the Duty Cycle. It's the percentage of how long the LED
# is illuminated for within each cycle. e.g. 50% is on for the first half of the Hz
# and then off for the remaining.
                       
# Alternatively you could
p= GPIO.PWM(pin,50)
# Then
p.start(0)
# or
p.stop()
# Here we're assigning the bulk of the function to a single letter
# variable which makes things such as starting or stopping easier

GPIO.PWM(pin,50).ChangeDutyCycle(newBrightness)
#or
p.ChangeDutyCycle(newBrightness)
# You can probably see why I'm eager to assigned so much of this to a variable now
