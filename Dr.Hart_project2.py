import matplotlib.pyplot as plt
import numpy as np

# import time

# fixed radio active decay problem, approximate the function given relation between derivative and function
tau = float(input("enter a value for Tau (time constant for decay):\n"))
N_0 = float(input("Enter the initial number of uranium nuclei present when time=0 :\n"))
dt = float(input("enter time change:\n"))

# current_time = lambda:int(round(time.time()*1000))

START_RANGE = 0
END_RANGE = 10
STEP = dt


def euler(N_t, halflife, delta_t):
    return N_t - (N_t * delta_t) / halflife


def analytic_value(time, halflife):
    return np.exp((-1 / halflife) * time) * N_0


time_range = np.arange(START_RANGE, END_RANGE + STEP, STEP)

# time_range 2 set to accommodate for using an initial value in the approximation
N = np.array(np.zeros(len(time_range)))

print(len(time_range))

N[0] = N_0

# this is what we know is right
N_analytic = np.array(np.zeros(len(time_range)))
N_analytic[0] = analytic_value(0, tau)

# print(N_analytic[0])

for i, t in enumerate(time_range[1:]):
    N[i + 1] = euler(N[i], tau, dt)
    N_analytic[i] = analytic_value(t, tau)
    print(N[i + 1])

    # approximation is blue
plt.plot(time_range, N)
plt.plot(time_range, N_analytic)
plt.xlabel('Time')
plt.ylabel('Uranium Nuclei Present')
plt.title('Radio Active Decay for Uranium')
plt.show()  # print(function_x)
# print(range_2)

"""
end_time = lambda:int(round(time.time()*1000))
run_time = end_time -  current_time
print(run_time)"""

# difference = N_analytic - N
# plt.plot(time_range, difference)
# plt.show()
