print("****CIRCLE****")
import math
def circle_perimeter(radius):
    return math.pi*radius*2
def circle_area(radius):
    return math.pi*radius*radius
def main():
    radius=float(input("enter the radius of the circle"))
    area=circle_area(radius)
    perimeter=circle_perimeter(radius)
    area=round(area,4)
    perimeter=round(perimeter,4)
    print("the area of the circle is",area)
    print("the perimeter of the circle is",perimeter)
main()
