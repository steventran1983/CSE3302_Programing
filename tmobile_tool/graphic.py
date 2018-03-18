from tkinter import *

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - 1024/2
y = (screen_height/2) - 768/2
root.geometry('%dx%d+%d+%d' % (1024, 768, x, y))




top_frame = Frame(root)
top_frame.pack(side=TOP)

label_command = Label(root, text="Command")
label_command.pack(side)

bottom_frame = Frame(root)
bottom_frame.pack(side= BOTTOM)

# scroll_bar = Scrollbar(bottom_frame)
# scroll_bar.pack(side=RIGHT, fill=Y)



# label_command = Label(root, text="Command")
# label_command.grid(row=0,column=0)
# #
# entry_command = Entry(root, width=70)
# entry_command.grid(row =0,column =1)
# #
# button_run = Button(root,text = "Run")
# button_run.grid(row = 0,column=2)
#
# label_command = Label(root)
# label_command.grid(row=1,column=0)

# scrollbar_V = Scrollbar()
# scrollbar_H = Scrollbar(orient=HORIZONTAL)
# scrollbar_V.grid(row=2, column=0, sticky=N + S + W)
# scrollbar_H.grid(row=2, column=0, sticky=N + E + S + W)
#
#
# listbox1 = Listbox(root,width=50,height = 20, yscrollcommand=scrollbar_V.set, xscrollcommand=scrollbar_H.set)
# listbox1.grid(row=2, column=0)

# lb = Listbox(width=30, height=20)
# lb.grid(row = 2, column=1)
#
# scrollbar = Scrollbar(orient="vertical", command=lb.yview)
# scrollbar.grid(row=  2, column =1 , sticky=N+S+W)
#
# lb.config(yscrollcommand=scrollbar.set)
#
# for i in range(10):
#     lb.insert(END, 'test'+str(i))



root.mainloop()