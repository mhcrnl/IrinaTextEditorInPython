import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox
def main():
    root = Tkinter.Tk(className=" TextPad")
    textPad = ScrolledText(root, width=100, height=50)
 
    # create a menu & define functions for each menu item
 
    def open_command():
        file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
        if file != None:
            contents = file.read()
            textPad.insert('1.0',contents)
            file.close()

    def saving():
        save_command(textPad)
    def save_command(self):
        file = tkFileDialog.asksaveasfile(mode='w')
        if file != None:
        # slice off the last character from get, as an extra return is added
            data = self.get('1.0', END+'-1c')
            file.write(data)
            file.close()
         
    def exit_command():
        if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
            root.destroy()
 
    def about_command():
        label=tkMessageBox.showinfo("About", "Just Another TextPad Judical CLAIR")

    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New", command=main)
    filemenu.add_command(label="Open...", command=open_command)
    filemenu.add_command(label="Save", command=saving)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=exit_command)
    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=about_command)
    
    textPad.pack()
    root.mainloop()
main()
