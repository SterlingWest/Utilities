eqn = raw_input()
while(len(eqn) > 0 and eqn[-1]=='\n'): eqn = eqn[:-1]
eqn = eqn.split('=')
eqn = eqn[0] + '-' + '(' + eqn[1] + ')'

def solve(f):
	tol = 0.0000001
	p0 = 0.
	p1 = 1.
	i = 0
	while(abs(f(p0)) > tol and abs(p1-p0) > tol and i < 10000):
		p0,p1  = p0 - f(p0)*(p0-p1)/(f(p0)-f(p1)), p0
		i += 1
	if(i == 10000): return None
	return round(p0,5)

f = lambda x: eval(eqn)
print solve(f)
