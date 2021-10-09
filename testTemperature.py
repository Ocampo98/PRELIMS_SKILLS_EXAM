from unittest import TestCase, main
from Temp import Temperature

class Testing(TestCase):

    def _CeltoFa(self):
        a = Temperature(celsius=12).kelvin
        b = 12 + 273.15
        self.result(a,b)

    def _CeltoFa2(self):
        a = Temperature(celsius=20).kelvin
        b = 20 + 273.15
        self.result(a,b)

    def _FartoK(self):
        a = Temperature(fahrenheit=12).kelvin
        b = 12 + 273.15
        self.result(a,b)

    def _CeltoFa(self):
        a = Temperature(fahrenheit=12).kelvin
        b = 12 + 273.15
        self.result(a,b)

        
if __name__=="__main__":
    main()