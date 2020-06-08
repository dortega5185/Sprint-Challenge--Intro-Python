# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# base class vehicle
class Vehicle:
    pass


# subclass of Vehicle class
class GroundVehicle(Vehicle):
    pass


# subclass of GroundVehicle class, which has a base class of Vehicle
class Car(GroundVehicle):
    pass


# subclass of GroundVehicle class, which has a base class of Vehicle
class Motorcycle(GroundVehicle):
    pass


# subclass of Vehicle class
class FlightVehicle(Vehicle):
    pass


# subclass of FlightVehicle class, which has a base class of Vehicle
class Airplane(FlightVehicle):
    pass


# subclass of FlightVehicle class, which has a base class of Vehicle
class Starship(FlightVehicle):
    pass
