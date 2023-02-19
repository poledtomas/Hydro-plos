import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataX0=pd.read_csv("C:\\Users\\tposo\\gnuplot\\x0.dat", sep="\t", header=None, names=["x", "y", "z","e"])
dataY0=pd.read_csv("C:\\Users\\tposo\\gnuplot\\y0.dat", sep="\t", header=None, names=["x", "y", "z","e"])
dataZ0=pd.read_csv("C:\\Users\\tposo\\gnuplot\\z0.dat", sep="\t", header=None, names=["x", "y", "z","e"])

cislo=int(input('\n (1) x0 \n (2) y0 \n (3) z0 \n '))
if cislo==1:
    lvls = np.linspace(dataX0["e"].min(),dataX0["e"].max(), int(dataX0["e"].max()-dataX0["e"].min())+1)
    plt.tricontourf(dataX0["z"],dataX0["y"], dataX0["e"], cmap="magma", levels=lvls)  
    plt.colorbar(label="$\epsilon [GeV/fm^3]$")
    plt.xlabel("$\eta_s$")
    plt.ylabel("y[fm]")
    plt.show()

if cislo==2:
    lvls = np.linspace(dataY0["e"].min(),dataY0["e"].max(), int(dataY0["e"].max()-dataY0["e"].min())+1)
    plt.tricontourf(dataY0["z"],dataY0["x"], dataY0["e"], cmap="magma", levels=lvls)  
    plt.colorbar(label="$\epsilon [GeV/fm^3]$")
    plt.xlabel("$\eta_s$")
    plt.ylabel("x[fm]")
    plt.show()

if cislo==3:
    lvls = np.linspace(dataZ0["e"].min(),dataZ0["e"].max(), int(dataZ0["e"].max()-dataZ0["e"].min())+1)
    plt.tricontourf(dataZ0["x"],dataZ0["y"], dataZ0["e"], cmap="magma", levels=lvls)  
    plt.colorbar(label="$\epsilon [GeV/fm^3]$")
    plt.xlim(-5,5)
    plt.ylim(-10,10)    
    plt.xlabel("x[fm]")
    plt.ylabel("y[fm]")
    plt.show()