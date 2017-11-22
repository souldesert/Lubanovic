class Laser:
    def does(self):
        return 'disintegrate'


class Claw:
    def does(self):
        return 'crush'


class SmartPhone:
    def does(self):
        return 'ring'


class Robot:
    def __init__(self, laser, claw, smart_phone):
        self.__laser = laser
        self.__claw = claw
        self.__smart_phone = smart_phone

    def does(self):
        return "%s, %s, %s" \
               % (self.__laser.does(), self.__claw.does(), self.__smart_phone.does())

robot = Robot(Laser(), Claw(), SmartPhone())
print(robot.does())
