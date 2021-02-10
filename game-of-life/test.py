# import numpy as np
# a = int(input("Enter the number of rows:"))
# b = int(input("Enter the number of columns:"))
# print("Enter the number in a single line separated by space:")
# val = list(map(int, input().split()))
# matrix = np.array(val).reshape(a,b)
# print(matrix)
# Var1 = 1
# Var2 = 0
# def function(): 
#     global Var1, Var2
#     if Var2 == 0 and Var1 > 0:
#         print("Result One")
#     elif Var2 == 1 and Var1 > 0:
#         print("Result Two")
#     elif Var1 < 1:
#         print("Result Three")
#     Var1 =- 1
# function()
# from p5 import *

# def setup():
#    size(100, 100)


# def draw():
#    background(204)
#    if mouse_is_pressed:
#       fill(255)
#    else:
#       fill(0)
#    rect((25, 25), 50, 50)

# if __name__ == '__main__':
#    run()
# import numpy as np
# from p5 import *
# import random
# from cell import Cell

# def make_matrix(cols, rows):
#     matrix = np.empty([cols, 0])
#     for i in range(cols):
#         cell_row = []
#         for j in range(rows):
#             cell = Cell(random.randint(0, 1), i, j)
#             cell_row.append(cell)
#         # print(cell_row)
#         matrix = np.vstack( (matrix, cell_row) )
#     return matrix

# def test_matrix():
#     matrix = np.empty([0, 3])
#     print('matrix: ', matrix)
#     cell_row = [Cell(random.randint(0, 1), 0, 0), Cell(random.randint(0, 1), 1, 1), Cell(random.randint(0, 1), 2, 2)]
#     matrix = np.vstack( (matrix, cell_row) )
#     print(matrix)

# def make_matrix(cols, rows):
#     matrix = np.zeros( (cols, rows) )
#     for i in range(cols):
#         for j in range(rows):
#             cell = Cell(random.randint(0, 1), i, j)
#             matrix[i][j] =  cell
#     return matrix


# test_matrix()
# current_grid = make_matrix(10, 10)
# print(current_grid)
# for i in range(10):
#     for j in range(10):
#         print(current_grid[i][j].print_state())

from p5 import *

gray = 0

def setup():
   size(100, 100)

def draw():
   background(gray)

def mouse_pressed():
   global gray
   gray += 20

if __name__ == '__main__':
   run()