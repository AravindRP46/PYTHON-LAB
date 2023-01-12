print("****SPHERE****")
import math
def sphere_area(radius):
    return 4*math.pi*radius**2
def sphere_vol(radius):
    return (4/3)*math.pi*radius**3
def main():
    radius=float(input("enter the radius of the sphere"))
    area=sphere_area(radius)
    volume=sphere_vol(radius)
    area=round(area,4)
    volume=round(volume,4)
    print("area of the sphere is :",area)
    print("volume of the sphere is:",volume)
main()
