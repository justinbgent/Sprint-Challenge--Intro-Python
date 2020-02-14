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

# Vehicle is the base class of all of them.
class Vehicle:
    pass
                    #Base
class GroundVehicle(Vehicle):
    pass
                    #Base
class Car(GroundVehicle):
    pass
                    #Base
class Motorcycle(GroundVehicle):
    pass
                    #Base
class FlightVehicle(Vehicle):
    pass
                    #Base
class Starship(FlightVehicle):
    pass
                    #Base
class Airplane(FlightVehicle):
    pass