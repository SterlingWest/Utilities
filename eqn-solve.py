import random
def secant_method(f):
	i, p0, p1, tol = 0.,80.,79.,0.000000
	while(abs(p1-p0) > tol and i < 10000):
		if(i%1000 == 0):
			p0 = random.random()*200000 -100000
			p1 = p0+1
		p0,p1,i  = p0 - f(p0)*(p0-p1)/(f(p0)-f(p1)), p0,i+1
	if(i == 100000): return 'Failure'
	return round(p0,5)
eqn = '-'.join(['('+e+')' for e in raw_input().split('=')])
f = lambda x: eval(eqn)
print secant_method(f)
