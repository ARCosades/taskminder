""" 
This App is called TaskMinder. 
It is a simple App that displays 
the activity that you're working on 
"""

import Tkinter


class Example(Tkinter.Frame):
    def __init__(self, parent):      
        Tkinter.Frame.__init__(self, background="black")
        self.parent = parent
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        parent.geometry(("%dx100")%(screen_width/2))
#        parent.overrideredirect(1)
        self.initUI(parent)
        self.pack(expand=1, fill=Tkinter.BOTH)
    def initUI(self,parent):
        self.B1 = quitButton(parent)
        self.headlabel = headLabel(parent) 
class quitButton(Tkinter.Button):
    def __init__(self, parent):
        Tkinter.Button.__init__(self, bg="black", fg="white")
        self['text'] = 'Exit'
        self['command'] = parent.destroy
        self.pack(side=Tkinter.RIGHT, expand=0, fill=Tkinter.Y)

class headLabel(Tkinter.Label):
    def __init__(self, parent):
        Tkinter.Label.__init__(self, text="This is the header Text", bg="white", fg="red")
        self.pack(side=Tkinter.TOP, expand=1)

def helloworld():
    print "Hello world"
    

def main():
    root = Tkinter.Tk()
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
