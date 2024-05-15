import time
import mg

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import axes3d

plt.style.use('_mpl-gallery')

import numpy as np

def ok():

    plt.style.use('_mpl-gallery')

# Make data
    X, Y, Z = axes3d.get_test_data(0.05)

# Plot
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    print(X[0])
    ax.plot_wireframe(X,Y,Z, rstride=10, cstride=10)

    ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

    plt.show()


def mgHamilton():
    res = []
    for n in range(5, 21, 1):
        for s in range(10,100,10):
            g = mg.genCyklHamiltona(n,s)
            t = time.time()
            mg.RobertsFlores(g)
            res.append((n,s, time.time()-t))
    X,Y,Z = list(map(lambda x: x[0],res)),list(map(lambda x: x[1],res)),list(map(lambda x: x[2],res))
    print(X[0])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(np.array(X).reshape((16, 9)), np.array(Y).reshape((16, 9)), np.array(Z).reshape((16, 9)), rstride=1, cstride=1)
    ax.set_xlabel('n')
    ax.set_ylabel('s')
    ax.set_zlabel('Time (s)')
    plt.show()

    # plt.show()
    # plt.style.use('_mpl-gallery')
    # fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    # ax.plot_wireframe(np.array(X), np.array(Y), np.array(Z), rstride=10, cstride=10)

    # ax.set(xticklabels=[],
    #    yticklabels=[],
    #    zticklabels=[])

    # plt.show()

def main():
    # ok()
    mgHamilton()
    return 
    res = []
    for n in range(5, 21, 1):
        for s in range(10,100,10):
            g = mg.genCyklHamiltona(n,s)
            t = time.time()
            mg.RobertsFlores(g)
            res.append((n,s, time.time()-t))

    # ax = plt.figure().add_subplot(projection='3d')
    X,Y,Z = list(map(lambda x: x[0],res)),list(map(lambda x: x[1],res)),list(map(lambda x: x[2],res))
    # X, Y, Z = axes3d.get_test_data(0.05)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
    ax.plot_wireframe(X,Y,Z) 
    # ax.set_zlabel9a0
    # ax.axis("z")
    # ax.set_zlim(-1, 1) 
    # ax.zaxis.set_major_locator(LinearLocator(6))
    # ax.plot()
    
    plt.show()

if __name__ == "__main__":  
    main()