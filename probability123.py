import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mean_h,std_h=165,7

#probability of being taller than 175cm
prob=1-norm.cdf(175,mean_h,std_h)#commulative distribution function
print(f'p(height>175cm)={prob:.4f}={prob*100:.1f}%')

#the 68-95-99.7 rule
print(f'68% of people: {mean_h-std_h:.0f}cm to {mean_h+std_h:.0f}cm')
print(f'95% of people: {mean_h-2*std_h:.0f}cm to {mean_h+2*std_h:.0f}cm')
print(f'99.7% of people: {mean_h-3*std_h:.0f}cm to {mean_h+3*std_h:.0f}cm')

