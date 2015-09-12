from Tkinter import *
from Tkinter.messagebox import *
from Tkinter.filedialog import *
from Tkinter.font import *
import sys, time, sched, math

#web: http://stackoverflow.com/questions/22848080/
#python-create-save-button-that-saves-an-edited-version-to-the-same-filenot-save

class Format:
    def __init__(self, notepad):
        print("Font")

class ZPad:
    def __init__(self):
        self.root = Tk()
        self.root.title("ZPad")
        self.root.wm_iconbitmap('Notepad.ico')

        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.textbox = Text(self.root, yscrollcommand=self.scrollbar.set, undo=TRUE)
        self.textbox.pack(side=LEFT, fill=BOTH, expand=YES)

        #Menu Bar
        self.menubar = Menu(self.root)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=self.New, accelerator="Ctrl+N")
        self.filemenu.add_command(label="Open...", command=self.open, accelerator="Ctrl+O")
        self.filemenu.add_command(label="Save", command=self.Save, accelerator="Ctrl+S")
        self.filemenu.add_command(label="Save as...", command=self.Save_as, accelerator="Ctrl+Shift+S")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.quit, accelerator="Ctrl+Q")
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Undo", command=self.Undo, accelerator="Ctrl+Z")
        self.editmenu.add_command(label="Redo", command=self.Redo, accelerator="Ctrl+Y")
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Cut", command=self.Cut, accelerator="Ctrl+X")
        self.editmenu.add_command(label="Copy", command=self.Copy, accelerator="Ctrl+C")
        self.editmenu.add_command(label="Paste", command=self.Paste, accelerator="Ctrl+P")
        self.editmenu.add_command(label="Clear All", command=self.Clear_All, accelerator="Ctrl+Shift+A")
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Format", command=self.options, accelerator="Ctrl+T")
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About...", command=self.About)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)


        self.root.config(menu=self.menubar)

        self.root.mainloop()

def Save(self):
    print("Save")

def Save_as(self):
    global file
    file = tkinter.filedialog.asksaveasfile(mode='w', defaultextension=".z", filetypes = ( ("ztext file", "*.z"),("zytext", "*.zy") ) )
    if file is None:
        return
    else:
        print(file)
    textoutput = self.textbox.get(0.0, END)
    file.write(textoutput.rstrip())
    file.write("\n")

notepad = ZPad()
