def cone_vol(r,h,pi):
    area = pi*r**2*h*(1/3)
    return area
print(cone_vol(17,12,3.14))
def f(x1,x2,y1,y2):
    m = (y2-y1)/(x2-x1)
    k = -(m*x1)+y1
    return k
print(f(26,10,33,18))
