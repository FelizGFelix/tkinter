from tkinter import *
from tkvideo import tkvideo

tk = Tk()
tk.title("Lonely Lonely")
vid = Label(tk)
vid.pack()
player = tkvideo("virus2/Download.mp4", vid, loop=1, size=(500,500))
player.play()
tk.mainloop()
