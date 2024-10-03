import math

def calculate_area_of_circle(radius):
    # Calculate the area using the formula: area = πr²
    area = math.pi * (radius ** 2)
    return area

def main():
    # Get the radius from the user
    radius = float(input("Enter the radius of the circle: "))
    
    # Calculate the area
    area = calculate_area_of_circle(radius)
    
    # Display the result
    print(f"The area of the circle with radius {radius} is: {area:.2f}")

if __name__ == "__main__":
    main()
