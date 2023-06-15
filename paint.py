import math
wall_height=int(input("Please enter the wall height"))
wall_width=int(input("Please enter the wall width"))
def paint(coverage_per_can):
    area=wall_height*wall_width
    number_of_cans=math.ceil(area/coverage_per_can)
    print(number_of_cans)
paint(5)    
