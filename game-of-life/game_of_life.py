from cell import Cell
from p5 import *
import numpy as np
import random
import copy

"""
    Baseado no código de Daniel Shiffman
    https://www.youtube.com/watch?v=FWSR_7kZuYg
"""

running = False
resolution = 20
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
current_grid = make_matrix(cols, rows)
next_grid = make_matrix(cols, rows)

def setup():
    size(400, 500)

def draw():
    global current_grid, next_grid, cols, rows, running
    ubuntu_font = load_font('./fonts/ubuntu.regular.ttf')
    text_font(ubuntu_font)
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
            if running:
                next_grid[i][j].state = calculate_new_grid(current_grid, i, j)
 
    if running:    
        # atualiza o grid para próxima iteração
        current_grid = copy.deepcopy(next_grid)
    text_size(16)
    fill(50)
    rect((0, 400), 400, 100)
    fill(255)
    text('Left click to add new cells and right click to remove cells', (0, 400))
    text('Press "r" to toggle the animation', (0, 423))
    text('Have fun :)', (0, 445))

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
            # usa-se o módulo por causa das celulas nas bordas
            # para que contabilize a celula da outra extremidade
            col = (x + i + cols) % cols 
            row = (y + j + rows) % rows

            sum += grid[col][row].state
    sum -= grid[x][y].state
    return sum

def mouse_pressed():
    i = mouse_x // resolution
    j = mouse_y // resolution
    try:
        cell_to_change = current_grid[i][j]
        if mouse_button == 'LEFT':
            cell_to_change.state = 1
        elif mouse_button == 'RIGHT':
            cell_to_change.state = 0
    except IndexError:
        pass

def key_pressed():
    global running
    if key == 'R' or key == 'r':
        running = not running

if __name__ == '__main__':
    run()
