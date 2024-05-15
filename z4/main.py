from cProfile import label
import time
import mg
import statistics
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
    for n in range(5, 26, 1):
        for s in range(10,91,10):
            r = []
            for _ in range(10):
                g = mg.genCyklHamiltona(n,s)
                t = time.time()
                print(mg.RobertsFlores(g))
                r.append(time.time()-t)
            res.append((n,s, sum(r)/4))

    X,Y,Z = list(map(lambda x: x[0],res)),list(map(lambda x: x[1],res)),list(map(lambda x: x[2],res))
    print(X[0])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("macierz grafu cykl Hamiltona")
    ax.plot_surface(np.array(X).reshape((21, 9)), np.array(Y).reshape((21, 9)), np.array(Z).reshape((21, 9)), rstride=1, cstride=1 ) #type: ignore
    ax.set_xlabel('n')
    ax.set_ylabel('s')
    ax.set_zlabel('Time (s)')  #type: ignore
    plt.show()

def mgHamiltonAcy():
    res = []
    for n in range(5, 26, 1):
        for s in range(10,91,10):
            r = []
            for _ in range(10):
                g = mg.genCyklHamiltonaAcy(n,s)
                t = time.time()
                try:
                    print(mg.RobertsFlores(g))
                except: pass
                r.append(time.time()-t)
            res.append((n,s, sum(r)/4))

    X,Y,Z = list(map(lambda x: x[0],res)),list(map(lambda x: x[1],res)),list(map(lambda x: x[2],res))
    print(X[0])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("macierz grafu acykliczny Hamiltona")
    ax.plot_surface(np.array(X).reshape((21, 9)), np.array(Y).reshape((21, 9)), np.array(Z).reshape((21, 9)), rstride=1, cstride=1 ) #type: ignore
    ax.set_xlabel('n')
    ax.set_ylabel('s')
    ax.set_zlabel('Time (s)')  #type: ignore
    plt.show()


import robertsflores
def msHamilton():
    res = []
    for n in range(5, 26, 1):
        for s in range(10,91,10):
            r = []
            for _ in range(10):
                g = robertsflores.gen_graph(n,s)
                t = time.time()
                print(robertsflores.hamiltonian_cycle(g))
                r.append(time.time()-t)
            res.append((n,s, sum(r)/4))

    X,Y,Z = list(map(lambda x: x[0],res)),list(map(lambda x: x[1],res)),list(map(lambda x: x[2],res))
    print(X[0])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("macierz sąsiedztwa cykl Hamiltona")
    ax.plot_surface(np.array(X).reshape((21, 9)), np.array(Y).reshape((21, 9)), np.array(Z).reshape((21, 9)), rstride=1, cstride=1 ) #type: ignore
    ax.set_xlabel('n')
    ax.set_ylabel('s')
    ax.set_zlabel('Time (s)')  #type: ignore
    plt.show()

def msHamiltonAcy():
    res = []
    for n in range(5, 26, 1):
        for s in range(10,91,10):
            r = []
            for _ in range(10):
                g = robertsflores.gen_graph_acy(n,s)
                t = time.time()
                try:
                    print(robertsflores.hamiltonian_cycle(g))
                except: pass
                r.append(time.time()-t)
            res.append((n,s, sum(r)/4))

    X,Y,Z = list(map(lambda x: x[0],res)),list(map(lambda x: x[1],res)),list(map(lambda x: x[2],res))
    print(X[0])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("macierz sąsiedztwa acykliczny Hamiltona")
    ax.plot_surface(np.array(X).reshape((21, 9)), np.array(Y).reshape((21, 9)), np.array(Z).reshape((21, 9)), rstride=1, cstride=1 ) #type: ignore
    ax.set_xlabel('n')
    ax.set_ylabel('s')
    ax.set_zlabel('Time (s)')  #type: ignore
    plt.show()


def main():
    # ok()
    msHamiltonAcy()
    # msHamilton()

if __name__ == "__main__":  
    main()