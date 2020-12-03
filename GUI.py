import time
import tkinter as tk
import AIEnvironment
import Minimax

def main_gameflow(r, c):

    # game is in progress
    actions = AIEnvironment.action(board)
    if (r, c) in actions:
        display_board[r][c]["text"] = "H"
        board[r][c] = "H"
        label_1["text"] = "AI turn"
        label_1["text"] = "Wait Computer is Thinking"

        if AIEnvironment.terminal(board):
            if AIEnvironment.draw((board)):
                label_1["text"] = "Game Ends no one wins"
            else:
                label_1["text"] = "winner is " + AIEnvironment.win(board)

            return

        value, cordinates = minimax.minimax(curr_depth=0,state=board,max_turn=True)
        display_board[cordinates[0]][cordinates[1]]["text"] = "A"
        board[cordinates[0]][cordinates[1]] = "A"
        label_1["text"] = "Your Turn"


    else:
        label_1["text"] = "Not a Valid Move"
        time.sleep(2)
        label_1["text"] = "Your Turn"





# main program
window_1 = tk.Tk()
window_1.title('Connect Four')

minimax = Minimax.Minimax(6)

board = [['' for _ in range(6)] for _ in range(6)]
display_board = [['' for _ in range(6)] for _ in range(6)]

for i in range(len(board)):
    for j in range(len(board)):
        display_board[i][j] = tk.Button(text='',font=('normal',60,'normal'),width=3,height=2,command=lambda r=i,c=j: main_gameflow(r,c))
        display_board[i][j].grid(row=i,column=j)


label_1=tk.Label(text="Your Turn",font=('normal',22,'bold'))
label_1.grid(row=6,column=3)
window_1.mainloop()


