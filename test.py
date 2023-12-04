class A:
    """_summary_
    实现create方法只被第一个对象调用一次
    """
    __a_created = False  # 类变量用于标志是否已经创建了a

    def __init__(self) -> None:
        pass

    def create(self):
        if not A.__a_created:
            A.__a_created = True
            print("创建了a")
        else:
            print("没有创建a")

a = A()
b = A()
c = A()
a.create()
b.create()
c.create()



class Singleton:
    """_summary_
    单列模式实现共用一个实例
    Returns:
        _type_: _description_
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

class ServiceA(Singleton):
    def operation(self):
        return "Operation from ServiceA"

class ServiceB(Singleton):
    def operation(self):
        return "Operation from ServiceB"

class ServiceC(Singleton):
    def operation(self):
        return "Operation from ServiceC"

class MyClass:
    def __init__(self, service_a: ServiceA, service_b: ServiceB, service_c: ServiceC):
        self.service_a = service_a
        self.service_b = service_b
        self.service_c = service_c

    def perform_operations(self):
        print(self.service_a.operation())
        print(self.service_b.operation())
        print(self.service_c.operation())

# 创建 MyClass 实例，由于 ServiceA、ServiceB、ServiceC 都是 Singleton，它们都指向同一个实例
my_instance = MyClass(ServiceA(), ServiceB(), ServiceC())
my_instance.perform_operations()

