#-*-encoding:utf8
from tkinter import *
from tkinter import filedialog
#create header
from tkinter.filedialog import askopenfilename
import logging

root=Tk()
root.title("Text Editor")
root.geometry("800x500")

#Edit Text Area
lnlabel = Label(root,width = 2,bg = 'antique white')
lnlabel.pack(side = LEFT,fill = Y)

textpad = Text(root,undo = True)
textpad.pack(expand = YES,fill = BOTH)

scroll = Scrollbar(textpad)
textpad.config(yscrollcommand = scroll.set)
scroll.config(command = textpad.yview)
scroll.pack(side = RIGHT,fill = Y)
#create menu
menubar = Menu(root)
root.config(menu = menubar)

def new():
    root.title('Untitled')
    filename = None
    textpad.delete(1.0, END)

def save():
    global filename
    try:
        f = open(filename, 'w')
        msg = textpad.get(1.0, END)
        f.write(msg)
        f.close()
    except:
        saveas()

def openfile():
    new()
    name = askopenfilename(filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                           title="Choose a file.")
    print(name)
    # Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name, 'r') as UseFile:
            text = UseFile.read();
            print(UseFile.read())
            print(text)
            textpad.insert(1.0, text)
    except:
        logging.exception("message")
        print("No file exists")

def saveas():
    t = textpad.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    savelocation = savelocation + ".txt"
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()

filemenu = Menu(menubar)
filemenu.add_command(label = 'New', accelerator ='ctrl + N', command = new)
filemenu.add_command(label = 'Open', accelerator ='ctrl + O', command = openfile)
filemenu.add_command(label = 'Save', accelerator ='ctrl + S', command = save)
filemenu.add_command(label = 'Save As', accelerator ='ctrl + Shift + s', command = saveas)
menubar.add_cascade(label='File', menu=filemenu)

#Edit Menu
editmenu = Menu(menubar)
editmenu.add_command(label = 'Undo',accelerator = 'ctrl + z')
editmenu.add_command(label = 'Redo',accelerator = 'ctrl + y')
editmenu.add_command(label = 'Copy',accelerator = 'ctrl + c')
editmenu.add_command(label = 'Cut',accelerator = 'ctrl + x')
editmenu.add_command(label = 'Paste',accelerator = 'ctrl + v')
editmenu.add_command(label = 'Find',accelerator = 'ctrl + F')
editmenu.add_command(label = 'Select All',accelerator = 'ctrl + A')
menubar.add_cascade(label = 'Edit',menu = editmenu)

def cut():
  textpad.event_generate('<<Cut>>')

def copy():
  textpad.event_generate('<<Copy>>')

def paste():
  textpad.event_generate('<<Paste>>')

def redo():
  textpad.event_generate('<<Redo>>')

def undo():
  textpad.event_generate('<<Undo>>')

def selectAll():
  textpad.tag_add('sel','1.0',END)

def search():
  topsearch = Toplevel(root)
  topsearch.geometry('300x30+200+250')
  label1 = Label(topsearch,text='Find')
  label1.grid(row=0, column=0,padx=5)
  entry1 = Entry(topsearch,width=20)
  entry1.grid(row=0, column=1,padx=5)
  button1 = Button(topsearch,text='查找')
  button1.grid(row=0, column=2)

root.mainloop()