from Borda_Guevara_Tissera_TP2.resolutions.n_queens import Nqueens, tt_entails
from logic import dpll, Expr, pl_true


# DPLL
def test_n_queens_dpll_4():
    n_queens = Nqueens(4)
    X00, X01, X02, X03, \
    X10, X11, X12, X13, \
    X20, X21, X22, X23, \
    X30, X31, X32, X33 = n_queens.symbols
    result = dpll(n_queens.clauses, n_queens.symbols, {})
    solution = {
        X00: False, X01: True,  X02: False, X03: False,
        X10: False, X11: False, X12: False, X13: True,
        X20: True,  X21: False, X22: False, X23: False,
        X30: False, X31: False, X32: True,  X33: False
    }
    assert result == solution


def test_n_queens_dpll_8():
    n_queens = Nqueens(8)
    X00, X01, X02, X03, X04, X05, X06, X07, \
    X10, X11, X12, X13, X14, X15, X16, X17, \
    X20, X21, X22, X23, X24, X25, X26, X27, \
    X30, X31, X32, X33, X34, X35, X36, X37, \
    X40, X41, X42, X43, X44, X45, X46, X47, \
    X50, X51, X52, X53, X54, X55, X56, X57, \
    X60, X61, X62, X63, X64, X65, X66, X67, \
    X70, X71, X72, X73, X74, X75, X76, X77 = n_queens.symbols

    result = dpll(n_queens.clauses, n_queens.symbols, {})
    solution = {
        X00: True,  X01: False, X02: False, X03: False, X04: False, X05: False, X06: False, X07: False,
        X10: False, X11: False, X12: False, X13: False, X14: True,  X15: False, X16: False, X17: False,
        X20: False, X21: False, X22: False, X23: False, X24: False, X25: False, X26: False, X27: True,
        X30: False, X31: False, X32: False, X33: False, X34: False, X35: True,  X36: False, X37: False,
        X40: False, X41: False, X42: True,  X43: False, X44: False, X45: False, X46: False, X47: False,
        X50: False, X51: False, X52: False, X53: False, X54: False, X55: False, X56: True,  X57: False,
        X60: False, X61: True,  X62: False, X63: False, X64: False, X65: False, X66: False, X67: False,
        X70: False, X71: False, X72: False, X73: True,  X74: False, X75: False, X76: False, X77: False,
    }
    assert result == solution


def test_n_queens_dpll_10():
    n_queens = Nqueens(10)
    X00, X01, X02, X03, X04, X05, X06, X07, X08, X09, \
    X10, X11, X12, X13, X14, X15, X16, X17, X18, X19, \
    X20, X21, X22, X23, X24, X25, X26, X27, X28, X29, \
    X30, X31, X32, X33, X34, X35, X36, X37, X38, X39, \
    X40, X41, X42, X43, X44, X45, X46, X47, X48, X49, \
    X50, X51, X52, X53, X54, X55, X56, X57, X58, X59, \
    X60, X61, X62, X63, X64, X65, X66, X67, X68, X69, \
    X70, X71, X72, X73, X74, X75, X76, X77, X78, X79, \
    X80, X81, X82, X83, X84, X85, X86, X87, X88, X89, \
    X90, X91, X92, X93, X94, X95, X96, X97, X98, X99 = n_queens.symbols

    result = dpll(n_queens.clauses, n_queens.symbols, {})
    solution = {
        X00: True,  X01: False, X02: False, X03: False, X04: False, X05: False, X06: False, X07: False, X08: False, X09: False,
        X10: False, X11: False, X12: True,  X13: False, X14: False, X15: False, X16: False, X17: False, X18: False, X19: False,
        X20: False, X21: False, X22: False, X23: False, X24: False, X25: True,  X26: False, X27: False, X28: False, X29: False,
        X30: False, X31: False, X32: False, X33: False, X34: False, X35: False, X36: False, X37: True,  X38: False, X39: False,
        X40: False, X41: False, X42: False, X43: False, X44: False, X45: False, X46: False, X47: False, X48: False, X49: True,
        X50: False, X51: False, X52: False, X53: False, X54: True,  X55: False, X56: False, X57: False, X58: False, X59: False,
        X60: False, X61: False, X62: False, X63: False, X64: False, X65: False, X66: False, X67: False, X68: True,  X69: False,
        X70: False, X71: True,  X72: False, X73: False, X74: False, X75: False, X76: False, X77: False, X78: False, X79: False,
        X80: False, X81: False, X82: False, X83: True,  X84: False, X85: False, X86: False, X87: False, X88: False, X89: False,
        X90: False, X91: False, X92: False, X93: False, X94: False, X95: False, X96: True,  X97: False, X98: False, X99: False,
    }
    assert result == solution


def test_n_queens_dpll_12():
    n_queens = Nqueens(12)
    X00,  X01,  X02,  X03,  X04,  X05,  X06,  X07,  X08,  X09,  X010,  X011,  \
    X10,  X11,  X12,  X13,  X14,  X15,  X16,  X17,  X18,  X19,  X1_10, X1_11,  \
    X20,  X21,  X22,  X23,  X24,  X25,  X26,  X27,  X28,  X29,  X210,  X211,  \
    X30,  X31,  X32,  X33,  X34,  X35,  X36,  X37,  X38,  X39,  X310,  X311,  \
    X40,  X41,  X42,  X43,  X44,  X45,  X46,  X47,  X48,  X49,  X410,  X411,  \
    X50,  X51,  X52,  X53,  X54,  X55,  X56,  X57,  X58,  X59,  X510,  X511,  \
    X60,  X61,  X62,  X63,  X64,  X65,  X66,  X67,  X68,  X69,  X610,  X611,  \
    X70,  X71,  X72,  X73,  X74,  X75,  X76,  X77,  X78,  X79,  X710,  X711,  \
    X80,  X81,  X82,  X83,  X84,  X85,  X86,  X87,  X88,  X89,  X810,  X811,  \
    X90,  X91,  X92,  X93,  X94,  X95,  X96,  X97,  X98,  X99,  X910,  X911,  \
    X100, X101, X102, X103, X104, X105, X106, X107, X108, X109, X1010, X1011, \
    X110, X111, X112, X113, X114, X115, X116, X117, X118, X119, X1110, X1111, = n_queens.symbols

    result = dpll(n_queens.clauses, n_queens.symbols, {})
    solution = {
        X00: True,   X01: False,  X02: False,  X03: False,  X04: False,  X05: False,  X06: False,   X07: False,  X08: False,  X09: False,  X010: False,  X011: False,
        X10: False,  X11: False,  X12: True,   X13: False,  X14: False,  X15: False,  X16: False,   X17: False,  X18: False,  X19: False,  X1_10: False, X1_11: False,
        X20: False,  X21: False,  X22: False,  X23: False,  X24: True,   X25: False,  X26: False,   X27: False,  X28: False,  X29: False,  X210: False,  X211: False,
        X30: False,  X31: False,  X32: False,  X33: False,  X34: False,  X35: False,  X36: False,   X37: True,   X38: False,  X39: False,  X310: False,  X311: False,
        X40: False,  X41: False,  X42: False,  X43: False,  X44: False,  X45: False,  X46: False,   X47: False,  X48: False,  X49: True,   X410: False,  X411: False,
        X50: False,  X51: False,  X52: False,  X53: False,  X54: False,  X55: False,  X56: False,   X57: False,  X58: False,  X59: False,  X510: False,  X511: True,
        X60: False,  X61: False,  X62: False,  X63: False,  X64: False,  X65: True,   X66: False,   X67: False,  X68: False,  X69: False,  X610: False,  X611: False,
        X70: False,  X71: False,  X72: False,  X73: False,  X74: False,  X75: False,  X76: False,   X77: False,  X78: False,  X79: False,  X710: True,   X711: False,
        X80: False,  X81: True,   X82: False,  X83: False,  X84: False,  X85: False,  X86: False,   X87: False,  X88: False,  X89: False,  X810: False,  X811: False,
        X90: False,  X91: False,  X92: False,  X93: False,  X94: False,  X95: False,  X96: True,    X97: False,  X98: False,  X99: False,  X910: False,  X911: False,
        X100: False, X101: False, X102: False, X103: False, X104: False, X105: False, X106: False,  X107: False, X108: True,  X109: False, X1010: False, X1011: False,
        X110: False, X111: False, X112: False, X113: True,  X114: False, X115: False, X116: False,  X117: False, X118: False, X119: False, X1110: False, X1111: False
    }
    assert result == solution


# Enumeracion de modelos
def test_n_queens_tte_4():
    n_queens = Nqueens(4)
    X00, X01, X02, X03, \
    X10, X11, X12, X13, \
    X20, X21, X22, X23, \
    X30, X31, X32, X33 = n_queens.symbols

    result = tt_entails(Expr('&', *n_queens.kb.clauses))
    solution = {
        X00: False, X01: True,  X02: False, X03: False,
        X10: False, X11: False, X12: False, X13: True,
        X20: True,  X21: False, X22: False, X23: False,
        X30: False, X31: False, X32: True,  X33: False
    }
    assert result == solution


# Resuelve en 2.5 minutes
def test_n_queens_tte_5():
    n_queens = Nqueens(5)
    X00, X01, X02, X03, X04, \
    X10, X11, X12, X13, X14, \
    X20, X21, X22, X23, X24, \
    X30, X31, X32, X33, X34, \
    X40, X41, X42, X43, X44 = n_queens.symbols

    result = tt_entails(Expr('&', *n_queens.kb.clauses))
    solution_0 = {
        X00: False, X01: True, X02: False, X03: False, X04: False,
        X10: False, X11: False, X12: False, X13: True, X14: False,
        X20: True, X21: False, X22: False, X23: False, X24: False,
        X30: False, X31: False, X32: True, X33: False, X34: False,
        X40: False, X41: False, X42: False, X43: False, X44: True
    }
    assert result == solution_0
