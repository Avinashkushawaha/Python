#Create a function that returns both the area and circumference of a circle given its radius.
import math
def circle_stats(radius):
    area =  3.14 * radius ** 2
    circumference = 2 * 3.14 * radius
    return area, circumference

a, c = circle_stats(3)

print("Area:", a, "Circumference: ", c)


