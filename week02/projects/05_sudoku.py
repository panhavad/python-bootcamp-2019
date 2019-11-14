'''
      NOTED: For most of the case program use use
      		 herizontal_checker and vertical_checker
      		 is enough but for rare 1 or 2 case the section_checker
      		 is used
    
'''

FINISHED_MASSAGE = "Finished"
NOT_FINISHED_MASSAGE = "Not Finished"
BAD_FORMAT_MESSAGE = "Invalid Format"
#In case in future there are more element in SUDOKU
SUDOKU_MATRIX = 9 #Change this value

def sudoku(board):
	"""Main function to return the check status back on the
		passed board

    Args:
      board as a list of list that will be in a sudoku form
    Returns:
      Finished
      Not Finished
      Invalid Format
    """

    # herizontal_checker(board)
    if len(board) == SUDOKU_MATRIX:#formart of whole board
        
        for each_row in board:#format of each row of board
            res = general_format_checker(each_row)
            if res != None:
                return res
            else:
                continue
    else:
        return BAD_FORMAT_MESSAGE


    # vertical_checker(board)
    element_no = 0
    
    while element_no < SUDOKU_MATRIX:
        column_value_list = []
        
        for each_row in board:
            column_value_list.append(each_row[element_no])
        
        element_no += 1
        res = general_format_checker(column_value_list)
        
        if res != None:
            return res
        else:
            continue


    # section_checker(board)
    x_axis, y_axis, times, callers, initial_value = 0,0,0,0,0
    last_round = False
    rows = board #to make our work more readable change board to rows
    section_value_list = list()
    
    while x_axis == times:
        
        #check when the searching process switch to other 3 regions
        if times == SUDOKU_MATRIX and x_axis == SUDOKU_MATRIX and y_axis == 0:
            times, x_axis, callers = 0, 0, 0
            initial_value += 3
            y_axis = initial_value
        elif times == SUDOKU_MATRIX and x_axis == SUDOKU_MATRIX and y_axis == 3:
            times, x_axis, callers, last_round = 0, 0, 0, True
            initial_value += 3
            y_axis = initial_value
        else:
            if last_round:
                break
        
        section_value_list.append(rows[x_axis][y_axis])
        y_axis += 1
        callers += 1
        
        #reexecute the loop when get 3 element already
        if callers == 3:
            callers, y_axis = 0, initial_value
            times += 1
            x_axis += 1
        
        if len(section_value_list) == SUDOKU_MATRIX:
            res = general_format_checker(section_value_list)
            
            if res != None:
                return res
            else:
                continue
            
            section_value_list = []

    return FINISHED_MASSAGE


def general_format_checker(list_values):
	"""Subset function of sudoku to check and find error of
		each list that formed by sudoku function

    Args:
      list of value that form by sudoku function
    Returns:
      None
      Not Finished
      Invalid Format
    """

    if len(list_values) == SUDOKU_MATRIX:
        each_row_unique = to_unique(list_values)
        if len(each_row_unique) == SUDOKU_MATRIX:#format of each component in each row
            
            for each_column in each_row_unique:
                try:
                    each_column = int(each_column)
                except Exception as e:
                    return BAD_FORMAT_MESSAGE
                
                if each_column in range(1, SUDOKU_MATRIX+1):#format of element in column
                    continue
                else:
                    return NOT_FINISHED_MASSAGE
        else:
            return NOT_FINISHED_MASSAGE
    else:
        return BAD_FORMAT_MESSAGE


def to_unique(simple_list):
	"""Subset function to make convertion is more readable
		purpose of this is to find unique value in
		list that form by sudoku function

    Args:
      simple_list that pass in purpose to convert 
    Returns:
      set of the value in passed list
    """
    return set(simple_list)