import unittest
from game import TicTacToe

import HtmlTestRunner
import xmlrunner


class TestWinner(unittest.TestCase):
    def setUp(self):
        self.test_game = TicTacToe()

    def test_winner_row(self):
        print("\ntest_winner_row - 1")
        self.test_game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.test_game.print_board()
        self.assertTrue(self.test_game.winner(2, 'X'))
        print("\ntest_winner_row - 2")
        self.test_game.board = [' ', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' ']
        self.test_game.print_board()
        self.assertTrue(self.test_game.winner(5, 'X'))
        print("\ntest_winner_row - 2")
        self.test_game.board = [' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X']
        self.test_game.print_board()
        self.assertTrue(self.test_game.winner(8, 'X'))

    def test_winner_colum(self):
        print("\ntest_winner_colum - 1")
        self.test_game.board = ['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ']
        self.test_game.print_board()
        self.assertTrue(self.test_game.winner(0, 'X'))
        print("\ntest_winner_colum - 2")
        self.test_game.board = [' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X', ' ']
        self.test_game.print_board()
        self.assertTrue(self.test_game.winner(1, 'X'))
        print("\ntest_winner_colum - 3")
        self.test_game.board = [' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X']
        self.test_game.print_board()
        self.assertTrue(self.test_game.winner(2, 'X'))

    def test_winner_diagonal1(self):
        print("\ntest_winner_diagonal1")
        self.test_game.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.test_game.print_board()
        self.assertTrue(self.test_game.winner(0, 'X'))

    def test_winner_diagonal2(self):
        print("\ntest_winner_diagonal2")
        self.test_game.board = [' ', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' ']
        self.test_game.print_board()
        self.assertTrue(self.test_game.winner(2, 'X'))

    def test_winne_not_won(self):
        print("\ntest_winne_not_won - 1")
        self.test_game.board = ['X', 'O', 'X', ' ', ' ', ' ', 'X', ' ', ' ']
        self.test_game.print_board()
        self.assertFalse(self.test_game.winner(0, 'X'))
        print("\ntest_winne_not_won - 2")
        self.test_game.board = [' ', ' ', 'X', 'O', 'X', ' ', ' ', ' ', ' ']
        self.test_game.print_board()
        self.assertFalse(self.test_game.winner(2, 'X'))
        print("\ntest_winne_not_won - 3")
        self.test_game.board = [' ', ' ', 'O', ' ', 'X', ' ', ' ', ' ', ' ']
        self.test_game.print_board()
        self.assertFalse(self.test_game.winner(5, 'X'))


def run_all_test():
    # Run all test functions.
    unittest.main()


# Run all test function and generate html report.
def run_all_test_generate_html_report():
    # Run all test functions with HtmlTestRunner to generate html test report.
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reportWinnerUnit'))


# Run all test function and generate html report.
def run_all_test_generate_xml_report():
    # Run all test functions with HtmlTestRunner to generate html test report.
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='./reportWinnerUnit'))


if __name__ == '__main__':
    run_all_test()
    # run_all_test_generate_html_report()
    # run_all_test_generate_xml_report()
