import math as math
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import random
import sys as sys
import imageio

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
	sys.stdout.write("#" * int(20 - xpro) + "\n")
	sys.stdout.flush()

def dist(x1,x2,y1,y2,z1,z2):
	return np.power((x1-x2)**2+(y1-y2)**2+(z1-z2)**2,0.5)

def gravity(dots,k,t,a,b,m):
	dots1 = dots.copy()
	dots2 = dots1.copy()
	dots3 = dots2.copy()
	dots4 = dots3.copy()
	deltax=(0.5-dots[1])*(np.random.rand(len(dots)))/10
	deltay=(dots[0]-0.5)*(np.random.rand(len(dots)))/10
	deltaz=(np.random.rand(len(dots))-0.5)/10
	startProgress("Progress")
	k1 = k
	kwargs={ 'duration': 0.04 }
	with imageio.get_writer('Gravity.gif', mode='I', **kwargs ) as writer:
		timer = 0
		while timer<500:
			progress(100 * (500-timer) / 500)
			plt.style.use('dark_background')
			plt.title('Gravity Simulation')
			plt.xlabel('First Axis')
			plt.ylabel('Second Axis')
			plt.axis('equal')
			plt.xlim(0, 1)
			plt.ylim(0, 1)
			plt.axis('off')
			plt.text(0.2, -0.05, '['+'|'*int(50 * (timer) / 500) + ' '*int(50 * (500-timer) / 500)+ ']',fontsize=10)
			plt.plot([dots4[0],dots3[0]],[dots4[1],dots3[1]],c=(1.0,1.0,0.8,0.7),lw=0.5)
			plt.plot([dots3[0],dots2[0]],[dots3[1],dots2[1]],c=(1.0,1.0,0.8,0.8),lw=1.0)
			plt.plot([dots2[0],dots1[0]],[dots2[1],dots1[1]],c=(1.0,1.0,0.8,0.9),lw=1.5)
			plt.plot([dots1[0],dots[0]],[dots1[1],dots[1]],c=(1.0,1.0,0.8,1.0),lw=2.0)
			plt.plot(dots[0],dots[1],'.',c=(1.0,1.0,0.8,0.01),ms=48.0)
			plt.plot(dots[0],dots[1],'.',c=(1.0,1.0,0.8,0.05),ms=24.0)
			plt.plot(dots[0],dots[1],'.',c=(1.0,1.0,0.8,0.2),ms=12.0)
			plt.plot(dots[0],dots[1],'.',c=(1.0,1.0,0.8,0.8),ms=6.0)
			plt.plot(dots[0],dots[1],'.',c=(1.0,1.0,0.8),ms=3.0)
			plt.savefig('temp.png')
			plt.close()
			image = imageio.imread('temp.png')
			writer.append_data(image)
			dots4 = dots3.copy()
			dots3 = dots2.copy()
			dots2 = dots1.copy()
			dots1 = dots.copy()
			for i in range(0,len(dots)):
				corr = (0.5+t*dist(dots[0][:],dots[0][i],dots[1][:],dots[1][i],dots[2][:],dots[2][i]))
				deltax[i] = a*(np.sum(m*m*(dots[0][:]-dots[0][i])/corr/corr/corr))/m + b*deltax[i]
				deltay[i] = a*(np.sum(m*m*(dots[1][:]-dots[1][i])/corr/corr/corr))/m + b*deltay[i]
				deltaz[i] = a*(np.sum(m*m*(dots[2][:]-dots[2][i])/corr/corr/corr))/m + b*deltaz[i]
			dots[0] = dots[0][:]+deltax[:]
			dots[1] = dots[1][:]+deltay[:]
			dots[2] = dots[2][:]+deltaz[:]
			timer=timer+1

	endProgress()

def GO():
	dots=[]
	for i in range(0,100):
		dots.append([random.random(),random.random(),random.random()])
	dots=pd.DataFrame(dots)
	print("=== Simulating gravitational force ===")
	a=gravity(dots,2,100,0.4,0.9,30)

GO()
