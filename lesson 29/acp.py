# Create a Bus child class inherited from the Vehicle class to calculate the total fare.
class Vehicle:
    def _init_(self, name, capacity, fare_per_person):
        self.name = name
        self.capacity = capacity
        self.fare_per_person = fare_per_person

    def total_fare(self):
        return self.capacity * self.fare_per_person

class Bus(Vehicle):
    def total_fare(self):
        base_fare = super().total_fare()
        maintenance_charge = base_fare * 0.1
        return base_fare + maintenance_charge

bus = Bus("City Bus", 50, 20)
print(f"Total Bus Fare: {bus.total_fare()}")