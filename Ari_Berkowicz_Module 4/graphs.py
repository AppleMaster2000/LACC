#!/usr/bin/python2.6

# Graph Theory easy exercises for Social Networks module
# LACC 2016

#*************************************
# This is where you write your code
#
# matrix_load()
#
# Loads an adjacency matrix for a graph from a file
#
# input: none
# output: matrix containing each node 
# 
# Note: You can open a file using open("filename.txt")
# 
# You can get a list containing each line with file.readlines()
#
# You'll need to grab each number from each line, cast it to an
# int using int() and place it into your matrix
#
# A matrix is just a double list (e.g., x[][] )
#*************************************
def matrix_load():
    filename = 'matrix.txt'
    f = open(filename)
    data = f.readlines()
    size = int(data[0])
    matrix = [[0 for x in range(size)] for y in range(size)]
    row = 0
    f.close()
    for col in range(size):
        if col < (size):     
            for row in range(size):
                matrix[col][row] = int(data[col + 1][row])
    return matrix

#*************************************
# This is where you write your code
#
# print_degrees(mat)
#
# Prints the degrees of all nodes in a graph given an adj. matrix 
#
# input: the adjacency matrix of the graph
# output: none
# 
# Note: You don't need to return anything. 
#
# Effectively, you'll need to count the number of 1s in each row 
# (or each column) and print this. Use a nested loop (for or while)
#*************************************

def is_connected(matrix, node, visitedNodes):
    for col in range(len(matrix)):
        if(matrix[node][col] == 1 and (col not in visitedNodes)):
            visitedNodes.add(col)
            visitedNodes = is_connected(matrix, col, visitedNodes)
    return visitedNodes 

def is_connected1(matrix):
    data = is_connected(matrix, 0, {0})
    if(len(data) == len(matrix)):
        return "Its connected"
    else:
        return "Its not connected"
        
def print_degrees(mat):
    for col in range(len(mat)):
        degree = 0
        for row in range(len(mat)):
            if mat[col][row] == 1:
                degree += 1
        print "The number of 1's in column " + str(col + 1) +" is " + str(degree)

def create_matrix(size):
    matrix = []
    col1 = math.random(0,1)
    row1 = math.random(0,1)
    for col in range(size):
        for row in range(size):
            
    
print is_connected1(matrix_load())
