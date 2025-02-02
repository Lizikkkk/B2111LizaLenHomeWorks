import random


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None, parrot=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 10
        self.job = job
        self.home = home
        self.car = car
        self.parrot = parrot

    def get_home(self):
        self.home = Home()

    def get_parrot(self):
        self.parrot = Parrot()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(list_of_job)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("I bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hooray!!!!!! Delicacies!!!!!!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_house(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def feed_parrot(self):
        if self.home.food >= 5:
            self.parrot.golod -= 10
        else:
            print("Lets buy food for parrot")
            self.shopping("food")

    def play_parrot(self):
        self.parrot.igrat -= 10
        self.parrot.golod += 5
        self.gladness += 10

    def day_indexes(self, day):
        print(f"Today is {day} of {self.name}'s live")
        print(f"Money - {self.money}\nGladness - {self.gladness}\nSatiety - {self.satiety}")
        print(f"Home \nFood - {self.home.food}\nMess - {self.home.mess}")
        print(f"Car\nFuel - {self.car.fuel}\nStrength - {self.car.strength}")
        print(f"Parrot\nGolod - {self.parrot.golod}\nIgrat - {self.parrot.igrat}")
        self.parrot.golod += 1
        self.parrot.igrat += 2

    def is_alive(self):
        if self.gladness < 0:
            print("Depression")
            return False
        if self.satiety < 0:
            print("Dead")
            return False
        if self.money < -500:
            print("Bankrut")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in a house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I am a {self.job.job}")
        if self.parrot is None:
            self.get_parrot()
            print(f"I am getting a parrot")
        self.day_indexes(day)
        dice = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.gladness < 20:
            self.chill()
        elif self.money < 0:
            self.work()
        elif self.car.strength < 15:
            self.to_repair()
        elif self.parrot.igrat >= 70:
            self.play_parrot()
        elif self.parrot.golod >= 70:
            self.feed_parrot()
        if dice == 1:
            print("Lets chill!")
            self.chill()
        elif dice == 2:
            print("It's time to go work!")
            self.work()
        elif dice == 3:
            print("Cleaning time")
            self.clean_house()
        elif dice == 4:
            print("Time for treats")
            self.shopping("delicacies")
        elif dice == 5:
            print("It's time to play with parrot!")
            self.play_parrot()
        elif dice == 6:
            print("It's time to feed parrot!")
            self.feed_parrot()


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move!")
            return False


brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, 'consumption': 6},
    "Lada": {"fuel": 50, "strength": 40, 'consumption': 10},
    "Volvo": {"fuel": 70, "strength": 150, 'consumption': 8},
    "Ferari": {"fuel": 80, "strength": 120, 'consumption': 14}
}


class Home:
    def __init__(self):
        self.food = 0
        self.mess = 0

class Parrot:
    def __init__(self):
        self.golod = 50 #чим більше - тим більше голод
        self.igrat = 50 #чим більше - тим більше хоче гратися


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


list_of_job = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1},
}

my_human = Human(name=input("name - "))
for day in range (1,32):
    if my_human.live(day) == False:
        break