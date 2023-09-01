from tkinter import*
root=Tk()
root.geometry("300x400")
root.resizable(False,False)

bg=PhotoImage(file="pic.png").subsample(5)
lbl=Label(root,image=bg)
lbl.place(x=0,y=0)

root.mainloop()