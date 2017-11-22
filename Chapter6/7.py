class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return "string=%s, symbol=%s, number=%d" \
               % (self.name, self.symbol, self.number)

hydrogen = Element('Hydrogen', 'H', 1)

print(hydrogen)
