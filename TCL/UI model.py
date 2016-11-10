# Imports and preprocessor

from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

root = Tk()
root.title("Nao Programming IDE")



# Function definitions. Currently This is only a placehoder (this is what the top menu bar is currently calling)
def hello():
    print("hello!")

# Called when the selection in the listbox changes
def showDescriptions(*args):
    idxs = function_list.curselection()
    if len(idxs) == 1:
        idx = int(idxs[0])
        code = functionCodes[idx]
        name = functionNames[idx]
        popn = descriptions[code]
        functionDescription.set("The funciton %s will %s" % (name, popn))

#When a function is double clicked or ADD is selected
def addFunction(*args):
    idxs = function_list.curselection()
    if len(idxs) == 1:
        idx = int(idxs[0])
        name = functionNames[idx]
        design_list.insert(END, name)


def removeFunction(*args):
    design_list.delete(design_list.curselection())

def moveUp(*args):

    pos = design_list.curselection()

    temp = design_list.get(pos)
    design_list.delete(pos)
    design_list.insert(pos[0] - 1, str(temp))

def moveDown(*args):

    pos = design_list.curselection()
    #if pos == :
    #       return 0

    temp = design_list.get(pos)
    design_list.delete(pos)
    design_list.insert(pos[0] + 1, str(temp))

# Top level menu
# create the file menu
menubar = Menu(root)
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



#Hash table of function names
functionCodes = ('wf', 'wb', 'tr', 'tl', 'ki', 'li', 'sy')
functionNames = ('WalkForwards', 'WalkBackwards', 'TurnRight', 'TurnLeft', 'Kick', 'Lift', 'Say')
fnames = StringVar(value=functionNames)
descriptions = {'wf':'move the robot forwards', 'wb':'move the robot backwards', 'tr':'turn the robot right', 'tl':'turn the robot left','ki':'make the robot kick', 'li':'make the robot lift its arms', 'sy':'make the robot speak'}



# String variables
functionDescription = StringVar()
search = StringVar()


# Create and grid the outer content frame
c = ttk.Frame(root, padding=(3, 3, 12, 12))
c.grid(column=0, row=0, sticky=(N,W,E,S))
c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(0,weight=1)


# Create the different widgets
function_list = Listbox(c, listvariable=fnames, height=20, exportselection=1)
function_scrollbar = ttk.Scrollbar(c, orient=VERTICAL, command=function_list.yview)
function_list.configure(yscrollcommand=function_scrollbar.set)
function_desc = ttk.Label(c, textvariable=functionDescription, anchor=W, width=50)

search_entry = ttk.Entry(c, width=20, textvariable=search,)
search_button = ttk.Button(c, text="Search", command=showDescriptions())

add_button= ttk.Button(c, text="Add Function", command=addFunction)
remove_button= ttk.Button(c, text="Remove Function", command=removeFunction)
moveUp_button= ttk.Button(c, text="Move Up", command=moveUp)
moveDown_button= ttk.Button(c, text="Move down", command=moveDown)

design_list = Listbox(c, height=5, exportselection=1)


# Grid all the widgets
#Col 1
search_entry.grid(column=1, row=1)
search_button.grid(column=1, row=2)
function_list.grid(column= 1, row=3, rowspan=5 ,sticky=(N,S,E,W))
function_desc.grid(column=1, row=100, sticky=(W,E))

#Col 2
function_scrollbar.grid(column=2, row=3, rowspan = 5, sticky=(N,S))

#Col 3
design_list.grid(column=3, row=3, rowspan=5, sticky=(N,S,E,W))

#Col 4
add_button.grid(column=4, row=3)
moveUp_button.grid(column=4, row=4)
moveDown_button.grid(column=4, row=5)
remove_button.grid(column=4, row=6)



# Set event bindings for when the selection in the listbox changes,
function_list.bind('<<ListboxSelect>>', showDescriptions)
function_list.bind('<Double-1>', addFunction)


# Color alternating lines of the listbox
for i in range(0,len(functionNames),2):
    function_list.itemconfigure(i, background='#f0f0ff')


# Set the starting state of the interface
functionDescription.set('')
function_list.selection_set(0)
showDescriptions()

root.mainloop()
