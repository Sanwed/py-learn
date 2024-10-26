import unittest
import logging

logging.basicConfig(
    level = logging.INFO,
    filename = 'runner_tests.log',
    filemode = 'w',
    encoding = 'UTF-8',
    format = '%(levelname)s: %(message)s'
)

class Runner:
    def __init__(self, name, speed = 5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
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
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    isFrozen = False

    @unittest.skipIf(isFrozen, 'test_walk has been frozen')
    def test_walk(self):
        try:
            runner = Runner('Alex', -5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info = True)


    @unittest.skipIf(isFrozen, 'test_run has been frozen')
    def test_run(self):
       try:
           runner = Runner(2321)
           for _ in range(10):
               runner.run()
           self.assertEqual(runner.distance, 100)
           logging.info('"test_run" выполнен успешно')
       except TypeError:
           logging.warning('Неверный тип данных для объекта Runner', exc_info = True)

    @unittest.skipIf(isFrozen, 'test_challenge has been frozen')
    def test_challenge(self):
        runner1 = Runner('Alex')
        runner2 = Runner('Andrew')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()
