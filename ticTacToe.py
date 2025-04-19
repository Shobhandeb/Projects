

def printboard(xState,zeroState):
    zero = 'X' if xState[0] else ( '0' if zeroState[0] else 0)
    one = 'X' if xState[1] else ( '0' if zeroState[1] else 1)
    two = 'X' if xState[2] else ( '0' if zeroState[2] else 2)
    three = 'X' if xState[3] else ( '0' if zeroState[3] else 3)
    four = 'X' if xState[4] else ( '0' if zeroState[4] else 4)
    five = 'X' if xState[5] else ( '0' if zeroState[5] else 5)
    six = 'X' if xState[6] else ( '0' if zeroState[6] else 6)
    seven = 'X' if xState[7] else ( '0' if zeroState[7] else 7)
    eight = 'X' if xState[8] else ( '0' if zeroState[8] else 8)

    print(f" {zero} | {one} | {two} ")
    print(f" --| --| --")
    print(f" {three} | {four} | {five} ")
    print(f" --| --| --")
    print(f" {six} | {seven} | {eight} ")

if __name__ =="__main__":
    print("helllo world ")
    xState = [0,0,0,0,0,0,0,0 ,0]
    zeroState =[0,0,0,0,0,0,0,0 ,0]
    turn = 1 
    print("Welcome to Tic Tac Toe ")
    while(True):
        printboard(xState,zeroState)
        if turn==1:
            print("X's Chance :")
            value = int(input("Please enter a value "))
            xState[value] = 1
        else:
            print("X's Chance :")
            value = int(input("Please enter a value "))
            zeroState[value] = 1
        printboard()
        break


#7mins : 23 secs