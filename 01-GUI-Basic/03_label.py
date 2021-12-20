import tkinter

root = tkinter.Tk()
root.title("MOYA GUI")
root.geometry("300x300")

label1 = tkinter.Label(root, text="HELLO")
label1.pack()

imageFile = tkinter.PhotoImage(file="01-GUI-Basic/image/btn50.png")
label2 = tkinter.Label(
    root,
    image=imageFile,
    width=50,
    height=50,
)
label2.pack()


def handleClick():
    label1.config(text="BYE BYE")
    global imageFile2
    imageFile2 = tkinter.PhotoImage(file="01-GUI-Basic/image/sun50.png")
    label2.config(image=imageFile2)


btn = tkinter.Button(root, text="CLICK", command=handleClick)
btn.pack()


root.mainloop()
