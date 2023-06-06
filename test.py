from tkinter import *

root=Tk()
root.title('Codemy.com Image Viewer')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()
    
var = IntVar()

# c = Checkbutton(root, text="Check this box.", variable = var)
# c.pack()


Staff_chk=Checkbutton(root)
Staff_chk["text"] = "Yes"
Staff_chk["variable"] = var

myButton = Button(root, text="Show", command=show).pack()

root.mainloop()