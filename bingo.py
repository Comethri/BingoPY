import tkinter as tk
import random

root = tk.Tk()
root.title("Bingo")

words = ["Keine\n Nazis", "WHO", "Wir\n sind\n friedlich", "gegen\n Masken", "Impfpflicht", "Trommeln", "Spazieren\n gehen",
        "ü60", "Klimawandel\n leugnen", "AFD\n propaganda", "Tagesschau\n durchsage", "Björn Höcke", "Russland\n macht\n doch\n nichts", "Frieden\n stat\n Krieg",
        "Nato\n ist\n schuld", "Redet\n obv.\n Müll", "euer Micha", "15\n Leute\n maximal", "Banger\n Musik", "klein\n Kinder", "Antifanten",
        "Diktatur", "Regierung\n muss\n weg!", "Amerikaner\n sind\n Kriegstreiber", "Freiheit"]

random.shuffle(words)

buttons = []

def assign_words():
    for i in range(5):
        row = []
        for j in range(5):
            if words:
                word = words.pop(0)
                button = tk.Button(root, text=word, width=12, height=6, highlightthickness=0, font=("TkDefaultFont", 10, "bold"), wraplength=0)
                button.grid(row=i, column=j)
                button.bind("<Button-1>", lambda event, button=button: button.configure(bg="green") if button.cget("bg") != "green" else button.configure(bg=root.cget("bg")))
                row.append(button)
        buttons.append(row)

assign_words()

def blink(button, count=5):
    if count <= 0:
        return
    button.configure(bg="yellow")
    button.after(500, lambda: button.configure(bg="green"))
    button.after(1000, lambda: blink(button, count - 1))


def check_bingo():
    for i in range(5):
        row = [button.cget("bg") for button in buttons[i]]
        if row.count("green") == 5:
            for button in buttons[i]:
                button.after(0, lambda button=button: blink(button))
            return True
        col = [button.cget("bg") for button in [buttons[j][i] for j in range(5)]]
        if col.count("green") == 5:
            for button in [buttons[j][i] for j in range(5)]:
                button.after(0, lambda button=button: blink(button))
            return True
    diagonal1 = [buttons[i][i].cget("bg") for i in range(5)]
    if diagonal1.count("green") == 5:
        for i in range(5):
            button = buttons[i][i]
            button.after(0, lambda button=button: blink(button))
        return True
    diagonal2 = [buttons[i][4-i].cget("bg") for i in range(5)]
    if diagonal2.count("green") == 5:
        for i in range(5):
            button = buttons[i][4-i]
            button.after(0, lambda button=button: blink(button))
        return True
    return False

while not check_bingo():
    root.update()

root.mainloop()