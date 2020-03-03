import os
os.system('cls')
#check win function 
def check_win(sym1,sym2):
    for j in range(0,7):
        if move[j] == move[j+1] and move[j+1] == move[j+2]:
            if move[j] == sym1:
                print("Player 1 WON!!")
                exit()
            elif move[j] == sym2:
                print("player 2 WON!!")
                exit()



#taking input
p1 = input("Choose 'X' or 'O' : ").upper()
if p1 == 'X':
    p2 = 'O'
elif p1 == 'O':
    p2 = 'X'
else:
    print("Unknown Input! Please try again.")
    exit()


#placing the X's and O's in the box 
move = []
for item in range(0,10):
    move.append(' ')

for i in range(0,10):
    os.system('cls')

        #printing board
    print(move[6]+'  |  '+move[7]+' |  '+move[8])
    print('------------')
    print(move[3]+'  |  '+move[4]+' |  '+move[5])
    print('------------')
    print(move[0]+'  |  '+move[1]+' |  '+move[2])


    m1 = int(input("P1 enter your position(1-9) : ")) -1
    move.pop(m1)
    move.insert(m1,p1)
    

    os.system('cls')

        #printing board
    print(move[6]+'  |  '+move[7]+' |  '+move[8])
    print('------------')
    print(move[3]+'  |  '+move[4]+' |  '+move[5])
    print('------------')
    print(move[0]+'  |  '+move[1]+' |  '+move[2])
    check_win(p1,p2)



    m2 = int(input("P2 enter your position(1-9) : ")) -1
    move.pop(m2)
    move.insert(m2,p2)
    

    os.system('cls')

        #printing board
    print(move[6]+'  |  '+move[7]+' |  '+move[8])
    print('------------')
    print(move[3]+'  |  '+move[4]+' |  '+move[5])
    print('------------')
    print(move[0]+'  |  '+move[1]+' |  '+move[2])
    check_win(p1,p2)

os.system('cls')
print("Its a TIE!!")
        
            