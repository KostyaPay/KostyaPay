from tkinter import * 
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Calc on KostyaPay")
root["bg"] = "black"
def calc(key):
    global memory
    if key == "=":
        strl="-+012345678900000.*/"
        if calc_entry.get()[0] not in strl:
            calc_entry.insert(END, "")
            messagebox.showerror("","Error")
        try:
            result = eval (calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "")
            messagebox.showerror("", "Error")
    elif key == "C":
        calc_entry.delete(0, END)
    elif key == "-/+":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] =="-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)    
        
bttn_list = ["+","-", "/","*","-/+","=",".","C",
             "1","2","3","4","5","6","7","8","9","0","00","000"
]
r = 1
c = 0

for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text = i, command = cmd).grid(row=r, column=c)
    c += 1
    if c>4:
        c=0
        r += 1
        
calc_entry = Entry(root, width = 33)
calc_entry.grid(row=0, column=0, columnspan=5)
        
root.mainloop()

