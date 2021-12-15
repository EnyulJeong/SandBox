class Parent ():
    def __init__(self, foo):
        # parameter (매개변수) a(변수) = 10(value)
        # argument (매개변수에 넣어주는 특정 value)
        print("this is inside of init of Parent class")
        print(f"foo is {foo}")
        # Parent() 클래스 함수를 실행할 때 반환값은 어떤 객체이므로 return 문이 없음
        # Parent() 클래스 함수를 실행할 때 인자는 __init__ 내부함수의 두번째 이하 매개변수가 받음
        # Parent() 클래스 함수를 실행할 때 어떤 객체를 반환한 직후 자동으로 __init__ 함수를 실행
        # Parent() 클래스 함수 내부함수들의 첫번째 매개변수(convention self)는 클래스 실행을 반환되는 객체를 argument로 삼아


    def foo(self, a):
        print(f"{a} is the argument of the foo function")

instanceOfParent = Parent(2)
print(instanceOfParent.foo(3))

class Child (Parent):

    def __init__(self, foo, z):
        super().__init__(foo)
        print(foo)
        print(z)

    def foo():
        print("hahaha") # override
    def ba(self, b):
        print(f"this is child mehtod for {b}")

childinstance = Child(4, 44)
print(childinstance.ba(55))



