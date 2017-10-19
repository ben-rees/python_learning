import RPi.GPIO as IO
import time

# Pins
led = 11
button = 7

duty = 25           # The duty percentage we'll use later

#GPIO setup
IO.setmode(IO.BOARD)    # Setting pin numbering scheme
IO.setup(led,IO.OUT)     # Setting pin 11 as a 3.3v output
IO.setup(button,IO.IN, pull_up_down=IO.PUD_UP)  # Setting pin 7 as an input
                                                # using internal pull up
                                                # resistor

# Pull up resistor note: Reads low when button pressed and high when released


# Pulse width modulation setup (LED brightness)
pwm = IO.PWM(led,60)  # First argument is for our pin number
                        # and second is for frequency (60Hz in this case)

pwm.start(25)       # Starts the LED on the duty cycle given (25%)

while True:
    try:
        if IO.input(button):
            duty = 25

        else:
            for duty in range(50):  # Cycles through 1 - 50. Numbers are doubled
                                    #later

                pwm.ChangeDutyCycle(duty*2) # Setting duty to the number counted
                                            # and then doubling it

                time.sleep(0.02)

            for duty in range(50):
                
                pwm.ChangeDutyCycle(100-(duty*2)) # Subtracting from 100 so LED
                                                  # gets dimmer from max

                time.sleep(0.02)
                            
                                                  

    except KeyboardInterrupt:
        pwm.stop()
        IO.cleanup()
        print("Cleanup complete")
