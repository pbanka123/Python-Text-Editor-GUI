#-*-encoding:utf8
import os
from os import open
from os import *
from tkinter import *
from tkinter import messagebox
from tkinter import dialog
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfile


#New
def new():
  root.title('Unnamed')
  filename = None
  textpad.delete(1.0,END)
#Open
def openfile():
  global filename
  filename = askopenfilename(defaultextension = '.txt')
  if filename == '':
    filename = None
  else:
    root.title('FileName:'+os.path.basename(filename))
    textpad.delete(1.0,END)
    print(filename)
    f = os.open(filename,os.O_RDONLY)
    print(filename)
    textpad.insert(1.0,f.read())
    f.close()
#Save
def save():
  global filename
  try:
    f = open(filename,'w')
    msg = textpad.get(1.0,END)
    f.write(msg)
    f.close()
  except:
    saveas()
#Save As
def saveas():
  f = asksaveasfilename(initialfile= 'Unnamed.txt', defaultextension='.txt')
  global filename
  filename = f
  fh = open(f,'w')
  msg = textpad.get(1.0,END)
  fh.write(msg)
  fh.close()
  root.title('FileName:'+os.path.basename(f))

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


root = Tk()
root.title('Benben Node')

#create menu
menubar = Menu(root)
root.config(menu = menubar)

filemenu = Menu(menubar)
filemenu.add_command(label = 'New',accelerator ='ctrl + N')
filemenu.add_command(label = 'Open',accelerator ='ctrl + O')
filemenu.add_command(label = 'Save',accelerator ='ctrl + S')
filemenu.add_command(label = 'Save As',accelerator ='ctrl + Shift + s')
menubar.add_cascade(label = 'File',menu = filemenu)

#Edit
editmenu = Menu(menubar)
editmenu.add_command(label = 'Undo',accelerator = 'ctrl + z')
editmenu.add_command(label = 'Redo',accelerator = 'ctrl + y')
editmenu.add_command(label = 'Copy',accelerator = 'ctrl + c')
editmenu.add_command(label = 'Cut',accelerator = 'ctrl + x')
editmenu.add_command(label = 'Paste',accelerator = 'ctrl + v')
editmenu.add_command(label = 'Find',accelerator = 'ctrl + F')
editmenu.add_command(label = 'Select All',accelerator = 'ctrl + A')
menubar.add_cascade(label = 'Edit',menu = editmenu)

#About
aboutmenu = Menu(menubar)
aboutmenu.add_command(label = 'Author')
aboutmenu.add_command(label = 'Copyright')
menubar.add_cascade(label = 'About',menu = aboutmenu)

#toolbar
toolbar = Frame(root,height = 15,bg = 'SkyBlue')
shortButton = Button(toolbar,text = 'New',command = open)
shortButton.pack(side = LEFT)
shortButton = Button(toolbar,text = 'Open',command = openfile)
shortButton.pack(side = LEFT,padx = 5,pady = 5)
shortButton = Button(toolbar,text = 'Save',command = save)
shortButton.pack(side = RIGHT)
shortButton = Button(toolbar,text = 'Undo',command = undo)
shortButton.pack(side = RIGHT,padx = 5,pady = 5)
toolbar.pack(expand = NO,fill = X)



#statusbar
status = Label(root,text = 'Ln20',bd = 1,relief = SUNKEN,anchor = 'w')
status.pack(side = BOTTOM,fill = X)

#Edit Area
lnlabel = Label(root,width = 2,bg = 'antique white')
lnlabel.pack(side = LEFT,fill = Y)

textpad = Text(root,undo = True)
textpad.pack(expand = YES,fill = BOTH)

scroll = Scrollbar(textpad)
textpad.config(yscrollcommand = scroll.set)
scroll.config(command = textpad.yview)
scroll.pack(side = RIGHT,fill = Y)




root.mainloop()