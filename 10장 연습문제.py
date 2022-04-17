from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *

# 2017038093 김동민

def pen():
    global name
    name = askopenfilename(parent = window, filetypes = (("GIF", "*.gif"),
                ("모든 파일", "*.*")))
    photo = PhotoImage(file = name)
    pLabel.configure(image = photo)
    pLabel.image = photo

value = 0

def Exit():
    window.quit()
    window.destroy()

def key_up(event): ##확대
    photo = PhotoImage(file = name)
    photo = photo.zoom(3,3)
    pLabel.configure(image = photo)
    pLabel.image = photo
 
def key_Down(event):  ## 축소
    photo = PhotoImage(file = name)
    photo = photo.subsample(3,3)
    pLabel.configure(image = photo)
    pLabel.image = photo

window = Tk()
window.geometry("500x500")
window.title("연습문제")

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일', menu = fileMenu)
fileMenu.add_command(label = '파일 열기', command = pen)
fileMenu.add_separator()
fileMenu.add_command(label = '프로그램 종료', command = Exit)

window.bind("<Up>",key_up)
window.bind("<Down>",key_Down)

window.mainloop()
