#******************** CLASSES ********************#
# when you invoke any class it executes the __init__ method.


class Zoo:
    def __init__(self, name):
        self.zoo_name = name


my_zoo = Zoo("Brandon's zoo")

print(my_zoo.zoo_name)
