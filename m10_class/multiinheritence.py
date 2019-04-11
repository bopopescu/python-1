class A (object):
    def method1(self):
        print('A.m1')
    def method2(self):
        print('A.m2')
class B (A):
    def method3(self):
        print('B.m3')
class C (A):
    def method2(self):
        print('C.m2')
    def method3(self):
        print('C.m3')
class D (B,C):
    def method4(self):
        print('D.m4')

def main():
    d = D()
    d.method1()
    d.method2()
    d.method3()
    d.method4()
main()