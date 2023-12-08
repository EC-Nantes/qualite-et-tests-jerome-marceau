import pytest
import tictactoe

def test_board():
    board = tictactoe.Board()
    assert board.check_win() is False
    assert board.new_move(0, 0) is True
    assert board.new_move(0, 0) is False
    assert board.check_win() is False
    assert board.new_move(0, 1) is True
    assert board.new_move(0, 2) is True
    assert board.check_win() == "X"
    assert board.new_move(1, 1) is True
    assert board.new_move(2, 2) is True
    assert board.check_win() == "X"
    assert board.new_move(1, 0) is True
    assert board.new_move(2, 0) is True
    assert board.check_win() == "X"
    assert board.new_move(1, 2) is True
    assert board.check_win() == "X"
    assert board.new_move(2, 1) is True
    assert board.check_win() == "X"
    assert board.new_move(2, 2) is False
    assert board.check_win() == "X"
    assert board.new_move(1, 1) is False
    assert board.check_win() == "X"
    assert board.new_move(0, 0) is False
    assert board.check_win() == "X"
    assert board.new_move(0, 1) is False
    assert board.check_win() == "X"
    assert board.new_move(0, 2) is False
    assert board.check_win() == "X"
    assert board.new_move(1, 0) is False
    assert board.check_win() == "X"
    assert board.new_move(2, 0) is False
    assert board.check_win() == "X"
    assert board.new_move(1, 2) is False
    assert board.check_win() == "X"
    assert board.new_move(2, 1) is False
    assert board.check_win() == "X"
    assert board.new_move(2, 2) is False
    assert board.check_win() == "X"
    assert board.new_move(1, 1) is False
    assert board.check_win() == "X"
    assert board.new_move(0, 0) is False
    assert board.check