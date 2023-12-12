import tkinter 
from tkinter import *

from simpleicons.icons import si_bookstack
from simpleicons.image import icon_to_image
from PIL import Image, ImageTk

root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")

task_list = []

#Root Image Icon
xml_bytes = si_bookstack.get_xml_bytes(fill="black")
img = icon_to_image(xml_bytes, bg=0xFFFFFF, scale=(5, 5))
img = img.resize((32, 32), Image.ANTIALIAS)
task_icon = ImageTk.PhotoImage(img)
root.iconphoto(False, task_icon)

root.mainloop()