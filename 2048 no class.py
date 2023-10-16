import random
import numpy as np

# class Driver:

print("Controls: w to move up, a to move left, s to move down, d to move right")


shape = (4,4)
arr = np.zeros(shape)
row = 0
col = 0
pos = (row, col)

def play():
    for i in range(4):
        for j in range(4):
            if arr[i][j] == 2048:
                print("you win!")
                exit()  
    
    print(arr)
    user_move()
    #checks if game is finished 2048
    #otherwise displays results and calls user move



def user_move():
    move = input().strip()
    valid = ['w', 'a', 's', 'd']
    while move not in valid:
        print("enter a valid move")
        input()
    if move == 'w':
        up()
    elif move == 'a':
        left()
    elif move == 's':
        down()
    elif move == 'd':
        right()
    new_num(pos)

def up():
    #move all nonzero values to top, then merge adjacent duplicates 
    global arr
    temp = arr
    arr = np.zeros(shape)
    #moves to topside
    for i in range(4): #iterating cols from 0 to 3 (left to right)
        pos = 0
        for j in range(4): #iterating rows from 0 to 3 (top to down)
            if(temp[j][i] != 0):
                arr[pos][i] = temp[j][i]
                pos += 1

    for i in range(4):
        for j in range(4): 
            if i >= 0 and i < 3 and arr[i][j] == arr[i+1][j]: #check adjacency of values below it
                arr[i][j] *= 2
                arr[i+1][j] = 0
            # elif i < 3 and arr[i][j] == arr[i+1][j]:
            #     arr[i][j] *= 2
            #     arr[i+1][j] = 0

    changed = False
    for i in range(4):
        for j in range(4):
            if(temp[i][j] != arr[i][j]):
                changed = True
    if changed is False:
        play()
    
    temp = arr #remerge because of potential gaps due to merging
    arr = np.zeros(shape)
    for i in range(4): 
        pos = 0
        for j in range(4): 
            if(temp[j][i] != 0):
                arr[pos][i] = temp[j][i]
                pos += 1
        
def left():
    global arr
    temp = arr
    arr = np.zeros(shape)
    for i in range(4):
        pos = 0
        for j in range(4):
            if(temp[i][j] != 0):
                arr[i][pos] = temp[i][j]
                pos += 1

    for i in range(4):
        for j in range(4): #0 0 1 1 > 0 0 2 0 , 1 1 0 0 > 2 0 0 0 
            if j >= 0 and j < 3 and arr[i][j] == arr[i][j+1]: #same values on the left 220 > 200
                arr[i][j] *= 2
                arr[i][j+1] = 0
            # elif j < 3 and arr[i][j] == arr[i][j+1]: #same values on the right 022 > 020
            #     arr[i][j] *= 2
            #     arr[i][j+1] = 0

    changed = False
    for i in range(4):
        for j in range(4):
            if(temp[i][j] != arr[i][j]):
                changed = True
    if changed is False:
        play()    

    temp = arr
    arr = np.zeros(shape)
    for i in range(4):
        pos = 0
        for j in range(4):
            if(temp[i][j] != 0):
                arr[i][pos] = temp[i][j]
                pos += 1

def down():
    global arr
    temp = arr
    arr = np.zeros(shape)
    #moves to topside
    for i in range(4): #iterating cols from 0 to 3 (left to right)
        pos = 0
        for j in range(4): #iterating rows from 3 to 0 (down to up)
            if(temp[3-j][i] != 0):
                arr[3-pos][i] = temp[3-j][i]
                pos += 1

    for i in range(4):
        for j in range(4): #check equality to upper value 1 1 0 0 > 0 2 0 0
            if i >= 0 and i < 3 and arr[3-i-1][j] == arr[3-i][j]:
                arr[3-i][j] *= 2
                arr[3-i-1][j] = 0
            # elif i == 3 and arr[3-i][j] == arr[3-i+1][j]:
            #     arr[3-i+1][j] *= 2
            #     arr[3-i][j] = 0

    changed = False
    for i in range(4):
        for j in range(4):
            if(temp[i][j] != arr[i][j]):
                changed = True
    if changed is False:
        play()            

    temp = arr
    arr = np.zeros(shape)
    for i in range(4): #iterating cols from 0 to 3 (left to right)
        pos = 0
        for j in range(4): #iterating rows from 3 to 0 (down to up)
            if(temp[3-j][i] != 0):
                arr[3-pos][i] = temp[3-j][i]
                pos += 1

def right(): 
    global arr
    temp = arr
    arr = np.zeros(shape)
    for i in range(4):
        pos = 0
        for j in range(4):
            if(temp[i][3-j] != 0):
                arr[i][3-pos] = temp[i][3-j]
                pos += 1

    for i in range(4):
        for j in range(4): #1 1 0 0 
            if j >= 0 and j < 3 and arr[i][3-j] == arr[i][3-j-1]: #same values on left 
                arr[i][3-j] *= 2
                arr[i][3-j-1] = 0
            # elif j == 3 and arr[i][3-j] == arr[i][3-j+1]:
            #     arr[i][3-j+1] *= 2
            #     arr[i][3-j] = 0

    changed = False
    for i in range(4):
        for j in range(4):
            if(temp[i][j] != arr[i][j]):
                changed = True
    if changed is False:
        play() 

    temp = arr
    arr = np.zeros(shape)
    for i in range(4):
        pos = 0
        for j in range(4):
            if(temp[i][3-j] != 0):
                arr[i][3-pos] = temp[i][3-j]
                pos += 1


def random_pos():
    row = random.randint(0, 3)
    col = random.randint(0, 3)
    pos = (row, col)
    return pos

def two(pos):
    pos = random_pos() 
    while arr[pos[0]][pos[1]] != 0:
        pos = random_pos()
    arr[pos[0]][pos[1]] = 2

def four(pos):
    pos = random_pos()
    while arr[pos[0]][pos[1]] != 0:
        pos = random_pos()
    arr[pos[0]][pos[1]] = 4

def new_num(pos):
    has_space = False
    for i in range(4):
        for j in range(4):
            if arr[i][j] == 0:
                has_space = True
    if has_space == False:
        print("you loes!")
        exit()
    if random.randint(0, 9) == 9:
        four(pos)
    else:
        two(pos)
    play()

new_num(pos)
play()



    


