def calculate_area(length,width):
    return 2 *(length + width)
def calculate_perimeter(length,width):
    return 2* (length + width)
def rectangle_info(length,width):
    area = calculate_area(length + width)
    perimeter = calculate_perimeter(length,width)
    print("the area of the rectangle is:",area)
    print("the perimeter of the rectangle is:",perimeter)
    rectangle_info(4,5)