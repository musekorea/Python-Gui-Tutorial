import tkinter

root = tkinter.Tk()
root.title("Moya GUI")
root.geometry("300x300")

listbox = tkinter.Listbox(root, selectmode="extended", height=0)
listbox.insert(tkinter.END, "Moya")
listbox.insert(tkinter.END, "Baozi")
listbox.insert(tkinter.END, "Nicai")
listbox.insert(tkinter.END, "Xiaoyu")
listbox.insert(tkinter.END, "Lucky")
listbox.pack()


def btnClick():
    print(listbox.get(1))


btn = tkinter.Button(root, text="CLICK", command=btnClick)
btn.pack()

root.mainloop()
