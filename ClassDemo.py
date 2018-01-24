class Person(type):
    def __new__(cls, name, bases, attrs):
        attrs['son'] = list()
        attrs['add'] = lambda self,value: self.son.append(value)
        return type.__new__(cls, name, bases, attrs)
class Son(list, metaclass=Person):
    pass

p = Son()
p.add('pplgin')

print(p.son)
