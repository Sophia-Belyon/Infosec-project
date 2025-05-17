def handle_error(instruction):
    while True:
        user_input = input(instruction)
        if user_input.strip() == "":
            print("Invalid input.Enter a valid number: ")
        elif user_input.isdigit():
            return user_input
        else:
             print("Invalid input.Enter a positive integer: ")
        
def area(a,b):
   area = a * b
   return area

def perimeter(a,b):
    perimeter = a + b
    return perimeter

length= int(handle_error("Enter length: "))
width = int(handle_error("Enter width: "))

square_perimeter = perimeter(length,width) 
square_area = area(length,width)

print(f"Square perimeter = {square_perimeter}")
print(f"Square area = {square_area}")