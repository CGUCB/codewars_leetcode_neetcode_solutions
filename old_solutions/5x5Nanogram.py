######################
#5x5 Nanogram Solver #
######################

import itertools
def complete_permutations(clue): #gets all clue possibilities according to a clue
    clue_w_zeros, results = [], []
    for element in clue: 
        clue_w_zeros += [1] * element + [0]
    clue_w_zeros = clue_w_zeros[:-1]
    for i in range(6 - len(clue_w_zeros)):
        results.append([0] * i + clue_w_zeros + [0] * (5 - len(clue_w_zeros) - i))
    if len(clue) == 2: #account for two 0 spaces in middle of clue
        extra_mid_zero = clue_w_zeros[:clue[0]] + [0] + clue_w_zeros[clue[0]:]
        for i in range(6 - len(extra_mid_zero)):
            results.append([0] * i + extra_mid_zero + [0] * (5 - len(extra_mid_zero) - i))
    if len(clue) == 2 and sum(clue) == 2: #account for three zero spaces in middle of pre_permutations
        extra_extra_mid_zero = clue_w_zeros[:clue[0]] + [0, 0] + clue_w_zeros[clue[0]:]
        for i in range(6 - len(extra_extra_mid_zero)):
            results.append([0] * i + extra_extra_mid_zero + [0] * (5 - len(extra_extra_mid_zero) - i))
    return results

def all_permutations(clue): #gets ALL permutations of clue (including those with numbers less than)
    all_clues, results = [[i] for i in range(1,max(clue)+1)], [[0,0,0,0,0]]
    if len(clue) == 1:
        for single_clue in all_clues:
            results.extend(complete_permutations(single_clue))
        return results
    else:
        pre_permutations = []
        for num in clue:
            pre_permutations.append([i for i in range(1,num+1)])
        all_combos = list(itertools.product(*pre_permutations))
        [results.extend(complete_permutations(single)) for single in all_combos]
        [results.extend(complete_permutations(single)) for single in all_clues]
        if len(clue) == 3:
            for value in all_permutations([1,1]):
                if value not in results:
                    results.append(value)
        return results

def test_col(board, array_of_col_perms): #tests if all columns of a board obey by the horiz clues
    col_as_rows = list(zip(*board))
    for i in range(len(col_as_rows)):
        if list(col_as_rows[i]) not in list(array_of_col_perms[i]):
            return False
    return True

def solve(clues):
    h_clues, v_clues = clues[0], clues[1] #divides the clues into horiz and vert clues
    result_arr = [[0] * len(h_clues) for _ in v_clues] #creates a blank matrix that will be populated with answers
    h_clue_perms = [all_permutations(clu) for clu in h_clues] #a list that has all permutatations of every column according to clues
    def solve_helper(row_index):
        if test_col(result_arr, h_clue_perms):
            if row_index == 5: 
                return True
            v_clue_perms = complete_permutations(v_clues[row_index])
            for perm in v_clue_perms:
                previous_row = result_arr[row_index]
                result_arr[row_index] = perm
                if solve_helper(row_index+1):
                    return True
                result_arr[row_index] = previous_row
        else:
            return False
    if solve_helper(0):
        return result_arr
        