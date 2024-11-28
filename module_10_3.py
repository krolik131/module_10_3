import threading
import random
import time
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        #print(self.lock.locked())
        self.lock.acquire()
        for i in range(100):
            random_num = random.randint(50, 500)
            self.balance = self.balance + random_num
            print(f'Пополнение на: {random_num}$. Актуальный баланс:{self.balance}$.')
            time.sleep(1)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
                print(f'Баланс: {self.balance}$')

    def take(self):
        for i in range(100):
            random_num = random.randint(50, 500)
            print(f'Запрос на: {random_num}$.')
            if random_num <= self.balance:
                self.balance = self.balance - random_num
                print(f'"Снятие: {random_num}$. Баланс: {self.balance}$"')
            else:
                print(f'Запрос отклонён, недостаточно средств на счету. Баланс: {self.balance}$')
                self.lock.acquire()

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}$')