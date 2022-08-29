# Gaussian-heat-source
3D Conical Gaussian Heat Source Model 

Simple chunk of code to obtain a 3D Conical Gaussian to use in a Finite Element Method Simulation Analysis of a Laser Welding

![alt text](https://github.com/Santiago221/Gaussian-heat-source/blob/master/img2.jpg?raw=true)

The Code Outpots a dataframe with the X,Y and Z positions of the gaussian heat source, the radius of the spot at any giveng Z position and the heat output for the same position 

![alt text](https://github.com/Santiago221/Gaussian-heat-source/blob/master/img1.jpg?raw=true)

**3D Gaussian Distribution**

$$Q(X,Y,Z) = Qo\cdot exp\left(-\frac{X^2 + Y^2}{R\left( Z \right)^2}  \right)$$

$$R\left( Z \right) = R_{min} + (Z -Z_{min})\cdot\frac{(R_{max}-R_{min})}{(Z_{max}-Z_{min})}$$

