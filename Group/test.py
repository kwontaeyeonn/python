import tkinter as tk

window = tk.Tk()
window.title("간단한 GUI")
window.geometry("300x100")

label = tk.Label(window, text="안녕하세요!")
label.pack()

window.mainloop()

