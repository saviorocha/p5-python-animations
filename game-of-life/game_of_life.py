import numpy as np
from p5 import *
import random
from cell import Cell
"""
    Baseado no código de Daniel Shiffman
    https://www.youtube.com/watch?v=FWSR_7kZuYg
"""

resolution = 40
width = 400
height = 400
cols = width // resolution
rows = height // resolution

def make_matrix(cols, rows):
    matrix = np.empty([0, rows])
    for i in range(cols):
        cell_row = []
        for j in range(rows):
            cell = Cell(0, i, j) # random.randint(0, 1)
            cell_row.append(cell)
        matrix = np.vstack( (matrix, cell_row) )
    return matrix
current_grid = next_grid = make_matrix(cols, rows)

def setup():
    size(400, 400)

def draw():
    global current_grid, next_grid, cols, rows

    # next_grid = np.zeros( (cols, rows) )
    # next_grid = np.empty([0, rows])

    background(0)

    # desenha o grid
    for i in range(cols):
        for j in range(rows):
            x = i * resolution
            y = j * resolution
            if current_grid[i][j].state == 1:
                fill(255)
                rect((x, y), resolution, resolution)
                # circle((x, y), resolution)

            next_grid[i][j].state = calculate_new_grid(current_grid, i, j)
            
    # atualiza o grid para próxima iteração
    current_grid = next_grid

# cria o grid do estado seguinte
def calculate_new_grid(current_grid, i, j):
    cell_state = current_grid[i][j].state
    neighbors_sum = count_neighbors(current_grid, i, j)

    # regras do jogo da vida
    if cell_state == 0 and neighbors_sum == 3:
        return 1
    elif cell_state == 1 and (neighbors_sum < 2 or neighbors_sum > 3):
        return 0
    else:
        return cell_state
                  
# soma todos os vizinhos de uma celula, excluindo ela propria
def count_neighbors(grid, x, y):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != x and j != y:
                # usa-se o módulo por causa das celulas nas bordas
                col = (x + i + cols) % cols 
                row = (y + j + rows) % rows

                sum += grid[col][row].state
    return sum


if __name__ == '__main__':
    run()
