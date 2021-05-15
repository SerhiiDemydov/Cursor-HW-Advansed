import pytest
from game import TicTacToe

import HtmlTestRunner
import xmlrunner


def setup_module(module):
    global test_game
    test_game = TicTacToe()


def test_winner_row():
    print("\ntest_winner_row - 1")
    test_game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
    test_game.print_board()
    assert (test_game.winner(2, 'X'))
    print("\ntest_winner_row - 2")
    test_game.board = [' ', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' ']
    test_game.print_board()
    assert (test_game.winner(5, 'X'))
    print("\ntest_winner_row - 2")
    test_game.board = [' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X']
    test_game.print_board()
    assert (test_game.winner(8, 'X'))


def test_winner_colum():
    print("\ntest_winner_colum - 1")
    test_game.board = ['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ']
    test_game.print_board()
    assert (test_game.winner(0, 'X'))
    print("\ntest_winner_colum - 2")
    test_game.board = [' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X', ' ']
    test_game.print_board()
    assert (test_game.winner(1, 'X'))
    print("\ntest_winner_colum - 3")
    test_game.board = [' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X']
    test_game.print_board()
    assert (test_game.winner(2, 'X'))


def test_winner_diagonal1():
    print("\ntest_winner_diagonal1")
    test_game.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
    test_game.print_board()
    assert (test_game.winner(0, 'X'))


def test_winner_diagonal2():
    print("\ntest_winner_diagonal2")
    test_game.board = [' ', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' ']
    test_game.print_board()
    assert (test_game.winner(2, 'X'))


def test_winne_not_won():
    print("\ntest_winne_not_won - 1")
    test_game.board = ['X', 'O', 'X', ' ', ' ', ' ', 'X', ' ', ' ']
    test_game.print_board()
    assert not (test_game.winner(0, 'X'))
    print("\ntest_winne_not_won - 2")
    test_game.board = [' ', ' ', 'X', 'O', 'X', ' ', ' ', ' ', ' ']
    test_game.print_board()
    assert not (test_game.winner(2, 'X'))
    print("\ntest_winne_not_won - 3")
    test_game.board = [' ', ' ', 'O', ' ', 'X', ' ', ' ', ' ', ' ']
    test_game.print_board()
    assert not (test_game.winner(5, 'X'))
