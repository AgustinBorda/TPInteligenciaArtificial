from logic import *


def get_board(n):
    board = list()
    start = 0
    end = n
    for i in range(start, end):
        row = list()
        for j in range(start, end):
            row.append('X{}_{}'.format(i, j))
        board.append(row)
    return board


def get_symbols(board):
    return expr(', '.join([item for row in board for item in row]))


def get_clauses(board):
    clauses = set()
    n = len(board)
    cols = [[] for _ in range(n)]
    rows = [[] for _ in range(n)]
    fdiag = [[] for _ in range(2 * n - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -n + 1

    for j in range(n):
        for i in range(n):
            cols[j].append(board[i][j])
            rows[i].append(board[i][j])
            fdiag[j + i].append(board[i][j])
            bdiag[j - i - min_bdiag].append(board[i][j])

    [clauses.add(' | '.join(row)) for row in rows]
    [clauses.add(' | '.join(col)) for col in cols]

    for row in rows:
        for i in range(n):
            for j in range(i + 1, n):
                clauses.add('~{} | ~{}'.format(row[i], row[j]))

    for col in cols:
        for i in range(n):
            for j in range(i + 1, n):
                clauses.add('~{} | ~{}'.format(col[i], col[j]))

    for diag in fdiag:
        for i in range(len(diag)):
            for j in range(i + 1, len(diag)):
                clauses.add('~{} | ~{}'.format(diag[i], diag[j]))

    for diag in bdiag:
        for i in range(len(diag)):
            for j in range(i + 1, len(diag)):
                clauses.add('~{} | ~{}'.format(diag[i], diag[j]))

    return tuple(expr(clause) for clause in clauses)


def get_kb(clauses):
    kb = PropKB()
    for clause in clauses:
        kb.tell(clause)
    return kb


def tt_entails(kb):
    symbols = list(prop_symbols(kb))
    return tt_check_all(kb, symbols, {})


def tt_check_all(kb, symbols, model):
    if not symbols:
        if pl_true(kb, model):
            return model
        else:
            return None
    else:
        P, rest = symbols[0], symbols[1:]
        res_0 = tt_check_all(kb, rest, extend(model, P, True))
        if res_0:
            return res_0
        res_1 = tt_check_all(kb, rest, extend(model, P, False))
        if res_1:
            return res_1
        return None


class Nqueens:
    def __init__(self, n):
        self.board = get_board(n)
        self.symbols = get_symbols(self.board)
        self.clauses = get_clauses(self.board)
        self.kb = get_kb(self.clauses)
