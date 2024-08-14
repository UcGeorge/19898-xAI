def CalculateAreaOfCircle( Radius ):
    from math import pi
    if( Radius <= 0 ):
        raise ValueError( "Radius must be positive" )
    area=pi*Radius**2
    return area


def Main():
    try:
        Radius = float(input("Enter the radius of the circle: "))
        Area = CalculateAreaOfCircle( Radius )
        print("The area of the circle is: ", Area)
    except ValueError as e:
        print( "Error: ", e )
Main()
