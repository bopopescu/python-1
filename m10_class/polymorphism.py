class Dog:
    def run(self):
        print("Dog : run()")
    def walk(self):
        print("Dog : walk()")

class Cat:
    def run(self):
        print("Cat : run()")
    def walk(self):
        print("Cat : walk()")
class Tiger:
    def run(self):
        print("Tiger : run()")
    def walk(self):
        print("Tiger : walk()")
def test(animal):
    animal.run()
    animal.walk() #可以利用相同方法名稱情況下，統一使用多型一次測試
def main():
    dog = Dog()
    cat = Cat()
    tiger = Tiger()
    test(dog)
    test(cat)
    test(tiger)

main()
