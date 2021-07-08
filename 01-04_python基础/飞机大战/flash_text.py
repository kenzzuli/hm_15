from tkinter import *
import tkinter.font as tkFont


def flash_text_a(text):
    canvas.itemconfigure(canvas.find_withtag('a_text'), fill=flashing_colors[idx])
    canvas.itemconfigure(canvas.find_withtag('b_text'), fill=flashing_colors[idx])
    window.after(100, flash_text_a, 'dummy', (idx + 1) % 2)


def flash_text_b(event=None, idx=0):
    print(idx)
    flashing_colors = ['black', 'grey']
    canvas.itemconfigure(canvas.find_withtag('b_text'), fill=flashing_colors[idx])
    window.after(1000, flash_text_a, 'dummy', (idx + 1) % 2)


window = Tk()
window.title("Flash")
ft = tkFont.Font(size=100)
canvas = Canvas(
    window,
    width=1200,
    height=1200,
    background="grey"
)
canvas.pack()

a_text = canvas.create_text(600, 200, text='我', font=ft, fill="black", tags="a_text")
b_text = canvas.create_text(600, 800, text="们", font=ft, fill="black", tags="b_text")
# canvas.bind("<ButtonPress-1>", flash_text_a)
# canvas.bind("<ButtonPress-2>", flash_text_b)
mainloop()
