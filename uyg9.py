class TelNo(object):
    def __init__(self, ulkekodu, alankodu, numara):
        self.ulkekodu = ulkekodu
        self.alankodu = alankodu
        self.numara = numara

    @classmethod
    def from_string(cls, string):
        return cls(*string.split(" "))


class AranabilenTelNo(TelNo):
    def ara(self):
        pass


mytel = TelNo.from_string("+90 507 7997272")
print(type(mytel))  # 1
myaranabilentel = AranabilenTelNo.from_string("+90 507 7997272")
print(type(myaranabilentel))  # 2
