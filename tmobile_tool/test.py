from tkinter import *

root = Tk()
root.geometry('500x300')

frame = Frame(root)
frame.place(x = 5, y = 5) # Position of where you would place your listbox

lb = Listbox(frame, width=70, height=6)
lb.pack(side = 'left',fill = 'y' )

scrollbar = Scrollbar(frame, orient="vertical",command=lb.yview)
scrollbar.pack(side="right", fill="y")

lb.config(yscrollcommand=scrollbar.set)

for i in range(10):
    lb.insert(END, 'test'+str(i))

root.mainloop()