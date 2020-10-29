import AIEnvironment


#test the heuristic functions
state = [['', 'H', '', 'H', '', ''],
         ['', 'A', 'A', 'A', '', ''],
         ['', 'H', 'A', 'H', '', ''],
         ['', 'H', 'H', 'A', '', ''],
         ['', 'H', 'H', 'H', '', ''],
         ['', 'A', 'H', 'A', '', ''],]

H_win_state =    [['','H', '', 'H', '', ''],
                 ['', 'A', 'A', 'A', '', ''],
                 ['', 'H', 'H', 'H', '', ''],
                 ['', 'H', 'H', 'A', '', ''],
                 ['', 'H', 'H', 'H', '', ''],
                 ['', 'A', 'H', 'A', '', ''],]

A_win_state_1 = [['', 'H', '', 'H', '', ''],
             ['', 'H', 'A', 'A', '', ''],
             ['', 'A', 'A', 'H', '', ''],
             ['', 'A', 'H', 'A', '', ''],
             ['', 'A', 'H', 'H', '', ''],
             ['', 'A', 'H', 'A', '', ''],]

draw = [['A', 'H', 'A', 'H', 'A', 'A'],
             ['A', 'H', 'A', 'A', '', ''],
             ['', 'A', 'A', 'H', '', ''],
             ['', 'H', 'H', 'A', '', ''],
             ['', 'A', 'A', 'H', '', ''],
             ['', 'A', 'H', 'A', '', ''],]

print("Human Wins ==  %s"%(AIEnvironment.win(H_win_state)))
print("AI Wins ==  %s"%(AIEnvironment.win(A_win_state_1)))
print("Not Terminated:%s"%(AIEnvironment.terminal(draw)))


print(AIEnvironment.heuristic(H_win_state))
print(AIEnvironment.heuristic(A_win_state_1))
print(AIEnvironment.heuristic(state))