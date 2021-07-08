import tkinter as tk


def flash(button, buttons=set(), _after=[]):
    if button not in buttons:
        buttons.add(button)
    current_color = button.cget("foreground")
    next_color = "grey" if current_color == "black" else "black"
    for button in buttons:
        button.config(foreground=next_color)
    for after_id in _after:
        root.after_cancel(after_id)
    if buttons:
        _after.append(root.after(1000, flash, button))


if __name__ == '__main__':
    root = tk.Tk()

    Button1 = tk.Button(root, text="Button1", foreground="grey")
    Button2 = tk.Button(root, text="Button2", foreground="grey")

    Button1.pack()
    Button2.pack()

    Button1.bind("<ButtonPress-1>", lambda event: flash(Button1))
    Button2.bind("<ButtonPress-1>", lambda event: flash(Button2))

    root.mainloop()
