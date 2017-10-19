class Pin11:					# Class setup
	import time				# Need this for any sleep commands


	def cancel(self):			# Defining a function to run when program is aborted by user. Both on and off functions
		import RPi.GPIO as IO		# Need this to use the GPIO functions

		print("Terminated by user")	# can be cancelled so this saves me writing it twice
		IO.cleanup()				# Runs to reset the GPIO pins. Good practive to use on code completion
		print("Cleanup completed")	# Gives me feedback that the cleanup ran as this prints afterwards


	def on(self):				# Defining an LED on function
		import RPi.GPIO as IO		# This needs to be imported into every function if I wish to address it as IO

		IO.setmode(IO.BOARD)		# Setting the pin numbering convention. Altrernative is (IO.BCM)
        	IO.setup(11,IO.OUT)		# Setting pin 11 as an output

		try:				# By running the code in a try loop I can execute my pin cleanup if the user quits
			print("LED on")
			IO.output(11,IO.HIGH)	# Sets pin 11 to on (3.3v in this case)

		except KeyboardInterrupt:	# The except loop will attetmpt to run if the try loop fails and the named exception is
			cancel()		# what broke it. In this case KeyboardInterrupt is equal to ctrl - c. Otherwise this
						# would be skipped too. This function is too quick for this too happen so this code is
						# mostly wasted

	def off(self):				# Defining an LED off function
		import RPi.GPIO as IO		# If I did this for the whole class then it would become Pin11.IO
		IO.setmode(IO.BOARD)		# These need to be defined for each function or it won't work. You learnt this the hard
		IO.setup(11,IO.OUT)		# way
		try:
			print("LED off")
			IO.output(11,IO.LOW)	# Sets pin 11 to off
			IO.cleanup()

		except KeyboardInterrupt:
			cancel()

Pin11 = Pin11()					# The class is merely a template until assigned to an object. In this case the object
						# "Pin11" is the same name as the class "Pin11()"


Pin11.on()
Pin11.time.sleep(5)
Pin11.off()
