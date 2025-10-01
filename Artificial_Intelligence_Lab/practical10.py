from math import inf

def alphabeta(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or isinstance(node, int):
        return node

    if maximizingPlayer:
        value = -inf
        for child in node:
            value = max(value, alphabeta(child, depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else:
        value = inf
        for child in node:
            value = min(value, alphabeta(child, depth-1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value


game_tree = [
    [[3, 5], [6, 9]],   
    [[1, 2], [0, -1]]           
]

print("Leaf node values:",game_tree)
print("Optimal value (with Alpha-Beta Pruning):",
      alphabeta(game_tree, 3, -inf, inf, True))

