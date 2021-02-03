

from Animal import Animal

class Cat(Animal):


    def __init__(self):
        self.hair = "短毛"
        print(f"我的猫是一只{self.hair}猫")
        super().__init__()

    def catch(self):
        self.catch = "捉老鼠"
        print(f"猫很会{self.catch}")

    def yelling(self):
        self.yelling = "喵喵叫"
        print(f"{cat.name}一直对我{self.yelling}")



if __name__ == '__main__':

    cat = Cat()
    print(cat.name, cat.age, cat.colour, cat.gender)
    cat.run()
    cat.yelling()
    cat.catch()