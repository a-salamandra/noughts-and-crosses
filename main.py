def display_board():

    print (f"""  Ход № {turn_count}!
    {board[1]} | {board[2]} | {board[3]}
    ---------
    {board[4]} | {board[5]} | {board[6]}
    ---------
    {board[7]} | {board[8]} | {board[9]}""")

def make_turn(turn):

    player = "O" if turn%2 == 0 else "X"

    space = int(input(f"Игрок {player} укажите клетку: "))

    while space not in legal_moves:
        space = int(input(f"Игрок {player} укажите правильную клетку: "))

    board[space] = player
    legal_moves.remove(space)

def is_there_a_winner():

    if board[1] == board[2] == board[3]:
        print(f"Игрок {board[1]} победил!")
        return True
    elif board[4] == board[5] == board[6]:
        print(f"Игрок {board[4]} победил!")
        return True
    elif board[7] == board[8] == board[9]:
        print(f"Игрок {board[7]} победил!")
        return True
    elif board[1] == board[5] == board[9]:
        print(f"Игрок {board[1]} победил!")
        return True
    elif board[3] == board[5] == board[7]:
        print(f"Игрок {board[3]} победил!")
        return True
    elif board[1] == board[4] == board[7]:
        print(f"Игрок {board[1]} победил!")
        return True
    elif board[2] == board[5] == board[8]:
        print(f"Игрок {board[2]} победил!")
        return True
    elif board[3] == board[6] == board[9]:
        print(f"Игрок {board[3]} победил!")
        return True
    elif legal_moves == []:
        print("Ничья")
        return True
    else:
        return False

if __name__ == '__main__':

    board = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
    legal_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    turn_count = 1

    while not is_there_a_winner():
        display_board()
        make_turn(turn_count)
        turn_count += 1