import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
import scipy.integrate
import scipy.stats
import matplotlib.mlab as mlab
import math

## This function performs interpolation on points from a histogram of randomly generated data. This gives an estimated pdf of the distribution.
def bin_interpolation(X,N):
    y,x = np.histogram(X,bins=N)# creates the bins to interpolate
    y = y/10000 #the creates proportions instead of counts

    # the following finds the mid points of the bins:
    mid_points = np.zeros(N)
    d=x[1]-x[0]
    for i in range(N):
        mid_points[i] = (x[i+1]+x[i])/2

    # add two extra end points on each side of the interval
    mid_points = np.concatenate((mid_points[0]-d,mid_points,mid_points[N-1]+d),axis=None) #adds a x-intercept to the data
    y = np.concatenate((0,y,0),axis=None)#adds the corresponding y values = 0 to the two extra points


    f1 = scipy.interpolate.CubicSpline(mid_points,np.sqrt(y)) # cubics spline interpolation on (x,y^.5), need a pdf to be positive
    f_1 = lambda x: (f1(x))**2 #square the intepolation
    integral = scipy.integrate.quad(f_1,min(mid_points),max(mid_points))[0]# constant scale
    intpol = lambda x: f_1(x)/integral# divide function by constant, this is the returned function
    return intpol


## This function performs polynomial regression on points from a histogram of randomly generated data. This gives an estimated pdf of the distribution.
def bin_poly_approx(X,N,n_deg):
    y,x = np.histogram(X,bins=N)# creates the bins to interpolate
    y = y/10000#the creates proportions instead of counts
    
    # the following finds the mid points of the bins:
    mid_points = np.zeros(N)
    d=x[1]-x[0]
    for i in range(N):
        mid_points[i] = (x[i+1]+x[i])/2
    mid_points = np.concatenate((mid_points[0]-d,mid_points,mid_points[N-1]+d),axis=None) #adds a x-intercept to the data
    y = np.concatenate((0,y,0),axis=None)

    # the following does the least squares poly approximation
    f_coef = np.polyfit(mid_points,np.sqrt(y),n_deg)
    f_coef = np.flip(f_coef,0)
    f = lambda x: (sum(np.multiply((np.power(x, np.arange(n_deg+1))),f_coef)))**2
    integral = scipy.integrate.quad(f,min(mid_points),max(mid_points))[0]
    poly = lambda x: f(x)/integral # this is the returned function after scaling
    return poly

