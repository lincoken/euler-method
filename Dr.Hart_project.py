import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.axes_divider import make_axes_area_auto_adjustable

#this program approximates the derivative

tau = 3
delta_time = float(input("enter a value for change in time: \n"))
range = np.arange(0, 10.1, .1)

def function(t):

    return np.exp((-1 / tau )*t)

def first_dev(t):

    return (-1 / tau ) * np.exp((-1 / tau) * t)

def first_dev_approx(t, dt ) :

    numerator = function(t+dt) - function(t)

    return numerator / dt


def collect(list, dt):
    result = []

    if dt > 0:
        for t in list:
            result.append(first_dev_approx(t, dt))
    else :
        for t in list:
            result.append(first_dev(t))

    return result


# print('x_coordinate')
# for i in time_range:
#     print(i)
#Things to imp[rove ?!calcualte the differance of values to create an array for accuarcy,array with delta t vaules to run and creat dictionary with delta t and -differance. loop it and save files
array1=collect(range, delta_time)
array2 =collect(range,0)
plt.plot(range, array1)
plt.plot(range,array2)
plt.xlabel('Time')
plt.ylabel('Rate of Funtion')
plt.title('Have life derivative aprox. and function')
plt.show()

