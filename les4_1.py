import typing
"""
прописать функцию, которая определяет по заданным координатам королевы и пешки, может ли королева побить пешку
"""

def is_queen_gambit(queen: typing.Tuple[int, int], pawn: typing.Tuple[int, int]):
    return queen[0] == pawn[0] or queen[1] == pawn[1] or (abs(queen[0] - pawn[0]) == abs(queen[1] - pawn[1]))


