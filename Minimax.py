import AIEnvironment
class Minimax:

    def __init__(self, depth):
        self.depth = depth

    def minimax(self, curr_depth, max_turn, state, alpha = -float('inf'), beta=float('inf')):
        if curr_depth == self.depth or AIEnvironment.terminal(state):
            return AIEnvironment.evaluation_function(state), ""

        best_val = float('inf') if not max_turn else -float('inf')
        list_actions = AIEnvironment.action(state)
        for action in list_actions:
            new_state = AIEnvironment.result(state, action)
            eval_val, eval_action = self.minimax(curr_depth+1, not max_turn, new_state)
            if max_turn and best_val < eval_val:
                best_val = eval_val
                best_action = action
                alpha = max(alpha, eval_val)
                if beta <= alpha:
                    break

            if not max_turn and best_val > eval_val:
                best_val = eval_val
                best_action = action
                beta = min(beta, eval_val)
                if beta <= alpha:
                    break

        return best_val, best_action


