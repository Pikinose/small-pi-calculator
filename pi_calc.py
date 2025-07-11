#code regarding pi
#this code is about calculating pi values
#or u can say a small pi calculator

pi_float = 3.141592653
pi_approx = 22/7

def cmfc(radius):
    
    cmfce2 = 2*pi_approx*radius
    
    return cmfce2
    print("the approx circumference of the given radius is ", cmfce)
    print("The almost exact circumference of the given radius is ", cmfce2)


def area(radi):
    
    ara_estimate = pi_approx*radi**2
    return ara_estimate
    
    print("The estimated area for the given radius is ", ara_estimate)
    print("The approx exact area for the given radius is ", ara_float)

def cmfcd(diameter):
    
    cmfcde2 = pi_approx*diameter
    
    return cmfcde2
    print("Approx circumference of the given diameter circle is ", cmfcde2)
    print("The almost exact circumference of the given diameter of the circle is ", cmfcde)

def arad(diameter):
    
    arar2 = pi_approx*diameter**2/4
    
    return arar2
    print("Approx area of the given diameter circle is ", arar2)
    print("The almost exact area of the given diameter of the circle is ", arar)


#trying out.............

print("Area with diameter", arad(2)) #area with diameter
print("Circumference with diameter", cmfcd(2)) #circumference with diameter
print("circumference with radius", cmfc(2)) #circumference with radius
print("Area with radius", area(2)) #area with radius