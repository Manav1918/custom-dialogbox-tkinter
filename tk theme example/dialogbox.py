from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk, THEMES
from tkinter import messagebox
import sys
with open('necessaries/help.txt','r') as helpfile:
    lines= helpfile.readlines()
    help =''
    help = help.join(line for line in lines)
def helpWin(root,e=None):
        infowin = Toplevel(root)
        infowin.grab_set()
        #infowin.grab_release()
        infowin.title('help')
        infowin.geometry("640x410+255+190")
        infowin.resizable(0,0)
        aboutImg = PhotoImage(file='icons/about.png')
        conImg = PhotoImage(file='icons/tick.png')
        infowin.tk.call('wm', 'iconphoto', infowin._w, aboutImg)
        lbl = Label(infowin,text="Custom Tkinter DialogBox Example Help Wizard! ",font=('arial',10,'bold','underline')).pack(fill=X,pady=3)
        ###
        f = Frame(infowin)
        f.pack(fill=BOTH,padx=5)
        yscrollbar = Scrollbar(f)
        yscrollbar.pack( side = RIGHT, fill = Y )
        txtbox = Text(f,height=21,yscrollcommand = yscrollbar.set,wrap=WORD)
        txtbox.pack(fill=BOTH,padx=5)

        txtbox.insert(END,help)
        #
        yscrollbar.config( command = txtbox.yview )
        okBtn = ttk.Button(infowin,text="  Quit  ",image=conImg,compound=LEFT,
                    style='C.TButton',cursor="hand2",command=infowin.destroy)
        okBtn.pack(side=TOP,pady=3)
        ###
        txtbox.config(state=DISABLED)
        infowin.mainloop()
