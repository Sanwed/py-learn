from tests_12_3 import RunnerTest, TournamentTest
import unittest

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity = 2)

if __name__ == '__main__':
    runner.run(test_suite)