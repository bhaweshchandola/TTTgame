from random import randrange

print("Project:Uber-Cool")
print("Welcome to the game of Tic-Tac-Toe:")
print("the game board will look something like this::")
#x=[[print(x,end='') print('') for x in range(0,3)] for y in range(0,3) print('')]
flag=1
for x in range(0,3):
    for y in range(0,3):
        print(flag,end='')
        flag+=1
    print('')

y=[[0,0,0],[0,0,0],[0,0,0]]
validmove=[1,2,3,4,5,6,7,8,9]


def uinput(turn):
    
    x=int(input("Make your move player {}:".format(turn)))
    if x in validmove:
        validmove.remove(x)
        if x==1:
            y[0][0]=turn
        elif x==2:
            y[0][1]=turn
        elif x==3:
            y[0][2]=turn
        elif x==4:
            y[1][0]=turn
        elif x==5:
            y[1][1]=turn
        elif x==6:
            y[1][2]=turn
        elif x==7:
            y[2][0]=turn
        elif x==8:
            y[2][1]=turn
        elif x==9:
            y[2][2]=turn
    else:
        print("invalid move")
        uinput(turn)
            

def board():
    for i in y:
        for j in i:
            print(j,end='')
        print('')

def win():
    if ((y[0][0]==y[0][1]==y[0][2]==1) or
        (y[1][0]==y[1][1]==y[1][2]==1) or
        (y[2][0]==y[2][1]==y[2][2]==1) or
        (y[0][0]==y[1][0]==y[2][0]==1) or
        (y[0][1]==y[1][1]==y[2][1]==1) or
        (y[0][2]==y[1][2]==y[2][2]==1) or
        (y[0][0]==y[1][1]==y[2][2]==1) or
        (y[2][0]==y[1][1]==y[0][2]==1)) :
        return 1
    if ((y[0][0]==y[0][1]==y[0][2]==2) or
        (y[1][0]==y[1][1]==y[1][2]==2) or
        (y[2][0]==y[2][1]==y[2][2]==2) or
        (y[0][0]==y[1][0]==y[2][0]==2) or
        (y[0][1]==y[1][1]==y[2][1]==2) or
        (y[0][2]==y[1][2]==y[2][2]==2) or
        (y[0][0]==y[1][1]==y[2][2]==2) or
        (y[2][0]==y[1][1]==y[0][2]==2)) :
        return 2
        
    

def main():
    playerturn=0
    while(playerturn<9):
        
        if playerturn%2==0:
            uinput(1)
            board()
            if win()==1:
                print("player 1 wins!!!")
                break
        if playerturn%2==1:
            uinput(2)
            board()
            if win()==2:
                print("player 2 wins!!!")
                break
        playerturn+=1    
main()



    


    
