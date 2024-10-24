import matplotlib.pyplot as plt
import numpy as np

'''
System to model:
s' = -B*s*i
i' = B*s*i-y*i
r' = y*i
'''

# Parameters
B = 1/3
y = 1/6
n_days = 250
dt = 1

# Initial Conditions
s = 1 - 1e-6
i = 1e-6
r = 0

# Logging
s_t = [s]
i_t = [i]
r_t = [r]
t = np.arange(0, n_days, dt)

# Run simulation for n_days
for step in range(len(t)-1):
	# Calculate change
	ds = -1*(B*s*i) * dt
	di = (B*s*i - y*i) * dt
	dr = (y*i) * dt

	# Update
	s += ds
	i += di
	r += dr

	# Log
	s_t.append(s)
	i_t.append(i)
	r_t.append(r)

# Estimate contact number from equilibrium populations
s_e = s_t[-1]
i_e = i_t[-1]
r_e = r_t[-1]
c = np.log(s_e) / (s_e -1)
print("Contact Number: ", c)


# Plot results
plt.plot(t, s_t, label='Susceptible')
plt.plot(t, i_t, label='Infected')
plt.plot(t, r_t, label='Recovered')
plt.title(f"SIR Model | β={np.round(B,2)} γ={np.round(y,2)}")
plt.xlabel("Days since start of infection")
plt.ylabel("Proportion of population")
plt.legend()
plt.show()
