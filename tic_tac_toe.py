def printboard():
    
    zero = "X" if xstate[0] == 1 else "O" if zstate[0] == 1 else 0
    one = "X" if xstate[1] == 1 else "O" if zstate[1] == 1 else 1
    two = "X" if xstate[2] == 1 else "O" if zstate[2] == 1 else 2
    three = "X" if xstate[3] == 1 else "O" if zstate[3] == 1 else 3
    four = "X" if xstate[4] == 1 else "O" if zstate[4] == 1 else 4
    five = "X" if xstate[5] == 1 else "O" if zstate[5] == 1 else 5
    six = "X" if xstate[6] == 1 else "O" if zstate[6] == 1 else 6
    seven = "X" if xstate[7] == 1 else "O" if zstate[7] == 1 else 7
    eight = "X" if xstate[8] == 1 else "O" if zstate[8] == 1 else 8

    print(f"\t\t\t\t  {zero}  |  {one}  |  {two}  ")
    print(f"\t\t\t\t-----|-----|-----")
    print(f"\t\t\t\t  {three}  |  {four}  |  {five}  ")
    print(f"\t\t\t\t-----|-----|-----")
    print(f"\t\t\t\t  {six}  |  {seven}  |  {eight}  ")


def checkwin(xstate, zstate):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4 , 6]]

    for win in wins:
        if (xstate[win[0]] + xstate[win[1]] + xstate[win[2]] == 3):
            print("-------------------------------------------------------------------------------------------------")
            print("\t\tX has won the game")
            print("-------------------------------------------------------------------------------------------------")
            return 1
        if (zstate[win[0]] + zstate[win[1]] + zstate[win[2]] == 3):
            print("-------------------------------------------------------------------------------------------------")
            print("\t\t0 has won the game")
            print("-------------------------------------------------------------------------------------------------")
            return 1
    return -1


print("-------------------------------------------------------------------------------------------------")
print("\t\t\tWelcome to the game of Tic Tac Toe")
print("-------------------------------------------------------------------------------------------------\n")

xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
zstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]


chance = 1
turns = 0
xposition = 0
zposition = 0

while(True):
    printboard()

    if checkwin(xstate, zstate) == 1:
        break

    if (turns == 9 and checkwin(xstate, zstate) == -1):
        print("The game has ended in a draw")
        break

    if chance == 1:
        print("X's turn:")
        while(True):
                xposition = int(input("Print where you want to mark your symbol: "))
                if ((xposition < 0) or (xposition > 8)):
                    xposition = int(input("Please re-enter a valid position here: "))
                    break
                else:
                    break

        xstate[xposition] += 1
        chance -= 1

    else:
        print("0's Turn")
        while(True):
                zposition = int(input("Print where you want to mark your symbol: "))
                if ((zposition < 0) or (zposition > 8)):
                    zposition = int(input("Please re-enter a valid position here: "))
                    break
                else:
                    break

        zstate[zposition] += 1
        chance += 1
    
    turns += 1