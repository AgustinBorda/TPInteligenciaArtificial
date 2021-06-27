from Borda_Guevara_Tissera_TP2.resolutions.n_queens import Nqueens
from logic import dpll


def test_n_queens_dpll_4():
    n_queens = Nqueens(4)
    X00, X01, X02, X03,X10, X11, X12, X13, X20, X21, X22, X23, X30, X31, X32, X33 = n_queens.symbols
    model = {X02: False}
    result = dpll(n_queens.clauses, n_queens.symbols, model)
    solution = {
            X00: False, X01: False, X02: True, X03: False,
            X10: True, X11: False, X12: False, X13: False,
            X20: False, X21: False, X22: False, X23: True,
            X30: False, X31: True, X32: False, X33: False
        }
    assert result == solution


def test_n_queens_dpll_8():
    n_queens = Nqueens(8)
    result = dpll(n_queens.clauses, n_queens.symbols, {})
    print(result)
    # solution = {
    #         X00: False, X01: False, X02: True, X03: False,
    #         X10: True, X11: False, X12: False, X13: False,
    #         X20: False, X21: False, X22: False, X23: True,
    #         X30: False, X31: True, X32: False, X33: False
    #     }
    # assert result == solution


def test_n_queens_dpll_10():
    n_queens = Nqueens(10)
    result = dpll(n_queens.clauses, n_queens.symbols, {})
    print(result)
    # solution = {
    #         X00: False, X01: False, X02: True, X03: False,
    #         X10: True, X11: False, X12: False, X13: False,
    #         X20: False, X21: False, X22: False, X23: True,
    #         X30: False, X31: True, X32: False, X33: False
    #     }
    # assert result == solution


def test_n_queens_dpll_12():
    n_queens = Nqueens(12)
    result = dpll(n_queens.clauses, n_queens.symbols, {})
    print(result)
    # solution = {
    #         X00: False, X01: False, X02: True, X03: False,
    #         X10: True, X11: False, X12: False, X13: False,
    #         X20: False, X21: False, X22: False, X23: True,
    #         X30: False, X31: True, X32: False, X33: False
    #     }
    # assert result == solution