import numpy as np
from p5 import *
import random

"""
    Baseado no código de Daniel Shiffman
    https://www.youtube.com/watch?v=FWSR_7kZuYg
"""

def makeMatrix(cols, rows):
    matrix = np.zeros( (cols, rows) )
    for i in range(cols):
        for j in range(rows):
            matrix[i][j] = random.randint(0, 1)
    return matrix

resolution = 40
width = 400
height = 400
cols = width // resolution
rows = height // resolution
current_grid = makeMatrix(cols, rows)

def setup():
    size(400, 400)

def draw():
    global current_grid, cols, rows
    
    background(0)
    
    # desenha o grid pela primeira vez
    for i in range(cols):
        for j in range(rows):
            x = i * resolution
            y = j * resolution
            if current_grid[i][j] == 1:
                fill(255)
                rect((x, y), resolution, resolution)
                # circle((x, y), resolution)

    # desenha o grid do estado seguinte
    next_grid = makeMatrix(cols, rows)

    for i in range(cols):
        for j in range(rows):
            
            state = current_grid[i][j]
            neighbors_sum = count_neighbors(current_grid, i, j)

            # regras do jogo da vida
            if state == 0 and neighbors_sum == 3:
                next_grid[i][j] = 1
            elif state == 1 and (neighbors_sum < 2 or neighbors_sum > 3):
                next_grid[i][j] = 0
            else:
                next_grid[i][j] = state
    
    # atualiza o grid para próxima iteração
    current_grid = next_grid
            
# soma todos os vizinhos de uma celula, excluindo ela propria
def count_neighbors(grid, x, y):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            # usa-se o módulo por causa das celulas nas bordas
            col = (x + i + cols) % cols
            row = (y + j + rows) % rows

            sum += grid[col][row]
    sum -= grid[x][y]
    return sum

if __name__ == '__main__':
    run()
