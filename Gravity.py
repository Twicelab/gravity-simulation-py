import math as math
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.mlab import griddata
import random
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.cluster import AgglomerativeClustering
import sys as sys

def startProgress(title):
	global xpro
	xpro=0
	print("         ____________________")
	sys.stdout.write("Progress:")
	sys.stdout.flush()

def progress(x):
	global xpro
	sys.stdout.write("#" * (int(x * 20 // 100 - xpro)))
	sys.stdout.flush()
	xpro = x * 20 // 100

def endProgress():
	global xpro
	sys.stdout.write("#" * (20 - xpro) + "\n")
	sys.stdout.flush()

def dist(x1,x2,y1,y2):
	return (x1-x2)**2+(y1-y2)**2

def gravity(dots,k,t,a):
	deltax=[0]*len(dots)
	deltay=[0]*len(dots)
	startProgress("Progress")
	k1 = k
	for u in range(0,t):
		progress(int(100*u/t))
		plt.title('Gravity Simulation')
		plt.xlabel('First Axis')
		plt.ylabel('Second Axis')
		plt.axis([0, 1, 0, 1])
		plt.plot(dots[0],dots[1],'w.',mec='r',mew=1.0,ms=8.0)
		plt.savefig(str(u)+'.png')
		plt.close()
		for i in range(0,len(dots)):
			corr = (0.5+dist(dots[0][:],dots[0][i],dots[1][:],dots[1][i]))
			corr = corr**k1
			deltax[i] = a*(np.sum(dots[0][:]/corr)/np.sum(1/corr)-dots[0][i])+(1-a)*deltax[i]
			deltay[i] = a*(np.sum(dots[1][:]/corr)/np.sum(1/corr)-dots[1][i])+(1-a)*deltay[i]
			dots[0][i] = dots[0][i]+deltax[i]
			dots[1][i] = dots[1][i]+deltay[i]
		if (t-u)>(t/5):
			k1=int(k*(1.0 - (u+1.0)/(t-(t/5)+1)))
		else:
			k1=0
	endProgress()

def GO():
	dots=[]
	for i in range(0,100):
		dots.append([random.random(),random.random()])
	dots=pd.DataFrame(dots)
	print("=== Simulating gravitational force ===")
	a=gravity(dots,128,500,0.05)

GO()
