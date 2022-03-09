# Columbia University Robotics Club
# MATE-ROV Competition
# Lexis Sablan lrs2217@columbia.edu

# Uses tkinter GUI builder to create a countdown given a number of mintues and seconds
# uncomment the three lines at the end of the file to run the program

import time
import tkinter as tk
from tkinter import messagebox


class Countdown:

	# container - the tkinter widget (ie. canvas, frame, window) on which to display the countdown
	# minutes - String less than 60
	# seconds - string less than 60
	def __init__(self, container, minutes, seconds):

		self.container = container
		self.minutes = minutes
		self.seconds = seconds

		# StringVar enables the string to be constantly updated
		self.minute_strVar=tk.StringVar()
		self.second_strVar=tk.StringVar()


		self.minute_strVar.set(minutes)
		self.second_strVar.set(seconds)

		# create minute and seconds label and push them to the container
		self.mins_label= tk.Label(self.container, textvariable=self.minute_strVar)
		self.mins_label.config(font=('Courier', 50))
		self.mins_label.grid(column=0, row = 0, sticky=tk.E)

		self.sec_label = tk.Label(self.container, textvariable=self.second_strVar)
		self.sec_label.config(font=('Courier', 50))
		self.sec_label.grid(row = 0, column = 1, sticky=tk.W)

		# start button that runs the startCountdown method 
		self.start_btn = tk.Button(self.container, text='START', bd='5', command= self.startCountdown)
		self.start_btn.grid(column = 0, row = 1, columnspan=2)


	def startCountdown(self):

		# convert the strings to ints in seconds
		count = int(self.minutes)*60 + int(self.seconds)

		while count >-1:
			mins,secs = divmod(count,60) 

			self.minute_strVar.set("{0:2d}".format(mins))
			self.second_strVar.set("{0:2d}".format(secs))

			#constantly update container
			self.container.update()
			#wait one second before decrementing again
			time.sleep(1)

		
			if (count == 0):
				messagebox.showinfo("", "Time's Up")
			

			count -= 1


#root = tk.Tk()
#Countdown(root, '01', '00')
#root.mainloop()

	