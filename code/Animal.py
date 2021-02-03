

class Animal:

    def __init__(self):
        self.name = "胖橘"
        self.colour = "橘黄色"
        self.age = "2岁"
        self.gender = "公猫"

    def yelling(self):
        self.yelling = "说饿了"
        print(f"这只动物一直对我{self.yelling}")

    def run(self):
        self.run = "跑"
        print(f"这只动物满屋子{self.run}")


if __name__ == '__main__':

    cute_animal = Animal()
    print(cute_animal.name, cute_animal.age, cute_animal.colour, cute_animal.gender)
    cute_animal.run()
    cute_animal.yelling()

    """
胖橘 2岁 橘黄色 公猫
这只动物满屋子跑
这只动物一直对我说饿了
    """
