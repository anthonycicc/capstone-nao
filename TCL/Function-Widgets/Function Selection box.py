from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Function scrollbox")

# Initialize our country "databases":
#  - the list of country codes (a subset anyway)
#  - a parallel list of country names, in the same order as the country codes
#  - a hash table mapping country code to population<
functionCodes = ('wf', 'wb', 'tr', 'tl', 'ki', 'li', 'sy')
functionNames = ('WalkForwards', 'WalkBackwards', 'TurnRight', 'TurnLeft', 'Kick', 'Lift', 'Say')
fnames = StringVar(value=functionNames)
descriptions = {'wf':'move the robot forwards', 'wb':'move the robot backwards', 'tr':'turn the robot right', 'tl':'turn the robot left','ki':'make the robot kick', 'li':'make the robot lift its arms', 'sy':'make the robot speak'}


# State variables
statusmsg = StringVar()

# Called when the selection in the listbox changes
def showDescriptions(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        code = functionCodes[idx]
        name = functionNames[idx]
        popn = descriptions[code]
        statusmsg.set("The funciton %s will %s" % (name, popn))



# Create and grid the outer content frame
c = ttk.Frame(root, padding=(3, 3, 12, 12))
c.grid(column=0, row=0, sticky=(N,W,E,S))
c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(0,weight=1)

# Create the different widgets
lbox = Listbox(c, listvariable=fnames, height=5)
scrollbar = ttk.Scrollbar(c, orient=VERTICAL, command=lbox.yview)
lbox.configure(yscrollcommand=scrollbar.set)
status = ttk.Label(c, textvariable=statusmsg, anchor=W)

# Grid all the widgets
lbox.grid(column=0, row=0, sticky=(N,S,E,W))
status.grid(column=0, row=2, columnspan=2, sticky=(W,E))
scrollbar.grid(column=2, row=0, sticky=(N,S))


# Set event bindings for when the selection in the listbox changes,
lbox.bind('<<ListboxSelect>>', showDescriptions)

# Colorize alternating lines of the listbox
for i in range(0,len(functionNames),2):
    lbox.itemconfigure(i, background='#f0f0ff')

# Set the starting state of the interface
statusmsg.set('')
lbox.selection_set(0)
showDescriptions()

root.mainloop()