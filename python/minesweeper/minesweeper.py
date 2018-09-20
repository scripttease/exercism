def board(input_board_array):
    # Function body starts here
    if len(set(map(len, input_board_array))) not in (0,1):
        raise ValueError('not all board rows have same length!')
