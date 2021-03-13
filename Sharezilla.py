from tkinter import *
from glob import glob
import socket, os
from tkinter import simpledialog
from tkinter.messagebox import *
from tkinter.filedialog import *
from random import choice, randint
from TkinterDnD2 import *
import tkinter as tk
from tkinter import ttk

class Main(TkinterDnD.Tk):
	def __init__(self):
		super().__init__()
		self.title('Sharezilla')
		self.geometry('700x600')
		self.config(background = "#FFFCCC")
		# self.resizable(False, False)
		menuBar = Menu(self)
		FileMenu = Menu(menuBar, tearoff = 0)
		HelpMenu = Menu(menuBar, tearoff = 0)
		FileMenu.add_command(label = "Open", command = None)
		FileMenu.add_command(label = "Exit", command = self.destroy)
		HelpMenu.add_command(label = "About ", command = None)
		menuBar.add_cascade(label = "File", menu = FileMenu)
		self.config(menu = menuBar)
		self.frame0 = Frame(self, bd = 3)
		self.frame0['bg'] = 'gray'
		self.frame0.pack(side = 'left', fill = Y)
		frame1 = Frame(self)
		frame1.place(x = 590, y = 180)
		frame2 = Frame(self)
		frame2.place(x = 380, y = 180)

		TabControl = ttk.Notebook(self.frame0)
		tab1 = ttk.Frame(TabControl)
		tab2 = ttk.Frame(TabControl)
		tab3 = ttk.Frame(TabControl)
		tab4 = ttk.Frame(TabControl)
		TabControl.add(tab1, text = "all")
		TabControl.add(tab2, text = "pictures")
		TabControl.add(tab3, text = "Music")
		TabControl.add(tab4, text = "Videos")
		TabControl.pack(fill = "both", expand = 1)

		self.All = Listbox(tab1, width = 45)
		self.All.pack(fill = Y, expand = 1)
		self.All['bg'] = "#000C18" # "#02075D"
		self.All['fg'] = "white"
		self.Pics = Listbox(tab2, bg = "#000C18", fg = "white", width = 45)
		self.Pics.pack(fill = Y, expand = 1)
		self.Aud = Listbox(tab3, bg = "#000C18", fg = "white", width = 45)
		self.Aud.pack(fill = Y, expand = 1)
		self.Vid = Listbox(tab4, bg = "#000C18", fg = "white", width = 45)
		self.Vid.pack(fill = Y, expand = 1)

		self.trans = Listbox(frame1, bg = "#000C18", fg = "white", width = 30, height = 21)
		self.trans.pack(fill = Y, expand = 1)
		self.trans.drop_target_register(DND_FILES)
		self.trans.dnd_bind('<<Drop>>', self.file_in)
		recv = Listbox(frame2, bg = "#000C18", fg = "white", width = 30, height = 21)
		recv.pack(fill = Y, expand = 1)
		self.widgets()

		for file in glob("**"):self.All.insert(END, file)
		for file in glob("*.png"):self.Pics.insert(END, file)
		for file in glob("*.jpg"):self.Pics.insert(END, file)
		for file in glob("*.bmp"):self.Pics.insert(END, file)
		for file in glob("*.gif"):self.Pics.insert(END, file)
		for file in glob("*.mp3"):self.Aud.insert(END, file)
		for file in glob("*.mp4"):self.Vid.insert(END, file)
		for file in glob('*.mkv'):self.Vid.insert(END, file)
		for file in glob("*.avi"):self.Vid.insert(END, file)
		for file in glob("*.mov"):self.Vid.insert(END, file)
		for file in glob("*.wmv"):self.Vid.insert(END, file)
		for file in glob("*.WebM"):self.Vid.insert(END, file)
		for file in glob("*.AVCHD"):self.Vid.insert(END, file)

		self.All.bind("<Double-Button>", lambda x: self.add(self.All))
		self.Pics.bind("<Double-Button>", lambda x: self.add(self.Pics))
		self.Aud.bind("<Double-Button>", lambda x : self.add(self.Aud))
		self.Vid.bind("<Double-Button>", lambda x : self.add(self.Vid))
		self.trans.bind("<Button-3>", lambda x: self.remove(self.trans))

	def file_in(self, e):
		file = self.trans.tk.splitlist(e.data)[0]
		with open(file, 'r', encoding='utf-8') as f:
			self.trans.insert(END, f)

	def add(self, lb):
		item = lb.get(ACTIVE)
		self.trans.insert(END,item)

	def remove(self, lb):
		item = lb.get(ACTIVE)
		self.trans.delete('active')

	def Open(self):
		self.file = askopenfilename()
		if self.file1 == " ":
			self.file = None
		else:
			self.trans.insert(END, self.file)
			try:
				file = open(self.file, "r")
				trans.insert(END, self.file)
				file.close()
			except FileNotFoundError:
				showinfo("Error", "Hey!, you didn't open a file!")

	def widgets(self):
		label0 = Label(self, text = 'ShareZilla, share now...', bg = '#FFFCCC', fg = "black", font = ("Helvetica", 15))
		label0.pack(padx = 5)
		quotes = ['"...friendship is never anything but sharing" ~ Elie Wiesel', '"Love only grows by sharing..."~Brian Tracy', '"If you are really thankful. what do you do? You share" ~ W. Clement Stone', '"i could really use someone elses sime today"~Richelle E. Goodrich', '"for it is in giving that we recieve"~St. Francis of Assisi']
		quote = choice(quotes)
		label1= Label(self, text = quote, bg = '#FFFCCC', fg = "black", font = ("Helvetica", 15))
		label1.pack(padx = 5)

		label2 = Label(self, text = "recieving", bg = '#FFFCCC', fg = 'black', font = ("Algerian", 9))
		label2.place(x = 440, y = 140)
		label3 = Label(self, text = 'sending', bg = '#FFFCCC', fg = 'black', font = ("Algerian", 9))
		label3.place(x = 660, y= 140)

if __name__=='__main__':
	Main().mainloop()
