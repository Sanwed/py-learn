from runner import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print('\n', dict({i + 1: cls.all_results[i] for i in range(len(cls.all_results))}))

    def test_faster_and_slower1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        self.__class__.all_results = tournament.start()
        self.assertTrue(self.all_results[-1], 'Ник')

    def test_faster_and_slower2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        self.__class__.all_results = tournament.start()
        self.assertTrue(self.all_results[-1], 'Ник')

    def test_faster_and_slower3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.__class__.all_results = tournament.start()
        self.assertTrue(self.all_results[-1], 'Ник')


if __name__ == '__main__':
    unittest.main()
