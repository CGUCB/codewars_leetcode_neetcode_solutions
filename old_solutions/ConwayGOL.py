def remove_empty_cells(cell_rem):
    """
    Removes all empty rows and columns from the cell_rem 2D matrix
    """
    while True: #This and below deals with empty top/bottom lines
        if sum(cell_rem[0]) == 0:
            cell_rem = cell_rem[1:]
        elif sum(cell_rem[0]) > 0:
            break
    while True:
        if sum(cell_rem[-1]) == 0:
            cell_rem = cell_rem[:-1]
        elif sum(cell_rem[-1]) > 0:
            break

    summed_cells, start, finish, sval, fval = [sum(x) for x in zip(*cell_rem)], 0, 0, False, False
    for i in range(len(summed_cells)):
        if not sval and summed_cells[i] > 0:
            start, sval = i, True
        if not fval and summed_cells[-i] > 0:
            finish, fval = -i, True
    if finish != 0:
        for r_index in range(len(cell_rem)):
            cell_rem[r_index] = cell_rem[r_index][start:finish+1]
    return cell_rem

def insert_whitespace(cell_ins):
    """
    Inserts a layer of 0s around the "cells" 2D matrix
    """
    cell_ins = [[0] * len(cell_ins[0])] + cell_ins + [[0] * len(cell_ins[0])] #Adds bottom and top empty rows
    for i in range(len(cell_ins)): #Adds left and right side empty rows
        cell_ins[i] = [0] + cell_ins[i] + [0]
    return cell_ins

def surr_sum(cells,row1,col1): #calc number of live cells around target cell
    eight_surrounding_sum = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if row1 + i >= 0 and col1 + j >= 0 and row1 + i < len(cells) and col1 + j < len(cells[0]):
                eight_surrounding_sum += cells[row1 + i][col1 + j]
    return eight_surrounding_sum if not cells[row1][col1] else eight_surrounding_sum - 1

def get_generation(cells, generations):
    if generations == 0: #if all generations gone through, returns resulting cells
        return remove_empty_cells(cells)
    cells = insert_whitespace(cells)
    new_cells = [[0] * len(cells[0]) for _ in range(len(cells))]
    for row in range(len(cells)):
        for col in range(len(cells[0])):
            surr_summed = surr_sum(cells,row,col)
            if cells[row][col] and surr_summed in [2,3]:
                new_cells[row][col] = 1
            elif not cells[row][col] and surr_summed == 3:
                new_cells[row][col] = 1
    return get_generation(new_cells, generations - 1)

