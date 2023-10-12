def calculate_perimeter():
    calculate_perimeter = ( length + width) * 2
    return calculate_perimeter

length = float(input("Enter the Length of the Rectangle:"))
width = float(input("Enter the width of the Rectangle:"))

perimeter = calculate_perimeter()

print("The perimeter of the Rectangle with a width of", width ,"and a length of", length ,"is", perimeter)