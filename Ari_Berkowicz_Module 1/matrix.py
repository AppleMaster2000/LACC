#import sys for stdout
import sys

#print a 2-dimensional grid
def printGrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            sys.stdout.write('|' + str(grid[i][j]) + '|')
        sys.stdout.write('\n')
        sys.stdout.flush()
    return

def hit(row, col):
    matrix[row][col] = "x"
    printGrid(matrix)
    print "-------------------------------------------------------------------------"

#create a square matrix of dimension 10, initialize all cells to 0, and print it out
dimension = 10
matrix = [[0 for i in range(dimension)] for j in range(dimension)]
printGrid(matrix)
print "-------------------------------------------------------------------------"
f = True
g = True
score = 0
fails = 0
while(g):
    while(f):
        print "Score:" + str(score)
        row = input("Please give me the row ")
        col = input("Please give me the column ")
        hit(row, col)
        if((row == 0 and col == 0)or(row == 9 and col == 9)or(row == 8 and col == 9)or(row == 7 and col == 9)or(row == 6 and col == 9)or(row == 5 and col == 9)or(row == 5 and col == 5)or(row == 5 and col == 7)or(row == 5 and col == 6)or(row == 8 and col == 4)or(row == 4 and col == 7)or(row == 4 and col == 8)or(row == 3 and col == 6)or(row == 4 and col == 6)):
            print "You hit a battle ship"
            score += 1
        if(score == 1):
            print "You win battle ship congratulations!"
            print "You failed this many times:" + str(fails)
            f = False
        else:
            print "Keep going you did not hit a ship yet"
            fails += 1
    reset = raw_input("Want to play again? If so hit y ")
    if(reset == "y"):
        score = 0
        fails = 0
        matrix = [[0 for i in range(dimension)] for j in range(dimension)]
        printGrid(matrix)
        print "-------------------------------------------------------------------------"
        f = True
    else:
        g = False
