import tkinter

root = tkinter.Tk()
root.title("MOYA GUI")
root.geometry("300x300")

txt = tkinter.Text(root, width=30, height=10)
txt.insert(1.0, "글자를 입력하세요")
txt.pack()


def btn_click():
    value = txt.get(0.0, tkinter.END)
    print(value)
    txt.delete(0.0, tkinter.END)


btn = tkinter.Button(root, text="CLICK", command=btn_click)
btn.pack()
root.mainloop()
