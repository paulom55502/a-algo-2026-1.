"""
Tic Tac Toe Player — dever-06 (CS50 AI)
Implementação completa com algoritmo Minimax.
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Retorna o estado inicial do tabuleiro.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Retorna qual jogador tem o próximo turno (X ou O).
    X sempre começa. Depois os turnos se alternam.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    # X joga quando as contagens são iguais (ele começa primeiro)
    if x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Retorna um conjunto de todas as ações possíveis (i, j) disponíveis no tabuleiro.
    """
    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Retorna o tabuleiro resultante de aplicar a ação, sem modificar o original.
    """
    i, j = action

    # Valida a ação
    if i not in range(3) or j not in range(3):
        raise Exception("Ação inválida: coordenadas fora do tabuleiro.")
    if board[i][j] != EMPTY:
        raise Exception("Ação inválida: célula já ocupada.")

    # Cria uma cópia profunda para não modificar o tabuleiro original
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)

    return new_board


def winner(board):
    """
    Retorna o vencedor (X ou O) ou None se não houver vencedor ainda.
    """
    # Verifica linhas e colunas
    for i in range(3):
        # Linha i
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
        # Coluna i
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]

    # Diagonal principal (↘)
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]

    # Diagonal secundária (↙)
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Retorna True se o jogo acabou (alguém ganhou ou empate), False caso contrário.
    """
    # Jogo acabou se há um vencedor
    if winner(board) is not None:
        return True

    # Jogo acabou se não há células vazias (empate)
    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    """
    Retorna a utilidade do tabuleiro terminal:
      1  → X ganhou
     -1  → O ganhou
      0  → empate
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Retorna a ação ótima para o jogador atual no tabuleiro.
    Usa poda Alpha-Beta para eficiência.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        # X quer maximizar
        _, best_action = max_value(board, -math.inf, math.inf)
    else:
        # O quer minimizar
        _, best_action = min_value(board, -math.inf, math.inf)

    return best_action


def max_value(board, alpha, beta):
    """
    Retorna (utilidade_máxima, melhor_ação) para o jogador X.
    """
    if terminal(board):
        return utility(board), None

    v = -math.inf
    best_action = None

    for action in actions(board):
        min_val, _ = min_value(result(board, action), alpha, beta)
        if min_val > v:
            v = min_val
            best_action = action
        alpha = max(alpha, v)
        if alpha >= beta:
            break  # poda beta

    return v, best_action


def min_value(board, alpha, beta):
    """
    Retorna (utilidade_mínima, melhor_ação) para o jogador O.
    """
    if terminal(board):
        return utility(board), None

    v = math.inf
    best_action = None

    for action in actions(board):
        max_val, _ = max_value(result(board, action), alpha, beta)
        if max_val < v:
            v = max_val
            best_action = action
        beta = min(beta, v)
        if alpha >= beta:
            break  # poda alpha

    return v, best_action