# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Qo(T, sigma = 5.67e-8 ):
    """
    :param T: Temperature [K]
    :param sigma:  Stefan–Boltzmann Constant [W/m^2K^4]
    :return: Heat Flux [W/m^2]
    """
    return sigma*T**4

def conical_heat_source(r_vet,z_vet, n = 100):
    Z = np.linspace(z_vet[0],z_vet[1],n)
    R = []
    for i,z in enumerate(Z):
        R.append(r_vet[0] + (z_vet[1] - z)*(r_vet[1]-r_vet[0])/(z_vet[1] - z_vet[0]))
    return R, Z

def Gaussian_Shape(Qo,r):
    pass

if __name__ == '__main__':
    n = 100
    n2 = 1.5
    # Heat Source
    T = 1500

    # Cone Size
    r_max = 0.833
    r_min = 0.4
    z_max = 0
    z_min = 4
    r_vet = [r_max,r_min]
    z_vet = [z_max,z_min]
    R, Z = conical_heat_source(r_vet, z_vet, n=100)
    X = np.linspace(-r_max * n2, r_max * n2, n)
    Y = np.linspace(-r_max * n2, r_max * n2, n)