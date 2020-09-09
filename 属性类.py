class RMB:
    __className = "RMB"
    def __init__(self, name, money):
        self.name = name
        self.__money = money
    def say(self):
        print("I am %s ,i have %d yuan" % (self.name, self.__money))
p = RMB('SJH',1000)
p.say()