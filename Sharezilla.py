from tkinter import *
from glob import glob
import socket, os
from transfer import Transfer
from tkinter import simpledialog
from recieve import Recieve
from tkinter.messagebox import *
from tkinter.filedialog import *
from random import choice, randint
from TkinterDnD2 import *
import tkinter as tk
from tkinter import ttk

root = TkinterDnD.Tk()

class Sharezilla:
    menuBar = Menu(root)
    FileMenu = Menu(menuBar, tearoff = 0)
    HelpMenu = Menu(menuBar, tearoff = 0)
    def __init__(self):
        global trans, recv
        self.root = root
        self.FileMenu.add_command(label = "Open", command = self.Open)
        self.FileMenu.add_command(label = "Exit", command = root.destroy)
        self.HelpMenu.add_command(label = "About ", command = None)        
        self.menuBar.add_cascade(label = "File", menu = self.FileMenu)
        root.config(menu = self.menuBar)
        self.widgets()
        self.frame0 = Frame(self.root, bd = 3)
        self.frame0['bg'] = 'gray'
        self.frame0.pack(side = 'left', fill = Y)
        frame1 = Frame(root)
        frame1.place(x = 590, y = 180)
        frame2 = Frame(root)
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

        trans = Listbox(frame1, bg = "#000C18", fg = "white", width = 30, height = 21)
        trans.pack(fill = Y, expand = 1)
        trans.drop_target_register(DND_FILES)
        trans.dnd_bind('<<Drop>>', self.file_in)
        recv = Listbox(frame2, bg = "#000C18", fg = "white", width = 30, height = 21)
        recv.pack(fill = Y, expand = 1)

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
        trans.bind("<Button-3>", lambda x: self.remove(trans))

    def file_in(self, e):
        file = trans.tk.splitlist(e.data)[0]
        with open(file, 'r', encoding='utf-8') as f:
            trans.insert(END, f)
            
    def add(self, lb):
        item = lb.get(ACTIVE)
        trans.insert(END,item) 
        #this place isn't working as i expected, it is giving indexes instead of the files themselves, i don't know why

    def remove(self, lb):
        item = lb.get(ACTIVE)
        trans.delete("active", item)

    def Open(self):
        self.file = askopenfilename()
        if self.file1 == " ":
            self.file = None
        else:
            trans.insert(END, self.file)
            try:
                file = open(self.file, "r")
                trans.insert(END, self.file)
                file.close()
            except FileNotFoundError:
                showinfo("Error", "Hey!, you didn't open a file!")

    def widgets(self):
        label0 = Label(self.root, text = 'ShareZilla, share now...', bg = '#FFFCCC', fg = "black", font = ("Helvetica", 15))
        label0.pack(padx = 5)
        quotes = ['"...friendship is never anything but sharing" ~ Elie Wiesel', '"Love only grows by sharing..."~Brian Tracy', '"If you are really thankful. what do you do? You share" ~ W. Clement Stone', '"i could really use someone elses sime today"~Richelle E. Goodrich', '"for it is in giving that we recieve"~St. Francis of Assisi']
        quote = choice(quotes)
        label1= Label(self.root, text = quote, bg = '#FFFCCC', fg = "black", font = ("Helvetica", 15))
        label1.pack(padx = 5)

        label2 = Label(self.root, text = "recieving", bg = '#FFFCCC', fg = 'black', font = ("Algerian", 9))
        label2.place(x = 440, y = 140)
        label3 = Label(self.root, text = 'sending', bg = '#FFFCCC', fg = 'black', font = ("Algerian", 9))
        label3.place(x = 660, y= 140)

class Btn(Button):
    def __init__(self, master, **kw):
        root.title("ShareZilla")
        root.geometry('800x650')
        root.resizable(False, False)
        root.config(background = "#FFFCCC")
        Button.__init__(self, master = master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e): self['background'] = self['activebackground']
    def on_leave(self, e): self['background'] = self.defaultBackground
            
def Send():
    compress_name = simpledialog.askstring("Input", "Enter a name for the compressed file", parent=root)
    files = trans.get(END)
    To_send = Transfer.compress(compress_name, compress_name, files)
    size = os.path.getsize(compress_name)
    Transfer.send(compress_name, size)

def _connect():
    if selected ==1:
        Recieve.init()
        Recieve.create_socket()
    elif selected == 0:
        Transfer.connect()

code = [randint(0, 9) for i in range(6)]
use_code = False

def Rad_method():
    global code
    if selected == 0:
        use_code = True
        #code = [randint(0, 9) for i in range(6)]
        #work on this region
        ##text = "waiting for connection"
        waiting = ["waiting for connection...", "waiting for connection  ...", "waiting for connection   ..."]
        #label1 = Label(pop, text = text, bg = 'blue', font = ('Helvetica', 17))
        #label1.pack()
        """
        for i in waiting:
            text = i
            sleep(2)
        """
        #end of region
            
    elif selected == 1:
        """pop1 = Tk()
        pop1.geometry('200x100')
        pop1.title('Authorisation')
        pop1.resizable(False, False)
        entry = Text(pop1, width = 20, height = 2, relief = SUNKEN, font = ("Helvetica", 16), wrap = "word", bg = "white", foreground = 'black')
        entry.pack()
        connect_ = Button(pop1, text = "Connect", font = ("Calibri", 13, 'bold'), command = None)#command is actually the _connect method below, i'll indent that properly
        connect_.pack()"""
        simpledialog.askstring("Authorisation", "Enter the Senders ID", parent = pop)

def Connect():
    global selected, pops
    pop = Tk()
    pop.geometry('300x240')
    pop.title('Connect')
    pop.resizable(False, False)
    radVar = IntVar()
    rad1 = Radiobutton(pop, text = "connect to open network as sender", variable = radVar, value = 0, command = Rad_method)
    rad1.pack()
    rad2 = Radiobutton(pop, text = "connect to open network as reciever", variable = radVar, value = 1, command =  Rad_method)
    rad2.pack()
    selected = radVar.get()
    if use_code is True:
        label = Label(pop, text = f' Your ID: {code}', bg = 'blue', font = ('Helvetica', 17))
        label.pack()

btn0 = Btn(root, text = "SEND",width = 10, height = 0, font = ('Calibri', 15, 'bold', 'italic'), bg = '#FFF44F', foreground = 'blue', activebackground = 'gold', highlightbackground = "#bce8f1", highlightthickness = 0.5, relief = RAISED, borderwidth = "2", command = Send)
btn0.place(x=280, y=560, anchor = 'nw')
btn1 = Btn(root, text = "RECIEVE", width = 10, height = 0, font = ('Calibri', 15, 'bold', 'italic'), bg = '#FFF44F', foreground = 'blue',  activebackground = 'gold', highlightbackground = "#bce8f1", highlightthickness = 0.5, relief = RAISED, borderwidth = "2", command = None)
btn1.place(x=370, y=560, anchor = 'nw')
btn2 = Btn(root, text = "Connect", width = 10, height = 0, font = ('Arial', 15, 'bold', 'italic'), bg = '#FFF44F', foreground = 'blue', activebackground = 'gold', highlightbackground = "#bce8f1", highlightthickness = 0.5, relief = RAISED, borderwidth = "2", command = Connect)
btn2.place(x = 610, y = 560)

if __name__=='__main__':
    Sharezilla()
