# First we import what we'll be using for class/object
# Time is for adding pauses/delays
# RPi.GPIO for controlling the onboard GPIO pins
# (Imported as GPIO to make referral easier later)
# randint from random to allow random number generation
# (Specifiying randint makes it easier to call)
# Threading to allow a function to run independant to the rest of the code
# Imported it here in case the code this is imported into doesn't have it
import time
import RPi.GPIO as GPIO
from random import randint
import threading

# Next I define my class to later be assigned to an object
class LED:
  
# Some basic GPIO setup. Not sure if this should be done in or out of the class.
# First we set the pin labelling
    GPIO.setmode(GPIO.BOARD)
# Next we specify our output pin
    GPIO.setup(11,GPIO.OUT)
# This disables warning messages in the console. Usually telling me a pin
# is already assigned.
    GPIO.setwarnings(False)
# Setting the Pulse Width Modulation function to the variable "p"
# 11 represents my pin, 60 is the frequency in Hz
    p = GPIO.PWM(11,60)
# Setting a variable to later break an infinite loop
    feedback = True

# Defining a function
    def blink(self):
# Sets the feedback variable back to True in case it's been left as False
# By another function. The self bit is used so python knows which object this
# function needs to reference later.
        self.feedback = True
# Running the loop in a try block allows me to define what happens if I end
# the loop with a keyboard termination
        try:
# Loop will only run as long as feeback is True
            while self.feedback == True:
# Starting Pulse Width Modulution (assigned to "p") with a duty cycle (brightness)
# at 50%
                self.p.start(50)
# Assigning a random number between one and 100 to the "i" variable
                i = randint(1,100)
# The brightness defaults to 50% if the number generated is less than 50
                if i > 50:
                    self.p.ChangeDutyCycle(50)
# If it's not less than 50 then the number (i) is assigned as the new brightness
                else:
                    self.p.ChangeDutyCycle(i)
# Giving a short delay before allowing the loop to run again
                    time.sleep(0.12)
# Once the while loop fails/ends this will run and end the PWM
            self.p.stop()

# Side note: I could have used number generation between 50 - 100 however I wanted
# moments where the LED stays at it's base brightness (50%) as it seemed like a better
# way for a LED to represent speach (the purpose of this code originally) than
# having it flicker crazily 60 times a second.

# My code that will execute upon the try loop being broken by ctrl-C (KeyboardInterrupt:)
        except KeyboardInterrupt:
# Prints a confirmation message
            print("Terminated by user")
# Stops the PWM
            self.p.stop()
# Runs the GPIO cleanup which resets any assigned pins and states
            GPIO.cleanup()
# Prints a confirmation that the cleanup ran
            print("Cleanup complete")
            
# Defining the function that stops the blinking
    def blinkStop(self):
# Setting "feedback" to False will break while loop in the blink function
        self.feedback = False
        self.p.stop()
           
# Example of code in use
           
# Assigning the class (LED()) to an object (LED)
LED = LED()
# Starts the blink function defined above now called LED.blink as it's attatched
# to an object called LED. threading.Thread.start() is what starts our thread
# With the brackets after Thread clearly setting the thread's name and the function
# that will run within it.
threading.Thread(name="blinker", target=LED.blink).start()
time.sleep(5)
LED.blinkStop()

# The reason we the blinker in a separate thread is because whilst the while loop
# is continuosly running the rest of the code won't be. It'll be waiting for it's turn.
# This makes using "if feedback == False: Continue" useless to exit the loop as nothing
# is able to run outside of the loop.
# Putting it in it's own thread allows the delay in this example to start once the
# thread has started and then allow the stop function to run and end the loop afterwards.
# Obviously thestopper doesn't always havae to be on a timer. You could have it trigger
# on a variable of it's own like blink does.