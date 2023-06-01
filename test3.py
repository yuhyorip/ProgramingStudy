# Import the required libraries
from tkinter import *
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk

# Create an instance of tkinter frame or window
win=Tk()
win.title("System Tray Application")
win.overrideredirect(True)

# Set the size of the window
win.geometry("700x350")

# Define a function for quit the window
def quit_window(icon, item):
   icon.stop()
   win.destroy()

# Define a function to show the window again
def show_window(icon, item):
   icon.stop()
   win.after(0,win.deiconify())

# Hide the window and show on the system taskbar
win.withdraw()
image=Image.open("logo.png")
menu=(item('Quit', quit_window), item('Show', show_window))
icon=pystray.Icon("name", image, "title", menu)
icon.run()
iconicButton=Label(win,text="-",bd=0,bg="gray19",font=('*Font',20),fg="snow",relief="flat")
iconicButton.bind("<Button-1>", lambda e: win.iconify())
iconicButton.place(x=640,y=9)
# win.protocol('WM_DELETE_WINDOW', hide_window)

win.mainloop()

