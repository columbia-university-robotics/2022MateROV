# Columbia University Robotics Club
# MATE ROV Competition 2022
# Lexis Sablan lrs2217@columbia.edu

# Creates the GUI from which we can view a countdown, make calculations, view motor 
# and ROV status, and run our algorithms with a push of a button


import tkinter as tk
import time
import PIL
from PIL import Image, ImageTk
from tkinter import messagebox
import countdown
import biomass_calc
import drift

class Dock:
	def __init__(self, window):
		self.window = window

		self.header()

		self.motor_can()

		self.countdown()
		self.biomass()
		self.drift_calc()


		self.main_can()
		self.task_buttons()

		self.window.mainloop()

	def header(self):
		self.header_can = tk.Canvas(self.window, width = 400, height = 200)
		self.header_can.grid(column = 0, row = 0)
		self.header_img = ImageTk.PhotoImage(Image.open('header.jpg'))
		self.header_can.create_image(10, 10, image = self.header_img, anchor=tk.NW)
		

	def motor_can(self):
		self.motor_canvas = tk.Canvas(self.window, width = 100, height = 100)
		self.motor_canvas.grid(column=0, row=1)

	def main_can(self):
		self.main_canvas = tk.Canvas(self.window, width = 1000, height = 600, bg = 'white')
		self.main_canvas.grid(column = 1, row = 1, rowspan=3)

	def drift_grid(self):
		self.click_count = 0
		self.dot1x = 0
		self.dot1y = 0
		self.dot2x = 0
		self.dot2y = 0
		self.drift_img = Image.open("grid_map.png")
		self.drift_img = self.drift_img.resize((900, 500), Image.ANTIALIAS)
		self.drift_img = ImageTk.PhotoImage(self.drift_img)
		self.main_canvas.create_image(70, 30, anchor = tk.NW, image=self.drift_img)
		self.main_canvas.bind('<Button-1>', self.draw_line)


	def draw_line(self, event):
		self.click_count+=1
		if self.click_count == 1:
			self.dot1x=event.x
			self.dot1y=event.y
			self.main_canvas.create_oval(self.dot1x,self.dot1y,self.dot1x+6,self.dot1y+6, fill='black', width=10)
		elif self.click_count == 2:
			self.dot2x=event.x
			self.dot2y=event.y
			self.main_canvas.create_oval(self.dot2x,self.dot2y,self.dot2x+6,self.dot2y+6, fill='black', width=10)
			self.main_canvas.create_line(self.dot1x, self.dot1y, self.dot2x, self.dot2y, fill='black')

	def clear_can(self):
		self.main_canvas.delete('all')
		


	def task_buttons(self):
		self.but_frame = tk.Frame(self.window)
		self.but_frame.grid(column = 1, row = 0, sticky = tk.S)

		self.grid_but = tk.Button(self.but_frame, text='Grid Map', bd = '5', command = self.drift_grid)
		self.grid_but.grid(column = 0, row = 0)

		self.wreck_but = tk.Button(self.but_frame, text='Wreck Map', bd = '5')
		self.wreck_but.grid(column = 1, row = 0)

		self.mort_but = tk.Button(self.but_frame, text='Detect Morts', bd = '5')
		self.mort_but.grid(column = 2, row = 0)

		self.fish_but = tk.Button(self.but_frame, text='Measure Fish', bd = '5')
		self.fish_but.grid(column = 3, row = 0)

		self.bow_stern_but = tk.Button(self.but_frame, text='Measure Ship', bd = '5')
		self.bow_stern_but.grid(column = 4, row = 0)

		self.photomosaic_but = tk.Button(self.but_frame, text='Photomosaic', bd = '5')
		self.photomosaic_but.grid(column = 5, row = 0)

		self.clear_but = tk.Button(self.but_frame, text='Clear', bd = '5', command = self.clear_can)
		self.clear_but.grid(column = 6, row = 0)


	def biomass(self):
		self.mass_frame = tk.Frame(self.window)
		self.mass_frame.grid(column = 0, row = 1)
		biomass_calc.Biomass_calc(self.mass_frame)

	def drift_calc(self):
		self.drift_frame = tk.Frame(self.window)
		self.drift_frame.grid(column = 0, row = 2, sticky=tk.N)
		drift.Drift_Calc(self.drift_frame)

	def countdown(self):
		self.countdown_frame = tk.Frame(self.window)
		self.countdown_frame.grid(column=0, row=3, pady=10, sticky = tk.N)
		countdown.Countdown(self.countdown_frame, '15', '00')


Dock(tk.Tk())

	