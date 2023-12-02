from abc import abstractclassmethod, ABCMeta

class InterfaceClass(metaclass=ABCMeta):
    """_summary_
    定义一下需要实现的方法
    Args:
        metaclass (_type_, optional): _description_. Defaults to ABCMeta.
    """
    def __init__(self) -> None:
        pass
    
    @abstractclassmethod
    def test(self):
        pass