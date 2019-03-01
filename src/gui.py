import tkinter as tk
from glitcher import Glitcher
from tkinter import filedialog


class GUI(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.filepath = ""
		self.glitcher = Glitcher()
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		self.pathField = tk.Text(height=1)
		self.pathField.grid(columnspan=2, row=0)
		self.selectButton = tk.Button(text="Choose file", command=self.choose_image)
		self.selectButton.grid(row=1, sticky=tk.N+tk.E+tk.S+tk.W)
		self.okButton = tk.Button(text="Glitch dat shit!", command=self.glitch_image)
		self.okButton.grid(column=1, row=1, sticky=tk.N+tk.E+tk.S+tk.W)

	def choose_image(self):
		self.filepath = filedialog.askopenfilename()
		self.pathField.insert(tk.INSERT,self.filepath)

	def glitch_image(self):
		if self.filepath and self.filepath != "":
			Glitcher.glitch(self.glitcher, self.filepath)
