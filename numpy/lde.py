# Logistic difference equation
# http://en.wikipedia.org/wiki/Logistic_map
# http://www.stsci.edu/~lbradley/seminar/logdiffeqn.html
#
# usage:
# python lde.py; open lde.png
#

from numpy import *
import matplotlib.pyplot as plt

def lde_step(r, y):
	return r * y * (1 - y)

def lde(r, y0, num=1000, i0=0):

	# Build the result array, which is num rows by two cols.
	l = num * 2;
	result = linspace(0, (l - 1), l)
	result = result.reshape(num, 2)
	
	y = y0
	
	for i in linspace(i0, i0 + num, num, False):
		y = lde_step(r, y)
		result[i - i0,0] = i
		result[i - i0,1] = y
	
	return result
	
# Plot n points for each value of r in the range [rmin, rmax].

# Classic view starts out simple...
rmin = 2.7
rmax = 4.0
n = 100

# Good detail of the chaotic region.
#rmin = 3.57
#rmax = 4
#n = 500

rstep = 0.005
i = 0
y = 0.8

for r in arange(rmin, rmax, rstep):
	result = lde(r, y, n, i)
	l = alen(result)
	i += l
	y = result[l-1,1]
	plt.plot(result[:,0], result[:,1], 'k,')

plt.savefig("lde.png")
