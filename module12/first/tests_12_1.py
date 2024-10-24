from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """
        Should be correct distance after runner walk
        """
        runner = Runner('Alex')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        """
        Should be correct distance after runner run
        """
        runner = Runner('Alex')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        """
        Should be not equal distance after challenge
        walking and running runners
        """
        runner1 = Runner('Alex')
        runner2 = Runner('Andrew')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()