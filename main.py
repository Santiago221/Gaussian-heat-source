# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def Qo(T, sigma = 5.67e-8 ):
    """
    :param T: Temperature [K]
    :param sigma:  Stefan–Boltzmann Constant [W/m^2K^4]
    :return: Heat Flux [W/m^2]
    """
    return sigma*T**4

def conical_heat_source(r_vet,z_vet, n = 100):
    """
    :param r_vet: Radius limit vector [mm]
    :param z_vet: Height limit vector [mm]
    :param n:     number of points [-]
    :return: Radius Vector [mm], Z Vector [mm]
    """
    Z = np.linspace(z_vet[0],z_vet[1],n)
    R = []
    for i,z in enumerate(Z):
        R.append(r_vet[0] + (z_vet[1] - z)*(r_vet[1]-r_vet[0])/(z_vet[1] - z_vet[0]))
    return R, Z

def Gaussian_Shape(Qo,X,Y,Z,R):
    '''
    :param Qo:  Heat Flux [W/m^2]
    :param X:   X Vector [mm]
    :param Y:   Y Vector [mm]
    :param Z:   Z Vector [mm]
    :param R:   Radius Vector [mm]
    :return:    Results Dataframe[X, Y, Z, R, Q]
    '''
    Q = []
    for i,z in enumerate(Z):
        for ii,x in enumerate(X):
            for iii,y in enumerate(Y):
                Q.append([x, y, z, R[i]])
    df = pd.DataFrame(Q, columns=['X', 'Y', 'Z', 'R'])
    df['Q'] = Qo*np.exp(- (df['X']**2 + df['Y']**2)/df['R']**2)
    return df

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
    R, Z = conical_heat_source(r_vet, z_vet, n=25)
    X = np.linspace(-r_max * n2, r_max * n2, n)
    Y = np.linspace(-r_max * n2, r_max * n2, n)

    df = Gaussian_Shape(Qo(T),X,Y,Z,R)
    df.to_csv('3D_Gaussian.csv')

    A = df[df['Z'] == 4]
    B = df[df['Z'] == 0]


    fig = plt.figure()
    ax = plt.axes(projection="3d")
    a1 = ax.scatter3D(A['X'],A['Y'],A['Z'],c = A['Q'],cmap = 'viridis',label = 'Z = 4')
    a1 = ax.scatter3D(B['X'], B['Y'], B['Z'], c=B['Q'], cmap='viridis',label = 'Z = 0')
    ax.set_xlabel('x [mm]')
    ax.set_ylabel('y [mm]')
    ax.set_zlabel('z [mm]')
    fig.colorbar(a1, ax=ax, shrink=1, aspect=25,orientation = 'horizontal')
    plt.show()
