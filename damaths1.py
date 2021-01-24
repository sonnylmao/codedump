#P4 CR5 Challenge
from math import *

#part c (y intercept)

a = [0, 0.5*pi, pi, 1.5*pi, 2*pi]

for x in a:
    print("x:",round(5*cos(x + pi/12),2), "\ndy/dx:", round(-4*cos(2*x)/(5*sin(x + pi/12)),2), "\n")

#part c (x intercept)
b = [5*pi/12, 17*pi/12]

for x in b:
    print("y:",round(2*sin(2*x),2), "\ndy/dx:", round(-4*cos(2*x)/(5*sin(x + pi/12)),2), "\n")
