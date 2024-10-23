def cone_vol(r,h,pi):
    area = pi*r**2*h*(1/3)
    return area
print(cone_vol(17,12,3.14))
def interest_calculator(P,r,t):
    A = P * (1 + (r / 100))**t
    return A
def average(x1,x2,y,z):
    y= ((x1+x2)/2 )**z 
    return y
print(average(2,3,5,235))