class Bear:

    @staticmethod
    def eats():
        return 'berries'


class Rabbit:

    @staticmethod
    def eats():
        return 'clover'


class Octothorpe:

    @staticmethod
    def eats():
        return 'campers'

# b = Bear()
# print(b.eats())
#
# r = Rabbit()
# print(r.eats())
#
# o = Octothorpe()
# print(o.eats())

print(Bear.eats())
print(Rabbit.eats())
print(Octothorpe.eats())
