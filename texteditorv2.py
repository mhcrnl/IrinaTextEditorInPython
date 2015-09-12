from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def file_new():
    print("New")

def save(self):
    print('Save')

def save_as():
    print('hi')

def file_open(): #this is how i get the .txt file
    fileo = filedialog.askopenfilename(filetypes=('Text files', '*.txt'))
    with open(fileo, 'r') as infile:
        data = infile.read()

def dummy():
    print("I'm a dummy :)")

def copyright():
    messagebox.showinfo('Copyright', 'This product belongs to Roemer Inc.')

class RoomEditor(Text, object):

    def __init__(self, master, **options):
        Text.__init__(self, master, **options)

        self.config(
            insertbackground="white",
            selectforeground="#00FF08",
            selectbackground="#00F000",
            font="{Courier} 14",
            foreground="#00C907",
            background="black",
            borderwidth=0,
            wrap=WORD,
            undo=True,
            width=64,
            )



root = Tk()
root.config(background="black")
root.title("Roemer's Notepad")

root.wm_state("zoomed")

editor = RoomEditor(root)
editor.pack(fill=Y, expand=1, pady=10)

editor.focus_set()

# Tkinter puts menus at the top by default
menu = Menu(root, bg='#00C907')
root.config(menu=menu)

subMenu = Menu(menu, tearoff=0)
# Adds a drop down when "File" is clicked
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New...", command=file_new)
subMenu.add_cascade(label="Save", command=save)
subMenu.add_cascade(label="Save As", command=save_as)
subMenu.add_cascade(label="Open", command=file_open)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.quit)

editMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Copy", command=dummy)
editMenu.add_command(label="Paste", command=dummy)
editMenu.add_separator()
editMenu.add_command(label="Copyright", command=copyright)

viewMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="View", menu=viewMenu)
viewMenu.add_command(label="Toolbar", command=dummy)
viewMenu.add_command(label="Status bar", command=dummy)
navigateMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Navigate", menu=navigateMenu)
navigateMenu.add_command(label="File", command=dummy)
windowMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Window", menu=windowMenu)
windowMenu.add_command(label="Font Colour", command=dummy)
windowMenu.add_command(label="Font Size", command=dummy)
helpMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About", command=dummy)
mainloop()
