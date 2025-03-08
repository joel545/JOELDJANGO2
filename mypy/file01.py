import tkinter as tk1
base = tk1.Tk()
def push():
    print("約書亞團契")
button=tk1.Button(base,text="按鈕1",command=push)
button.pack()
base.mainloop()
