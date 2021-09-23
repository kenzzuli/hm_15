import tkinter as tk
import tkinter.font as tkFont


def flash_rate_1(tmp=None):
    current_color = Button1.cget("foreground")
    next_color = "grey" if current_color == "black" else "black"
    Button1.config(foreground=next_color)
    root.after(int(1000 / 6.0), flash_rate_1, Button1)  # 6hz


def flash_rate_2(tmp=None):
    current_color = Button2.cget("foreground")
    next_color = "grey" if current_color == "black" else "black"
    Button2.config(foreground=next_color)
    root.after(int(1000 / 7.0), flash_rate_2, Button2)  # 7hz


root = tk.Tk()
ft = tkFont.Font(size=200)
Button1 = tk.Button(root, text="你", background="grey", foreground="black", font=ft)
Button2 = tk.Button(root, text="好", background="grey", foreground="black", font=ft)

Button1.pack()
Button2.pack()
Button1.after(int(1000 / 6), flash_rate_1)
Button2.after(int(1000 / 7), flash_rate_2)
root.mainloop()
