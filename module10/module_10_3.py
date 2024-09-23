from threading import Thread, Lock
from random import randint
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            add_sum = randint(50, 500)
            self.balance += add_sum
            print(f'Пополнение: {add_sum}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            sub_sum = randint(50, 500)
            print(f'Запрос на {sub_sum}')
            if sub_sum <= self.balance:
                self.balance -= sub_sum
                print(f'Снятие: {sub_sum}. Баланс: {self.balance}')
            else:
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bank = Bank()
deposit = Thread(target = Bank.deposit, args = (bank,))
take = Thread(target = Bank.take, args = (bank,))

deposit.start()
take.start()

deposit.join()
take.join()

print(f'Итоговый баланс: {bank.balance}')
