# 315535518, 316539196

import mytoolbox


def read_maze(path):
    """
    This functon gets the maze file path and returns the maze data as list of lists
    :param path: A string of the file path.
    :return: list of lists, map information, only for local testing use.
    """
    list_map_data = mytoolbox.csv2list(path, True)
    return list_map_data


def check_start_end_points(maze):
    """
    This functions checks weather there are well-defined Starting and Target points in the maze.
    :param maze: (matrix) List of lists of all the maze information.
    :return: (boolean) True - their are S & T points False otherwise.
    """
    flag_state = [False, False]

    for curr_list in maze:
        for value2 in curr_list:
            if value2 == 'S':
                flag_state[0] = True
            elif value2 == 'T':
                flag_state[1] = True
            else:
                continue
    if flag_state[0] == True & flag_state[1] == True:
        return True
    else:
        return False


def maze_solver_as_a_game(maze):
    """
    Trying to solve the problem as a game with a player that moves in side the maze.
    Thinking about the question differently.
    :param maze: The list of lists of the maze data.
    :return: Bool solvable True | unsolvable False
    """

    char_border = 'X'
    width_maze = len(maze[0])
    maze_real = []

    """Creating a maze with borders"""
    list_hor_blocks = []
    for index in range(0, width_maze + 2):
        list_hor_blocks.append(char_border)

    maze_real.append(list_hor_blocks)

    for value1 in maze:
        list_curr_row = []
        list_curr_row.append(char_border)

        for value2 in value1:
            list_curr_row.append(value2)
        list_curr_row.append(char_border)
        maze_real.append(list_curr_row)

    maze_real.append(list_hor_blocks)
    """Creating a maze with borders"""

    """Finding the starting_location and Target Locations"""
    map_ST_C = {'S': [], 'T': []}

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                map_ST_C['S'].append(j)
                map_ST_C['S'].append(i)
            elif maze[i][j] == 'T':
                map_ST_C['T'].append(j)
                map_ST_C['T'].append(i)

    movement_pot = {'x': map_ST_C['T'][0] - map_ST_C['S'][0],
                    'y': map_ST_C['T'][1] - map_ST_C['S'][1]}

    # - in x  -> length
    # - in y -> down

    player = map_ST_C['S']
    map_of_m_p = {"UP": True,
                  "DOWN": True,
                  "LEFT": True,
                  "RIGHT": True}

    # for player 1 == y
    # for player 0 == x

    checker_x = 0
    checker_y = 0
    while player != map_ST_C['T']:
        # potential - left movement
        if movement_pot['x'] < 0:
            while player[0] - map_ST_C['T'][0] > 0:
                checker_x = player[0] - 1
                if maze[checker_y][checker_x] != char_border:
                    player[0] = checker_x
                else:
                    # up movement potential
                    if player[1] - map_ST_C['T'][1] > 0:
                        checker_y = player[1] - 1
                        if maze[checker_y][checker_x] != char_border:
                            player[1] = checker_y

                    # down movement potential
                    elif player[1] - map_ST_C['T'][1] < 0:
                        checker_y = player[1] + 1
                        if maze[checker_y][checker_x] != char_border:
                            player[1] = checker_y

        # potential - right movement
        elif movement_pot['y'] > 0:
            while player[0] - map_ST_C['T'][0] < 0:
                checker_x = player[0] + 1
                if maze[checker_y][checker_x] != char_border:
                    player[0] = checker_x
                else:
                    # up movement potential
                    if player[1] - map_ST_C['T'][1] > 0:
                        checker_y = player[1] - 1
                        if maze[checker_y][checker_x] != char_border:
                            player[1] = checker_y

                    # down movement potential
                    elif player[1] - map_ST_C['T'][1] < 0:
                        checker_y = player[1] + 1
                        if maze[checker_y][checker_x] != char_border:
                            player[1] = checker_y

    if player == map_ST_C['T']:
        print("SOLVED")
    else:
        print("NOT SOLVED")

def maze_solver(maze):
    """
    This is the main function.
    First this function finds the starting_locationing point of the maze [S] point.
    Secondly it uses the recursive algorithm to check if the maze is solvable.
    :param maze: all the maze information saved in a lists of lists given by mytoolbox.csv2list function.
    :return: boolean True for solvable False for unsolvable
    """

    """ 
        Finding the starting_location and Target Locations.
    """

    map_ST_C = {'S': [], 'T': []}

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                map_ST_C['S'].append(i) # j is the X axes  movement in columns
                map_ST_C['S'].append(j) # i is the X axes  movement in columns
            elif maze[i][j] == 'T':
                map_ST_C['T'].append(j)
                map_ST_C['T'].append(i)

    starting_location = map_ST_C['S']
    movement_history = []

    is_maze_solvable = recursive_maze_solver(maze, starting_location, movement_history)

    return is_maze_solvable


def recursive_maze_solver(maze, location, movement_history):
    """
    This function takes a different approach then the way of thought presented in the maze_solver_as_a_game.
    This functions goal is to check weather there is a valid path from location S to T in the maze.
    A valid path is a path that is not through blocks and stays with in the boundaries of the maze.
    :param maze: (matrix) List of lists of all the maze information.
    :param location: (list) A list of 2 values representing the place of the s.  y index
    :param movement_history: (list) A memorization list to help optimize the creation of a valid path.
    :return: (boolean) True if the algorithm found a valid path | False if there is no valid path.
    """
    if location[0] < 0 or location[1] < 0:
        return False
    if location[0] > len(maze) - 1 or location[1] > len(maze[location[0]]) - 1:
        return False
    # checking that the path is not going back on itself.
    if location in movement_history:
        return False
    # checking that the path is not through blocks.
    if maze[location[0]][location[1]] == 'X':
        return False
    if maze[location[0]][location[1]] == 'T':
        return True

    # At the first cycle it adds the S point to the history list
    movement_history.append(location)

    # Using a map of readability
    potential_movement = {"UP": [location[0] + 1, location[1]],
                          "DOWN": [location[0] - 1, location[1]],
                          "LEFT": [location[0], location[1] - 1],
                          "RIGHT":  [location[0], location[1] + 1]}

    # running all the different movements possible using or logic to determine a possible movement in the maze.
    return recursive_maze_solver(maze, potential_movement["RIGHT"], movement_history) or \
        recursive_maze_solver(maze, potential_movement["LEFT"], movement_history) or \
        recursive_maze_solver(maze, potential_movement["UP"], movement_history) or \
        recursive_maze_solver(maze, potential_movement["DOWN"], movement_history)

# Used for tests
if __name__ == "__main__":

    maze = read_maze("maze_example.csv")
    print(maze_solver(maze))
