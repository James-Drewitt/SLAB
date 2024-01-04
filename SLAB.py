# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 15:16:41 2023

@author: James
"""
import numpy as np
import matplotlib.pyplot as plt

def Ass(twotheta, mu, L, alpha):
    calc = np.exp(-mu * L * (np.sin(alpha) / np.sin(twotheta + alpha))) * (
            (np.exp(((mu * (np.sin(alpha) / np.sin(twotheta + alpha))) - mu) * L) - 1) /
            ((mu * (np.sin(alpha) / np.sin(twotheta + alpha)) - mu) * L))
    return calc

# parameters
t = 1 # thickness in mm

a = 0.163E-2 # Ga
#a = 310.5E-6  # absorption length in m #Pb
#a = 278.5E-6  # absorption length in m #Hg

# generate range of twotheta angles
twotheta_values = np.linspace(0.01, 30, 60)

alpha = 0
alpha = 90 + alpha
beta = 180 - (alpha)
gamma = 180 - 90 - beta

print(f"alpha = {alpha}, beta = {beta}, gamma={gamma}")

alpha = np.radians(alpha)
gamma = np.radians(gamma)

t = t / 1000
mu = 1 / a 

L = t / np.cos(gamma)

print(f"L = {L}")

Ass_values = [Ass(np.radians(twotheta), mu, L, alpha) for twotheta in twotheta_values]

# Plot the results
plt.plot(twotheta_values, Ass_values, label='As,s (twotheta)')
plt.xlabel('TwoTheta')
plt.ylabel('As,s (twotheta)')
plt.title('Self-shielding attenuation factor')
plt.legend()
plt.grid(True)
plt.show()