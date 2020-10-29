

"""
returns list of tuples showing the possible positions
"""
from copy import deepcopy

def action(state):
    actions = []
    for col in range(len(state[0])):
        row = len(state)-1
        while row > 0 and state[row][col] != '':
            row -= 1
        if row > 0:
            actions.append((row, col))

    return actions

def result(state, action):
    new_state = deepcopy(state)
    new_state[action[0]][action[1]] = "A"
    return new_state

def terminal(state):
    if win(state) or draw(state):
        return True
    else:
        return False

"""
player = "A" or "H"
"""
def heuristic(state):
    game_score = 0
    visited = set()
    for limit in range(2,0,-1): #discover patterns in limit of 2, 1, 0
        for row in range(len(state)):
            for col in range(len(state[0])):
                if (row, col) not in visited:
                    lists = []
                    list_1_val = []
                    list_1_cord = []
                    lists.append((list_1_val, list_1_cord))

                    list_2_val = []
                    list_2_cord = []
                    lists.append((list_2_val, list_2_cord))

                    list_3_val = []
                    list_3_cord = []
                    lists.append((list_3_val, list_3_cord))

                    list_4_val = []
                    list_4_cord = []
                    lists.append((list_4_val, list_4_cord))

                    for move in range(limit+1): #inclusive limit
                        # move to bottom from center

                        if row+move < len(state) and (row+move, col) not in visited and state[row][col]!='' and (len(list_1_val) == 0 or state[row+move][col] in list_1_val):
                            list_1_val.append(state[row+move][col])
                            list_1_cord.append((row+move, col))

                        #move to top from center

                        if 0<= row - move  and (row - move, col) not in visited and state[row][col] != '' and (
                                len(list_2_val) == 0 or state[row - move][col] in list_2_val):
                            list_2_val.append(state[row-move][col])
                            list_2_cord.append((row - move, col))

                        # move to left from center

                        if 0 <= col - move and (row, col-move) not in visited and state[row][col] != '' and (
                                len(list_3_val) == 0 or state[row][col-move] in list_3_val):
                            list_3_val.append(state[row][col-move])
                            list_3_cord.append((row, col-move))

                        # move to left from center

                        if col + move < len(state[0]) and (row, col+move) not in visited and state[row][col] != '' and (
                                len(list_4_val) == 0 or state[row][col+move] in list_4_val):
                            list_4_val.append(state[row][col+move])
                            list_4_cord.append((row, col+move))

                    #evaluate all lists
                    for (list_val, list_cord) in lists:
                        if len(list_val) == limit+1:
                            game_score+=score(list_val, limit+1)
                            for cordinates in list_cord:
                                visited.add(cordinates)

    return game_score



def score(list_val, size):
    score = 0
    if size == 3:
        if list_val[0] == "A":
            score += 50
        else:
            score -= 50
    elif size == 2:
        if list_val[0] == "A":
            score += 25
        else:
            score -= 25
    elif size == 1:
        if list_val[0] == "A":
            score += 10
        else:
            score -= 10
    return score


def evaluation_function(state):
    if terminal(state):
        if win(state) == "A":
            return 1000      #maximum possible score if AI wins
        elif win(state) == "H":
            return -1000     #minimum possible if human wins
        else:
            if heuristic(state) < 0:
                return -1000
            else:
                return 1000
    else: # game is going we need to evaluate player points
        return heuristic(state)


def win(state):
    for row in range(len(state)):
        for col in range(len(state[0])):
            if (col+2 < len(state[0]) and col-1 >=0): #check connecting dots horizonatlly
                if state[row][col]!='' and state[row][col-1] == state[row][col] == state[row][col+1] == state[row][col+2]:
                    return state[row][col]
            if (row+2 < len(state ) and row-1 >=0): #check connecting dots vertically
                if state[row][col]!='' and state[row-1][col] == state[row][col] == state[row+1][col] == state[row+2][col]:
                    return state[row][col]
            # if (row+2 < len(state) and col+2 < len(state[0]) and  row-1 >=0 and col-1 >=0):
            #     if state[row][col] != '' and state[row-1][col-1] == state[row][col] == \
            #             state[row + 1][col+1] == state[row + 2][col+2]:
            #         return state[row][col]
            # if (row+2 < len(state) and col-2 >= 0 and  row-1 >=0 and col+1 < len(state)):
            #     if state[row][col] != '' and state[row-1][col+1] == state[row][col]== \
            #             state[row + 1][col-1] == state[row + 2][col-2]:
            #         return state[row][col]
    return ''

def draw(state):
    for row in range(len(state)):
        for col in range(len(state[0])):
            if state[row][col] == '':
                return False

    return True
