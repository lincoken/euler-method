import matplotlib.pyplot as plt
import numpy as np

velocity_i = float(input("Enter an inital velocity: \t"))
angle = float(input("Enter an angle to launch cannon from (degrees): \t"))
velocity_xi = velocity_i * np.cos(np.deg2rad(angle))
velocity_yi = velocity_i * np.sin(np.deg2rad(angle))
dt = float(input("Enter a change in time to aproximate path: \t"))
B2 = float(input("Enter a drag constant: \t"))
mass = 50
gravity = 10
x_inital = 0
y_inital = 0
X = [x_inital]
Y = [y_inital]
Vx = [velocity_xi]
Vy = [velocity_yi]


def euler_x(x_t, v_xt, delta_t):
    return x_t + (v_xt * delta_t)


def euler_Vx(v_xt, B2, v, delta_t, m):
    return v_xt - (B2 * v * v_xt * delta_t) / m


def euler_y(y_t, v_yt, delta_t):
    return y_t + (v_yt * delta_t)


def euler_Vy(v_yt, B2, v, delta_t, m, g):
    return v_yt - (g * delta_t) - (B2 * v * v_yt * delta_t) / m


while True:
    placement_x = len(X) - 1
    x_old = X[placement_x]

    placement_y = len(Y) - 1
    y_old = Y[placement_y]

    placementVx = len(Y) - 1
    Vx_old = Vx[placementVx]

    placementVy = len(Y) - 1
    Vy_old = Vy[placementVy]

    V_old = np.sqrt((Vx_old * Vx_old) + (Vy_old * Vy_old))

    X.append(euler_x(x_old, Vx_old, dt))
    Vx.append(euler_Vx(Vx_old, B2, V_old, dt, mass))

    y_i = euler_y(y_old, Vy_old, dt)
    Y.append(y_i)
    Vy.append(euler_Vy(Vy_old, B2, V_old, dt, mass, gravity))

    if y_i <= 0:
        break

#print(X)
#print(Y)

plt.plot(X, Y)

plt.xlabel('x position')
plt.ylabel('y position')
plt.title('ready, aim, FIRE')

plt.show()
print((X[len(X) - 1] + X[len(X)-2]) /2)