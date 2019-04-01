import math
import matplotlib.pyplot as plt

def f(x):

##    if (x >=0):
##        return 1
##    return 0

    if (x >= -1 and x <= 1):
        return 1
    return 0


    return abs(x)
    
##    if (x >= -1 and x <= 0):
##        return 1+x
##    elif (x > 0 and x <= 1):
##        return 1-x
##    return 0
##
##    return math.sin(x)

def g(x):

##    if x in [0,1,2,3,-1,-2,-3]:
##        return 1
##    return 0

##    return -abs(x)

##    return math.e

    if (x >= -1 and x <= 1):
        return 1
    return 0
##
##    if (x >= -1 and x <= 0):
##        return 1+x
##    elif (x > 0 and x <= 1):
##        return 1-x
##    return 0

##    return math.sin(x)

    return math.cos(x)

def get_points(offset, l, r, inc_f):

    y_points = []

    i = l

    while i <= r:

        y_points += [g(offset - i)]

        i += inc_f

    return y_points
    
l = -3
r = 3
inc_f = 0.01

x_f = []
y_f = []
y_fpre = []
x_g = []
y_g = []
y_gi = []
x_h = []
y_h = []
x_gshift = []

#getting points
i = l
while i <= r:

    x_gshift += [i]
    y_fpre += [f(i)]
    i += inc_f

i = l

while i <= r:

    x_f += [i]
    x_g += [i]
    x_h += [i]
    y_f += [f(i)]
    y_g += [g(i)]
    y_gi += [g(-i)]
    y_gshift = get_points(i, l, r, inc_f)

    #to calculate h(x)
    j = l
    curr = 0
    while j <= r:

        curr += f(j)*g(i-j)*inc_f

        j += inc_f

    y_h += [curr]

    #plotting axes and bounds
    plt.axvline(0, color = 'black')
    plt.axhline(0, color = 'black')
    plt.axvline(l, color = 'white')
    plt.axvline(r, color = 'white')
    plt.axvline(i, color = 'green')

    #plotting functions
##    plt.plot(x_f, y_f, color = 'grey')
    plt.plot(x_gshift, y_fpre, color = 'grey')
##    plt.plot(x_g, y_g, color = 'grey')
##    plt.plot(x_g, y_gi, color = 'blue')
    plt.plot(x_gshift, y_gshift, color = 'blue')
    plt.plot(x_h, y_h, color = 'red')

    plt.show(block = False)
    plt.pause(0.01)
    plt.close()

    i += inc_f

#plotting axes
plt.axhline(0, color = 'black')
plt.axvline(0, color = 'black')

#plotting functions
plt.plot(x_f, y_f, color = 'grey')
plt.plot(x_g, y_g, color = 'grey')
plt.plot(x_g, y_gi, color = 'blue')
plt.plot(x_h, y_h, color = 'red')

plt.show()
