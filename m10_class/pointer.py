class Pointer:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "x = {} , y = {}".format(self.x,self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Pointer(x,y)
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Pointer(x,y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y



def main():
    p1 = Pointer(4,8)
    print(p1)
    p2 = Pointer(4,8)
    print(p2)
    print(p1 +p2)
    print(p1 - p2)
    print(p1 == p2)

main()