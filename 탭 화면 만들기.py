from tkinter import *
from tkinter import ttk

# 2017038093 김동민
window = Tk()

baseTab = ttk.Notebook(window)

tabDog = ttk.Frame(baseTab)
baseTab.add(tabDog, text='강아지')
tabCat = ttk.Frame(baseTab)
baseTab.add(tabCat, text='고양이')

baseTab.pack(expand=1, fill="both")

photoDog = PhotoImage(file = "gif/dog.gif")
labelDog = Label(tabDog, image = photoDog)
labelDog.pack()

photoCat = PhotoImage(file = "gif/cat.gif")
labelCat = Label(tabCat, image = photoCat)
labelCat.pack()

window.mainloop()
