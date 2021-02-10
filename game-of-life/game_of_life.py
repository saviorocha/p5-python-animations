import numpy as np
from p5 import *
import random

"""
    Baseado no código de Daniel Shiffman
    https://www.youtube.com/watch?v=FWSR_7kZuYg
"""

resolution = 20
width = 400
height = 400
cols = width // resolution
rows = height // resolution

def make_matrix(cols, rows):
    matrix = np.zeros( (cols, rows) )
    for i in range(cols):
        for j in range(rows):
            matrix[i][j] = random.randint(0, 1)
    return matrix
current_grid = make_matrix(cols, rows)

def setup():
    size(400, 400)

def draw():
    global current_grid, cols, rows
    
    next_grid = np.zeros( (cols, rows) )
    background(0)
    
    # desenha o grid
    for i in range(cols):
        for j in range(rows):
            x = i * resolution
            y = j * resolution
            if current_grid[i][j] == 1:
                fill(255)
                rect((x, y), resolution, resolution)
                # circle((x, y), resolution)

            next_grid[i][j] = calculate_new_grid(current_grid, i, j)
            
    # atualiza o grid para próxima iteração
    current_grid = next_grid

# cria o grid do estado seguinte
def calculate_new_grid(current_grid, i, j):
    cell_state = current_grid[i][j]
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
                col = (x + i + cols) % cols # (0 - 1 + 10) % 10 = 9
                row = (y + j + rows) % rows

                sum += grid[col][row]
    return sum

if __name__ == '__main__':
    run()
