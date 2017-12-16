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

def dist(x1,x2,y1,y2):
	return np.power((x1-x2)**2+(y1-y2)**2,0.5)

def gravity(dots,k,t,a,b):
	dots1 = dots.copy()
	dots2 = dots1.copy()
	dots3 = dots2.copy()
	dots4 = dots3.copy()
	deltax=[0]*len(dots)
	deltay=[0]*len(dots)
	startProgress("Progress")
	k1 = k
	kwargs={ 'duration': 0.04 }
	with imageio.get_writer('Gravity.gif', mode='I', **kwargs ) as writer:
		timer = 0
		while timer<100:
			progress(100 * (100-timer) / 100)
			#plt.style.use('dark_background')
			plt.title('Gravity Simulation')
			plt.xlabel('First Axis')
			plt.ylabel('Second Axis')
			plt.axis('off')
			#plt.xlim(0, 1)
			#plt.ylim(0, 1)
			#plt.text(0.27, -0.05, 'Timelapse acceleration: 1e+'+str(64.0*k/k1),fontsize=10)
			plt.plot([dots4[0][dots[2]==1],dots3[0][dots[2]==1]],[dots4[1][dots[2]==1],dots3[1][dots[2]==1]],c=(1.0,0.0,0.0,0.7),lw=0.5)
			plt.plot([dots3[0][dots[2]==1],dots2[0][dots[2]==1]],[dots3[1][dots[2]==1],dots2[1][dots[2]==1]],c=(1.0,0.0,0.0,0.8),lw=1.0)
			plt.plot([dots2[0][dots[2]==1],dots1[0][dots[2]==1]],[dots2[1][dots[2]==1],dots1[1][dots[2]==1]],c=(1.0,0.0,0.0,0.9),lw=1.5)
			plt.plot([dots1[0][dots[2]==1],dots[0][dots[2]==1]],[dots1[1][dots[2]==1],dots[1][dots[2]==1]],c=(1.0,0.0,0.0,1.0),lw=2.0)
			plt.plot(dots[0][dots[2]==1],dots[1][dots[2]==1],'.',c=(1.0,0.0,0.0,0.01),mew=1.0,ms=48.0)
			plt.plot(dots[0][dots[2]==1],dots[1][dots[2]==1],'.',c=(1.0,0.0,0.0,0.05),mew=1.0,ms=24.0)
			plt.plot(dots[0][dots[2]==1],dots[1][dots[2]==1],'.',c=(1.0,0.0,0.0,0.2),mew=1.0,ms=12.0)
			plt.plot(dots[0][dots[2]==1],dots[1][dots[2]==1],'.',c=(1.0,0.0,0.0,0.8),mew=1.0,ms=6.0)
			plt.plot(dots[0][dots[2]==1],dots[1][dots[2]==1],'.',c=(1.0,0.0,0.0),mew=1.0,ms=3.0)
			plt.plot([dots4[0][dots[2]==-1],dots3[0][dots[2]==-1]],[dots4[1][dots[2]==-1],dots3[1][dots[2]==-1]],c=(0.0,0.0,1.0,0.7),lw=0.5)
			plt.plot([dots3[0][dots[2]==-1],dots2[0][dots[2]==-1]],[dots3[1][dots[2]==-1],dots2[1][dots[2]==-1]],c=(0.0,0.0,1.0,0.8),lw=1.0)
			plt.plot([dots2[0][dots[2]==-1],dots1[0][dots[2]==-1]],[dots2[1][dots[2]==-1],dots1[1][dots[2]==-1]],c=(0.0,0.0,1.0,0.9),lw=1.5)
			plt.plot([dots1[0][dots[2]==-1],dots[0][dots[2]==-1]],[dots1[1][dots[2]==-1],dots[1][dots[2]==-1]],c=(0.0,0.0,1.0,1.0),lw=2.0)
			plt.plot(dots[0][dots[2]==-1],dots[1][dots[2]==-1],'.',c=(0.0,0.0,1.0,0.01),mew=1.0,ms=48.0)
			plt.plot(dots[0][dots[2]==-1],dots[1][dots[2]==-1],'.',c=(0.0,0.0,1.0,0.05),mew=1.0,ms=24.0)
			plt.plot(dots[0][dots[2]==-1],dots[1][dots[2]==-1],'.',c=(0.0,0.0,1.0,0.2),mew=1.0,ms=12.0)
			plt.plot(dots[0][dots[2]==-1],dots[1][dots[2]==-1],'.',c=(0.0,0.0,1.0,0.8),mew=1.0,ms=6.0)
			plt.plot(dots[0][dots[2]==-1],dots[1][dots[2]==-1],'.',c=(0.0,0.0,1.0),mew=1.0,ms=3.0)
			plt.plot(0.5,0.5,'k.',ms=12.0)
			plt.plot(0.5,0.5,'w.',ms=9.0)
			plt.plot(0.5,0.5,'k.',ms=6.0)
			plt.savefig('temp.png')
			plt.close()
			image = imageio.imread('temp.png')
			writer.append_data(image)
			dots4 = dots3.copy()
			dots3 = dots2.copy()
			dots2 = dots1.copy()
			dots1 = dots.copy()
			for i in range(0,len(dots)):
				corr = 1+t*(dist(dots[0][:],dots[0][i],dots[1][:],dots[1][i]))				
				deltax[i] = a*(np.sum((-1)*dots[2][:]*dots[2][i]*(dots[0][:]-dots[0][i])/corr/corr/corr)) + deltax[i]
				deltay[i] = a*(np.sum((-1)*dots[2][:]*dots[2][i]*(dots[1][:]-dots[1][i])/corr/corr/corr)) + deltay[i]
				dots[0][i] = dots[0][i]+deltax[i]
				dots[1][i] = dots[1][i]+deltay[i]
			if np.sum(np.asarray(deltax)*np.asarray(deltax)+np.asarray(deltay)*np.asarray(deltay))<1:
				timer=timer+1
			else:
				timer=0
			print(timer)
	endProgress()

def GO():
	dots=[]
	for i in range(0,100):
		dots.append([random.random(),random.random(),2*(i%2)-1])
	dots=pd.DataFrame(dots)
	print("=== Simulating gravitational force ===")
	a=gravity(dots,2,10,0.1,0.1)

GO()
