from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, type_, physique, character):
        self.name = None
        self.type = type_
        self.physique = physique
        self.character = character

    @classmethod
    def cry(cls):
        print(cls.voice)

    @property
    def is_fierce(self):
        return True if self.physique >= "中等" \
                       and self.type == "食肉" \
                       and self.character == "凶猛" \
            else False

    @property
    def is_pet(self):
        return False if self.character == "凶猛" else True


class Cat(Animal):
    voice = "喵"

    def __init__(self, name, type_, physique, character):
        super().__init__(type_, physique, character)
        self.name = name


class Dog(Animal):
    voice = "汪"

    def __init__(self, name, type_, physique, character):
        super().__init__(type_, physique, character)
        self.name = name


class Zoo(object):
    def __init__(self, name):
        self.name = name
        self._animal_set = set()

    def add_animal(self, animal: Animal):
        if animal not in self._animal_set:
            self._animal_set.add(animal)
            setattr(self, animal.__class__.__name__, None)
        else:
            animal.cry()
            print(animal.name, "has been already add into zoo")


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    assert cat1.is_fierce == False
    cat2 = Cat("mao2", '食肉', '中等', '凶猛')
    assert cat2.is_fierce == True

    # 增加一只猫到动物园
    z.add_animal(cat1)
    z.add_animal(cat2)
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    assert have_cat == True
    assert hasattr(z, 'Dog') == False
