import unittest

class Runner:
    def __init__(self, name, speed = 5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants[:]:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    isFrozen = False

    @unittest.skipIf(isFrozen, 'test_walk has been frozen')
    def test_walk(self):
        runner = Runner('Alex')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(isFrozen, 'test_run has been frozen')
    def test_run(self):
        runner = Runner('Andrew')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(isFrozen, 'test_challenge has been frozen')
    def test_challenge(self):
        runner1 = Runner('Alex')
        runner2 = Runner('Andrew')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

class TournamentTest(unittest.TestCase):
    isFrozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = Runner("Усэйн", speed = 10)
        self.runner2 = Runner("Андрей", speed = 9)
        self.runner3 = Runner("Ник", speed = 3)

    @classmethod
    def tearDownClass(cls):
        for res in cls.all_results:
            print('\n', res)

    @unittest.skipIf(isFrozen, 'test_race_1 has been frozen')
    def test_race_1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        TournamentTest.all_results.append(tournament.start())
        self.assertTrue(TournamentTest.all_results[-1][max(TournamentTest.all_results[-1].keys())], 'Ник')

    @unittest.skipIf(isFrozen, 'test_race_2 has been frozen')
    def test_race_2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        TournamentTest.all_results.append(tournament.start())
        self.assertTrue(TournamentTest.all_results[-1][max(TournamentTest.all_results[-1].keys())], 'Ник')

    @unittest.skipIf(isFrozen, 'test_race_3 has been frozen')
    def test_race_3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        TournamentTest.all_results.append(tournament.start())
        self.assertTrue(TournamentTest.all_results[-1][max(TournamentTest.all_results[-1].keys())], 'Ник')


if __name__ == '__main__':
    unittest.main()
