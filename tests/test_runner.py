# tests/runner.py
import unittest
from tests.piece import *
from tests.board import *
from tests.models import *

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_piece))
suite.addTests(loader.loadTestsFromModule(test_piece_movement))
suite.addTests(loader.loadTestsFromModule(test_piece_legal_moves))
suite.addTests(loader.loadTestsFromModule(test_piece_capture))

suite.addTests(loader.loadTestsFromModule(test_chessboard))
suite.addTest(loader.loadTestsFromModule(test_fen))
suite.addTests(loader.loadTestsFromModule(test_chess_game))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
