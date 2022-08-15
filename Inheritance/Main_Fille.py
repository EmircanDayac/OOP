class Animal:
    def __init__(self):
        self.eyes = 2

    def run(self):
        print("ye run")


class wolf(Animal):
    def __init__(self):
        super().__init__()

    def voice(self):
        print("haw haw!")

one = wolf()
one.run()
print(one.eyes)
one.voice()
