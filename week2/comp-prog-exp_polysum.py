import math
def polysum(n,s):
    perimeter = n*s
    area = (0.25*n*s**2)/(math.tan(math.pi/n))
    answer = area + perimeter**2
    roundedanswer = round(answer,4)
    return roundedanswer
