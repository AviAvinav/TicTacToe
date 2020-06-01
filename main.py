from os import system
import time
from math import inf as infinity

board = ["_","_","_","_","_","_","_","_","_"]


def print_board(x):
    print(" ", x[0], "|", x[1], "|", x[2], " ")
    print("------------")
    print(" ", x[3], "|", x[4], "|", x[5], " ")
    print("------------")
    print(" ", x[6], "|", x[7], "|", x[8], " ")
    print("------------")

def evaluate(state):
    if winner(state, "O"):
        score += 1
    elif winner(state, "X"):
        score += -1
    else:
        score = 0

    return score

def available_spots(x):
    result =[]
    for i,j in enumerate(x):
        if j == "_":
            result.append(i)

    return result

def winner(state, player):
    win_state =[
        [state[0], state[1], state[2]],
        [state[3], state[4], state[5]],
        [state[6], state[7], state[8]],
        [state[0], state[4], state[8]],
        [state[0], state[3], state[6]],
        [state[2], state[4], state[6]],
        [state[2], state[5], state[8]],
        [state[1], state[4], state[7]],
    ]

    if [player, player, player] in win_state:
        return True
    else:
        return False

def game_over(state):
    return winner(state, "X") or winner(state, "O")

def minimax(x, depth, player):
    if player == "O":
        best = [-1, -infinity]
    else:
        best = [-1, infinity]

    if depth == 0 or game_over(x):
        score = evaluate(x)
        return [-1, score]

    for cell in available_spots(x):
        x[cell] = player

        if player == "O"
            score = minimax(x, depth - 1, "X")
        else:
            score = minimax(x, depth - 1, "O")

        x[cell] = "_"
        score[0] = cell
        if player == "O":
            if best[1] < score[1]:
                best = score
        else:
            if best[1] > score[1]:
                best = score

    return best

def human_response(x):
    depth = len(available_spots(x))
    if depth == 0 or game_over(x):
        return

    move = -1

    while move < 1 or move > 9:
        clean()
        print("Human's Turn\n")
        print_board(x)
        move = int(input("Enter position from 1 to 9"))

        if move <= 9 or move >= 1:
            if x[move-1] == "_"
                move -= 1
                x[move] = "X"
                print_board(x)
                return
            else:
                print_board("This position isn't free.")
                move = -1
                time.sleep(1)

        else:
            print("bad move")
            move = -1


def clean():
    system('cls')


def computer_move():
    depth = len(available_spots(board))
    if depth == 0 or game_over(board):
        return

    clean()

    print("AI's turn \n")
    move = minimax(board, depth, 'O')
    board[move[0]] = "O"
    print_board(board)
    time.sleep(1)


def main(x):
    while len(available_spots(x)) > 0 and not game_over(board):
        human_response(x)
        computer_move()

    if winner(x, "X"):
        print("You won!")
        return 0
    elif winner(x, "O"):
        print("Computer won.")
        return 0
    else:
        print("It's a draw.")
        return 0

if __name__ == "__main__":
    while True:
        main(board)
        board = ["_","_","_","_","_","_","_","_","_"]
        again = input("Wanna play again? [Y/N]: ")
        if again == "N":
            break
