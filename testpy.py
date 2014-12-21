from Tkinter import *

# Create a class that specializing the Button class from the tkinter
class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        # Change the message here
        self['text'] = 'Good Bye'
        # Command to close the window (the destory method)
        self['command'] = parent.destroy
        self.pack(side=BOTTOM)

root = Tk()

quitButton(root)

mainloop()
