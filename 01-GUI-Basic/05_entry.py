import tkinter

root = tkinter.Tk()
root.title("Moya GUI")
root.geometry("300x300")

ent = tkinter.Entry(root, width=30)
ent.insert(0, "한 줄 입력입니다 ")
ent.pack()


def btn_click():
    data = ent.get()
    print(data)
    ent.delete(0, tkinter.END)


btn = tkinter.Button(root, text="CLICK", command=btn_click)
btn.pack()

root.mainloop()
