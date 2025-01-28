#симулятор папуги
import random


class Parrot:
    def __init__(self, name):
        self.name = name
        self.besellye = 10  #на скільки папуга щаслива
        self.golod = 10  #на скільки папуга голодна (чим менше ця змінна, тим голодніша папужка)
        self.sonlivost = 10  #на скільки папуга хоче спати (чим більша ця змінна, тим більше хоче спати)
        self.alive = True

    def to_kushat(self):  #папуга їсть
        print("Час поїсти!")
        self.golod -= 5
        self.sonlivost += 1
        self.besellye -= 2

    def to_spat(self):  #папуга спить
        print("Час поспати!")
        self.sonlivost -= 3
        self.besellye -= 1
        self.golod += 5

    def to_besitsya(self):  #папуга біситься (грається)
        print("Час побеситися!")
        self.besellye += 5
        self.golod += 3
        self.sonlivost += 1

    def я_живий(self):  #перевірка на скільки жива папужка
        if self.golod < 0:
            print("Помер від голоду(")
            self.alive = False
        if self.besellye <= 0:
            print("Діпрессія...(")
            self.alive = False
        if self.sonlivost >= 30:
            print("Помер від безсонні(")
            self.alive = False

    def end_of_day(self):  #ітоги дня
        print(f"Щастя = {self.besellye}")
        print(f"Голод = {self.golod}")
        print(f"Сонливість = {self.sonlivost}")

    def live(self, day):
        text = f"{day} день з життя {self.name}"
        print(f"{text:=^30}")
        live_cub = random.randint(1, 3)
        if live_cub == 1:
            self.to_kushat()
        elif live_cub == 2:
            self.to_spat()
        elif live_cub == 3:
            self.to_besitsya()
        self.end_of_day()
        self.я_живий()


Papyga = Parrot(input("Оберіть ім'я папужки "))

for day in range(365):
    if Papyga.alive:
        Papyga.live(day)
    else:
        break
