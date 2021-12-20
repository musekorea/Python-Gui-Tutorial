import tkinter

root = tkinter.Tk()
root.title("MOYA GUI")
root.geometry("300x300")


def click():
    print("Button Clicked")


my_btn_image = tkinter.PhotoImage(file="01-GUI-Basic/image/test_btn.png")
btn6 = tkinter.Button(root, image=my_btn_image, command=click)
btn6.pack()

root.mainloop()
