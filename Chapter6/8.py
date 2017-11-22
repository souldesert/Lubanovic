class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    def __str__(self):
        return "string=%s, symbol=%s, number=%d" \
               % (self.__name, self.__symbol, self.__number)

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

hydrogen = Element('Hydrogen', 'H', 1)

print(hydrogen.name)

