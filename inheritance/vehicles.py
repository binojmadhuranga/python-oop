"""Inheritance practice: Demo using Vehicle, Car, and Truck classes.

This example shows:
- A base class `Vehicle` with common behavior and attributes (in vehicle.py)
- Subclasses `Car` and `Truck` that inherit and override behavior (in car.py and truck.py)
- Use of `super()` to call the parent implementation
- Polymorphism: treating different subclasses uniformly
- `isinstance` and `issubclass` checks

Run with:
    python .\inheritance\vehicles.py
"""

from __future__ import annotations
from vehicle import Vehicle
from car import Car
from truck import Truck


def _demo() -> None:
    vehicles: list[Vehicle] = [
        Car("Toyota", "Corolla", 2020, doors=4),
        Truck("Ford", "F-150", 2019, capacity_tons=1.5),
        Vehicle("Generic", "ModelX", 2010),
    ]

    for v in vehicles:
        print(v.info())
        print(" Horn:", v.horn())
        v.accelerate(20)
        print(" After accelerating to speed:", v.speed)
        v.brake(5)
        print(" After braking:", v.speed)
        print()

    # Polymorphism: call the same function for different types
    def sound_the_horn(vehicle: Vehicle) -> None:
        print(f"{vehicle.make} horn sound: {vehicle.horn()}")

    for v in vehicles:
        sound_the_horn(v)

    # isinstance and issubclass
    c = Car("Honda", "Civic", 2022)
    print("c is Vehicle?", isinstance(c, Vehicle))
    print("Car is subclass of Vehicle?", issubclass(Car, Vehicle))


if __name__ == "__main__":
    _demo()
