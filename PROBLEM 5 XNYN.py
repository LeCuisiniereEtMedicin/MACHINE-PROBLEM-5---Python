import math as m
import matplotlib.pyplot as show
y = []
x = []
print('Enter a function in terms of n')
print("Use put 'm.' in front of trig functions and identities, ex. m.cos(n), m.pi ")
xn = input()
a = list(range(0,200))
for n in a:
    x.append(eval(xn))
for n in a:
    if n == 0:
        yn = -1.5*x[n] + 2*x[n+1]-0.5*x[n+2]
        y.append(yn)
        continue
    if  n<=198:
        yn = 0.5*x[n+1] - 0.5*x[n-1]
        y.append(yn)
        continue
    if n == 199:
        yn = 1.5*x[n] - 2*x[n-1] + 0.5*x[n-2]
        y.append(yn)
        
show.plot(x, color = 'r',label='x(n)')
show.plot(y,label='y(n)')
show.xlabel('n')
show.ylabel('f(n)')
show.legend()