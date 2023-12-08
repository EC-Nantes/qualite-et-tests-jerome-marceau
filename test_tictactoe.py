import pytest
import tictactoe

def board1():
    board1 = tictactoe.Board()
    board1.grid = [['o', 'x', 'o'], ['o', 'o', 'x'], ['o', 'x', 'o']]
    return board1

def board2():
    board2 = tictactoe.Board()
    board2.grid = [['x', 'x', 'o'], ['x', 'x', 'x'], ['o', 'o', 'x']]
    return board2

def board3():
    board3 = tictactoe.Board()
    board3.grid = [['x', 'o', 'o'], ['x', 'o', 'o'], ['o', 'x', 'x']]
    return board3

def board4():
    board4 = tictactoe.Board()
    board4.grid = [['x', ' ', 'o'], [' ', 'x', 'o'], [' ', 'o', 'x']]
    return board4

def test_check_column():
    assert board1().check_column(0) == 'o'
    assert board2().check_column(1) == False
    assert board3().check_column(2) == False

def test_check_line():
    assert board1().check_line(0) == False
    assert board2().check_line(1) == 'x'
    assert board3().check_line(2) == False

def test_check_diagonal():
    assert board1().check_diagonal(0) == 'o'
    assert board2().check_diagonal(0) == 'x'
    assert board3().check_diagonal(1) == 'o'

def test_check_win():
    assert board4().check_win() == 'x'