#replace with actual fields
long = 0
lat = 0
height = 0
on = true
company = 'firebolt space agency'
isFlying = false
anonymous = false

class car:
    def __init__(self, long, lat, height,on, company, isFlying, anonymous,gas):
        self._gas = gas
        self._long = long
        self._lat = lat
        self._height = height
        self._on = on
        self._company = company
        self._isFlying = isFlying
        self._anonymous = anonmymous
        self._on = false
        self._isFlying = false
    def refillGas(self):
        self._gas = 100
    def lowGas(self):
        # update amount of gas
        if self._gas < 20:
            print("Refill gas soon the percentage of gas is",self._gas,"%")
    def turnOff(self):
        self._on = true
    def  takeOff(self):
        self._isFlying = true
    def goingAnonymous(self):
        self._anonymous = true
    def north(self, units):
        self._lat = self._lat + units
    def south(self, units):
        self._lat = self._lat - units
    def west(self,units):
        self._long - units
    def east(self,units):
        self._long + units
    def rise(self,units):
        self._height = self._height + units
    def fall(self,units):
        self._height= self._height - units
def test():
    try:
        # TODO(aaronhma): Print test messages with color
        canary = car(long,lat,height, on,'firebolt space agency', isFlying, anonymous, gas)
        print("[PASS] Passed!")
    except:
        canary = None
        raise Exception("[FAIL] Test failed!")
    return canary

if __name__ == "__main__":
    sep = "==============================================================="
    print(sep, "\nTesting!\n")
    test()
    print("\n", sep)
