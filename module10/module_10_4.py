from queue import Queue
from random import randint
from threading import Thread
from time import sleep

class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *tables: Table):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            is_sitting = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    is_sitting = True
                    break
            if not is_sitting:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while (
                not self.queue.empty()
                or any(table.guest is not None for table in self.tables)
        ):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушел(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        print(f'{table.guest.name} вышел из очереди и сел(-а) за стол номер {table.number}')
                        table.guest.start()


tables = [Table(number) for number in range(1, 6)]
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
