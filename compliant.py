def calculate_area_of_circle(radius):
    """Calculate the area of a circle given the radius."""
    from math import pi

    if radius <= 0:
        raise ValueError("Radius must be positive")
    
    area = pi * radius ** 2
    return area


def main():
    try:
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_area_of_circle(radius)
        print(f"The area of the circle is: {area:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
