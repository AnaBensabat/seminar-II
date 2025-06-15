import matplotlib.pyplot as plt
import numpy as np
import random as rd
from celluloid import Camera

def theta(vx, vy):
    return np.arctan2(vy/vx)

# system dimensions
dimX = 20
dimY = dimX

# parameters
N = 100 # number of birds
v = 0.4 # velocity
R = 5 # radius of interaction
T = 500 # time of simulation
eta = np.pi/3

# data structures
xs = np.random.random(N)*dimX
ys = np.random.random(N)*dimX
thetas = np.random.uniform(-eta, eta,N)

camera = Camera(plt.figure())

# evolve
for i in range(T):

    for bird in range(N):

        av_theta = 0
        neighbours = 0
        
        for other_bird in range(N):

            if (((xs[bird]-xs[other_bird])**2+(ys[bird]-ys[other_bird])**2)<R**2):
                av_theta += thetas[other_bird]
                neighbours += 1

        av_theta /= neighbours
        thetas[bird] = av_theta + rd.uniform(-eta, eta)
        xs[bird] = (xs[bird] + v*np.cos(thetas[bird]))%dimX
        ys[bird] = (ys[bird] + v*np.sin(thetas[bird]))%dimY


    plt.scatter(xs,ys,c='black')
    camera.snap()

anim = camera.animate()
anim.save('viseck.mp4')



