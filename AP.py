class BMW:
    
    def fuel_type(self):
        print ("BMW m5 Fuel Type is Petrol")
    
    def max_speed(self):
        print ("BMW m5 Max Speed is 325 kmh")
    
    def mileage(self):
        print ("BMW mileage is 9 kmpl")        
          
class Lamborgini:
    
    def fuel_type(self):
        print ("Lamborgini huracan Fuel Type is Petrol")
    
    def max_speed(self):
        print ("Lamborgini huracan Max Speed is 325 kmh")
    
    def mileage(self):
        print ("Lamborgini huracan mileage is 11 kmpl")    

class Horse:
    
    def fuel_type(self):
        print ("Horse's fuel type is water")
    
    def max_speed(self):
        print ("Horse's max speed is 50 kmh")

    def mileage(self):
        print ("Horse's Mileage is 3 kmpl")

class buggati:
    
    def fuel_type(self):
        print ("Buggatis fuel type is petrol/gas")
    
    def max_speed(self):
        print ("Buggatis max speed is 429 kmh")    
    
    def mileage(self):
        print ("Buggati's mileage is 16 kmpl")
bmw = BMW()
lamborgini = Lamborgini()
Horse = Horse()
Buggati = buggati()

for car in (bmw, lamborgini, buggati, Horse):
    car.fuel_type()
    car.max_speed()
    car.mileage()
    print()