# -*- coding:utf-8 -*-

import tkinter

# main window
main_window = tkinter.Tk()
main_window.title("Test")
main_window.geometry("320x240")
main_window.resizable(False, False)
status = tkinter.StringVar()
status.set("Status: Press OK or Exit")
#  commands
def cmd1():
    status.set("Status: You pressed OK!")
def close_window():
    main_window.destroy()
# interface objects
label1 = tkinter.Label(main_window, text="Hello, I'm Window!")
button1 = tkinter.Button(main_window, text="OK", command=cmd1)
button2 = tkinter.Button(main_window, text="Exit", command=close_window)
status_label1 = tkinter.Label(main_window, textvariable=status)
# interface objects locations
label1.place(x=100, y=60)
button1.place(x=90, y=160)
button2.place(x=180, y=160)
status_label1.place(x=10, y=210)
main_window.mainloop()