# fn designed to take a board and return the mine hints
def board(input_board_array):
    if input_board_array == []:
        return []
    # mapping each item in board array to its length
    # resulting length of that set (if all same) is 1 or 0 if no items
    if len(set(map(len, input_board_array))) not in (0,1):
        raise ValueError('not all board rows have same length!')
    # length of first item in list (ie first row length)
    numcols_rowlen = len(input_board_array[0])
    # number of rows
    numrows_collen = len(input_board_array)
    # makes input into nested list
    nested_input = [list(i) for i in input_board_array]
    # count the mines in a range from just before to just after current i in list
    # for i in range rowlen: mines = list_input[current_row][i-1:i+2]
    # nb the above will fail when i is out of range. (ie over row length) 
    # low_bound = max(0, current_cell -1): high_bound doesn't matter??
    for current_row in range(numrows_collen):
        for current_cell in range(numcols_rowlen):
            # original input must be nil, space or *
            if nested_input[current_row][current_cell] not in ('',' ', '*'):
                raise ValueError('invalid board')
            # if statement says only do the else if its ' '
            if nested_input[current_row][current_cell] != ' ':
                continue
            else:
                lower_bound = max(current_cell -1 ,0)
                # counts mines on same row
                mines = nested_input[current_row][lower_bound:current_cell+2].count('*')

                if current_row > 0:
                    mines += nested_input[current_row -1 ][lower_bound:current_cell+2].count('*')
                if current_row < numrows_collen -1:
                    mines += nested_input[current_row + 1 ][lower_bound:current_cell+2].count('*')

                # don't write in 0s or overwrite mines
                if mines != 0 and current_cell != '*':
                    nested_input[current_row][current_cell] = str(mines)
                else:
                    continue
    # un-nests the list
    return ["".join(lst) for lst in nested_input]
