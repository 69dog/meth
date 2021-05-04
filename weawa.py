#import libraries
import math

# define function
def areaofcircle(r):
        area = math.pi * r * r
        print ("returning to main program")
        return (area)

# main program
radius = float(input("what is the radius of the circle in units?"))
print ("radius is", radius, "units")
print ("area of your rent is", areaofcircle(radius),"units")

