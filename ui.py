from tkinter import *
from tkinter.ttk import *
import tkinter
import proofread
import grammar
import codecs
from collections import OrderedDict

d = []

g = []

class Spellings(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('mispeltword', 'suggestions')
        tv.heading("#0", text='Line No.', anchor='center')
        tv.column("#0", anchor="center")
        tv.heading('mispeltword', text='Mispelt Word')
        tv.column('mispeltword', anchor='center', width=200)
        tv.heading('suggestions', text='Suggestions')
        tv.column('suggestions', anchor='center', width=200)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):
        for t in d:
            self.treeview.insert('', 'end', text=str(t[0] + 1), values=(t[1],
                             t[2]))
        
class Grammar(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('sentence', 'suggestion', 'type')
        tv.heading("#0", text='Line No.', anchor='center')
        tv.column("#0", anchor="center")
        tv.heading('sentence', text='Sentence')
        tv.column('sentence', anchor='center', width=200)
        tv.heading('suggestion', text='Suggestion')
        tv.column('suggestion', anchor='center', width=200)
        tv.heading('type', text='Type')
        tv.column('type', anchor='center', width=200)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):
        print(g)
        for t in g:
            self.treeview.insert('', 'end', text=str(t[0] + 1), values=(t[1],
                             t[2], t[3]))
        

def spellCheck():
    # create child window
    if(root.filename):
        fname = root.filename
        errors = proofread.proofread(fname)
        for i in range(len(errors)):
            d.append(errors[i])
        d.sort()
        if len(d) > 0:
            child = Toplevel()
            child.title("Spell Check")
            Spellings(child)

def grammarCheck():
    global g
    if(root.filename):
        # display message
        fname = root.filename
        text = ''
        with codecs.open(fname, "r",encoding='utf-8', errors='ignore') as f:
            text += f.read()
        g = grammar.check(text)
        g.sort()
        if len(g) > 0:
            child = Toplevel()
            child.title("Grammar Check")
            Grammar(child)

# create root window
root = Tk()
# put a button on it, or a menu
root.geometry("500x500")
root.title("SJournal")
back = tkinter.Frame(master=root,bg='black')
parent = Frame(root)

def getFile():
    root.filename = tkinter.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Text Files","*.txt"),("all files","*.*")))
    spellCheck()
    grammarCheck() 

Button(parent, text='Pick a file', command=getFile).pack(fill="x")
parent.pack(expand=1)
# start event-loop
root.mainloop()
