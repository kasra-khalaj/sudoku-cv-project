"""
Phase 3: Sudoku Solver

This module implements a backtracking algorithm to solve a standard 9x9 Sudoku puzzle.
The algorithm includes validation logic for standard Sudoku constraints (rows, columns,
and 3x3 blocks).

Attribution/Licensing:
While this implementation is written from scratch for this project, it draws inspiration
from standard educational backtracking algorithms, such as those found in:
- Norvig's Sudoku Solver / AIMA Python (https://github.com/aimacode/aima-python)
- LiorSinai SudokuSolver-Python (https://github.com/LiorSinai/SudokuSolver-Python)
"""

import numpy as np
from typing import List, Union, Tuple, Optional

def is_valid_board(board: Union[List[List[int]], np.ndarray]) -> bool:
    """
    Checks if the initial board configuration is valid (no conflicting non-zero numbers
    and all numbers in the valid range 0-9).
    """
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    blocks = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val < 0 or val > 9:
                return False
            if val != 0:
                block_idx = (r // 3) * 3 + (c // 3)
                if val in rows[r] or val in cols[c] or val in blocks[block_idx]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                blocks[block_idx].add(val)
    return True

def is_safe(board: List[List[int]], row: int, col: int, num: int) -> bool:
    """
    Checks if placing `num` at `board[row][col]` is safe.
    """
    # Check row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check 3x3 block
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def find_empty_location(board: List[List[int]]) -> Optional[Tuple[int, int]]:
    """
    Finds an empty space on the board (represented by 0).
    Returns (row, col) or None if the board is full.
    """
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None

def solve_backtracking(board: List[List[int]]) -> bool:
    """
    Solves the Sudoku board using backtracking in place.
    """
    empty_loc = find_empty_location(board)
    if not empty_loc:
        return True # Puzzle is solved

    row, col = empty_loc

    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num

            if solve_backtracking(board):
                return True

            # Backtrack
            board[row][col] = 0

    return False

def solve_sudoku(board: Union[List[List[int]], np.ndarray]) -> Tuple[bool, Optional[Union[List[List[int]], np.ndarray]]]:
    """
    Solves a 9x9 Sudoku board.

    Args:
        board: 9x9 nested list or NumPy array representing the Sudoku puzzle. Empty cells are 0.

    Returns:
        A tuple (success, solved_board). If unsolvable or initially invalid, returns (False, None).
    """
    # Ensure it's a 9x9 structure
    if len(board) != 9 or any(len(row) != 9 for row in board):
        return False, None

    # Handle NumPy arrays gracefully
    is_numpy = isinstance(board, np.ndarray)

    # Create a deep copy to work on
    if is_numpy:
        working_board = board.tolist()
    else:
        working_board = [row[:] for row in board]

    # Check if initially valid
    if not is_valid_board(working_board):
        return False, None

    # Solve
    success = solve_backtracking(working_board)

    if not success:
        return False, None

    if is_numpy:
        return True, np.array(working_board)
    else:
        return True, working_board
