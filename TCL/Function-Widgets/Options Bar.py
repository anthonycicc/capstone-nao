from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Top Menu")

def hello():
    print("hello!")

menubar = Menu(root)

# create the file menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create the edit menu
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

#create the Run menu
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Compile", command=hello)
editmenu.add_command(label="Run", command=hello)
editmenu.add_command(label="Debug", command=hello)
menubar.add_cascade(label="Run", menu=editmenu)

#Create the help menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
root.config(menu=menubar)
root.mainloop()