from cmath import sqrt
from math import factorial

def fact(n):
	i = 0
	factoriel = 1
	if n>=0:
		while i<n:
			factoriel *= n-i
			i +=1
		return factoriel
	else :
		print('ValueError')

def roots(a, b, c):
	delta = b**2 - 4*a*c
	racine = -b/(2*a) + sqrt(delta)/(2*a)
	if delta < 0:
		return 0
	if delta >= 0:
		return racine

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	pass

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
