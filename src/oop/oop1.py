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

''' nothing '''
class Vehicle():
    pass
''' is a Vehicle '''
class FlightVehicle(Vehicle):
    pass
''' is a Vehicle '''
class GroundVehicle(Vehicle):
    pass
''' is a FlightVehicle'''
class Starship(FlightVehicle):
    pass
''' is a FlightVehcile '''
class Airplane(FlightVehicle):
    pass
''' is a GroundVehicle '''
class Car(GroundVehicle):
    pass
''' is a GroundVehicle'''
class Motorcycle(GroundVehicle):
    pass