from tkinter import *

buttons = ["b"]*9
row = [0,0,0,1,1,1,2,2,2]
col = [0,1,2,0,1,2,0,1,2]
turns = 0
game_over = False

def check_winner():
    win_combos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in win_combos:
        a, b, c = combo
        t = buttons[a]["text"]
        if t != " " and t == buttons[b]["text"] == buttons[c]["text"]:
            status_label.config(text=f"🎉 {t} wins!", fg="gold")
            for btn in buttons:
                btn.config(state=DISABLED)
            return True

    if all(buttons[i]["text"] != " " for i in range(9)):
        status_label.config(text="It's a tie!", fg="white")
        return True

    return False

def enter(btn):
    global turns, game_over
    if game_over or btn["text"] != " ":
        return
    if turns % 2 == 0:
        btn.config(text="X", fg="blue")
        next_turn = "O"
    else:
        btn.config(text="O", fg="red")
        next_turn = "X"
    turns += 1

    if check_winner():
        game_over = True
    else:
        status_label.config(text=f"{next_turn}'s turn",
                            fg="lightblue" if next_turn == "X" else "salmon")

def reset():
    global turns, game_over
    turns = 0
    game_over = False
    for btn in buttons:
        btn.config(text=" ", state=NORMAL)
    status_label.config(text="X's turn", fg="lightblue")

window = Tk()
window.title("Tic Tac Toe")
window.config(pady=30, padx=50, bg="black")

status_label = Label(window, text="X's turn", font=("Arial", 18, "bold"),
                     bg="black", fg="lightblue")
status_label.grid(row=0, column=0, columnspan=3, pady=(0, 15))

for i in range(9):
    buttons[i] = Button(window, text=" ", width=10, height=5,
                        font=("Arial", 16, "bold"))
    buttons[i].config(command=lambda b=buttons[i]: enter(b))
    buttons[i].grid(row=row[i]+1, column=col[i], padx=5, pady=5)

reset_btn = Button(window, text="Reset", font=("Arial", 12),
                   command=reset, width=15)
reset_btn.grid(row=4, column=0, columnspan=3, pady=(15, 0))

window.mainloop()