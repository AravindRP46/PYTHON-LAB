print("****RECTANGLE****")
def rect_perimeter(l,w):
 return 2*(l+w)
def rect_area(l,w):
 return l*w
def main():
 l=int(input("enter length of the rectangle:"))
 w=int(input("enter the width of the rectangle:"))
 area=rect_area(l,w)
 perimeter=rect_perimeter(l,w)
 area=round(area,4)
 perimeter=round(perimeter,4)
 print("area of rectangle is:",area)
 print("perimeter of rectangle is",perimeter)
main()
