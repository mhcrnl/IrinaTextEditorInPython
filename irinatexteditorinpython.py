from Tkinter import *
import tkFileDialog
import ScrolledText
import tkMessageBox

	# Acesta este un text editor - cod disponibil pe github
def main():
	
	fereastra = Tk(className= " Irina's Text Editor")
	textEditor = ScrolledText.ScrolledText(fereastra, width=100, height=80)

	# Adaugam un meniu si o functie care sa ne asigure ca aplicatia funct
	def functProvizorie():
		print "Mai tarziu voi fi stearsa"
	# Functiile care asigura functionarea aplicatiei

	def fileNew():
		textEditor.set("")
	
	def fileOpen():
		file = tkFileDialog.askopenfile(parent=fereastra, mode='rb', title='Selectati fila')
		if file != None:
			contents = file.read()
			textEditor.insert('1.0', contents)
			file.close()
		
	def fileSave():
		file = tkFileDialog.asksaveasfile(mode='w')
		if file != None:
			data = textEditor.get('1.0', END+'-1c')
			file.write(data)
			file.close()
		
	def fileExit():
		if tkMessageBox.askokcancel("Inchide", "Doriti inchidera aplicatiei?"):
			fereastra.destroy()
		
	def helpAbout():
		label = tkMessageBox.showinfo("Despre", "Acesta este un text editor") 
	
	# Adaugam un meniu si un submeniu	
	menu = Menu(fereastra)
	fereastra.config(menu=menu)
	fileMenu = Menu(menu)
	menu.add_cascade(label="File", menu=fileMenu)
	# Adaugam in continuare in File submeniurile
	fileMenu.add_command(label="New", command=main, accelerator="Ctrl+N")
	fileMenu.add_command(label="Open", command=fileOpen)
	fileMenu.add_command(label="Save", command=fileSave)
	fileMenu.add_separator()
	fileMenu.add_command(label="Exit", command=fileExit, accelerator="Ctrl+e")
	fileMenu.add_command(label="New", command=functProvizorie)
	# Adaugarea meniului Help cu submeniu
	helpMenu = Menu(menu)
	menu.add_cascade(label="Help", menu=helpMenu)
	helpMenu.add_command(label="About", command=helpAbout)

	textEditor.pack()

	fereastra.mainloop()
main()
