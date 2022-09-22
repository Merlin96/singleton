import os
import pickle
class SingletonPy(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
class Singletonkek(metaclass=SingletonPy):
    def some_business_logic(self,a):
        a=5
        return a


class Singleton:
    def __init__(self, ipn, opv, vosms, osms, sn, so, oklad, mrp, zp):
        self.ipn = ipn
        self.opv = opv
        self.vosms = vosms
        self.osms = osms
        self.sn = sn
        self.so = so
        self.oklad = oklad
        self.mrp = mrp
        self.zp = zp

    def Show(self):
        print(self.ipn, self.opv, self.vosms, self.osms, self.sn, self.so, self.oklad, self.mrp, self.zp)

    def singleton_base(self, zp):
        opv_r = float(zp) * self.opv
        print("OPV: ", opv_r)
        vosms_r = opv_r * self.vosms
        print("VOSMS: ", vosms_r)
        ipn_r = (zp - opv_r - 14 * self.mrp - vosms_r) * 0.1
        print("IPN: ", ipn_r)
        zp_r = zp - opv_r - ipn_r - vosms_r
        return zp_r

    def gph(self, zp):
        opv_r = float(zp) * self.opv
        print("OPV: ", opv_r)
        ipn_r = (float(zp) - opv_r) * self.ipn
        print("IPN: ", ipn_r)
        osms_r = float(zp) * 0.03
        print("OSMS: ", osms_r)
        zp = float(zp) - opv_r - ipn_r - osms_r
        return zp


if os.path.isfile('saved.pickle'):
    pass
else:
    s = Singleton(0.1, 0.1, 0.02, 0.03, 0.095, 0.035, 0, 0.03, 0)
    with open("saved.pickle", "wb") as outfile:
        pickle.dump(s, outfile)

# print("S: ", s)




with open("saved.pickle", "rb") as infile:
    s_saved = pickle.load(infile)
# Debug to know files was stored xD
# print("saved: ", s_saved)
# Singleton.Show(s_saved)
your_zp = int(input("Enter your zp"))
print("What operation do you want?")
print("1) GPH Form \n" "2)Based")
choose = int(input("1 or 2..."))
if (choose == 1):
    Gph = Singleton.gph(s_saved, your_zp)
    print("Your GPH: ", Gph)
    with open("gph.pickle", "wb") as outfile:
        pickle.dump(Gph, outfile)
elif (choose == 2):
    based = Singleton.singleton_base(s_saved, your_zp)
    print("Your zp: ", based)
    with open("based.pickle", "wb") as outfile:
        pickle.dump(based, outfile)
obj = []
with open("based.pickle", "rb") as openfile:
    obj.append(pickle.load(openfile))
print (obj)
