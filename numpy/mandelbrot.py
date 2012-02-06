# Mandelbrot Set
# http://en.wikipedia.org/wiki/Mandelbrot_set
# http://mathworld.wolfram.com/MandelbrotSet.html

from numpy import *
import matplotlib.pyplot as plt

# For each point C = a + bi in the complex plane where -2 <= a <= 1 and -1 <= b <= 1, 
# iterate over the function znext = (zprev)**2 + C where z0 = C.
# The point is included in the set if abs(znext) < 2 after N iterations.

def in_mandelbrot_set(c, imax=10):
	
	z = c
	i = 0
	rmax = 2
	
	while ((i < imax) and (abs(z) < rmax)):
		z = (z ** 2) + c
		i += 1
	
	return (i == imax)

# bmin and bmax should not be complex.  They are used to create a complex C internally.
def plot_mandelbrot(amin, amax, bmin, bmax):
	
	rmax = 2
	
	for a in linspace(amin, amax, 50):
		print a
		for b in linspace(bmin, bmax, 50):
			c = a + (b * 1j)
			if (in_mandelbrot_set(c)):
				plt.plot(a, b, 'k,')

def elephant_valley():
	plot_mandelbrot(0.3, 0.4, -0.1, 0.1)
	plt.savefig("elephant_valley.png")

def seahorse_valley():
	plot_mandelbrot(-0.85, -0.65, 0, 0.2)
	plt.savefig("seahorse_valley.png")

def mandelbrot():
	plot_mandelbrot(-2, 1, -1.2, 1.2)
	plt.savefig("mandelbrot.png")

seahorse_valley()
#elephant_valley()
#mandelbrot()
