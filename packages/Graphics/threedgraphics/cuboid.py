print("****CUBOID****")
def cuboid_SA(length,width,height):
    return 2*(length*width+height+width*height)
def cuboid_volume(length,width,height):
    return length*width*height
def main():
    length=float(input("enter the length"))
    width=float(input("enter the width"))
    height=float(input("enter the height"))
    area=cuboid_SA(length,width,height)
    volume=cuboid_volume(length,width,height)
    area=round(area,4)
    volume=round(volume,4)
    print("the area of the cuboid is", area)
    print("the volume of the cuboid is",volume)
main()
