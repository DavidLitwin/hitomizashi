# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 10:45:39 2022

@author: dgbli
"""

import numpy as np
import matplotlib.pyplot as plt

def return_true(n):
    x = []
    for i in range(n):
        if i%2==0:
            x.append(i)
            x.append(i+1)
        else:
            x.append(None)
    return x

def return_false(n):
    x = []
    for i in range(n):
        if i%2==1:
            x.append(i)
            x.append(i+1)
        else:
            x.append(None)
    return x

class Hitomizashi:
    
    def __init__(self, rows, columns, color='k', linewidth=1.0, capstyle='projecting'):
        
        self.a = columns
        self.b = rows
        self.Na = len(self.a)
        self.Nb = len(self.b)
        
        self.color = color
        self.lw = linewidth
        self.cs = capstyle
        
    def draw(self):
        
        fig, ax = plt.subplots()

        #horizontals:
        for i in range(self.Na):
            if b[i] == True:
                x = np.array(return_true(self.Na))
                ax.plot(x,i*np.ones(len(x)), color=self.color, linewidth=self.lw, solid_capstyle=self.cs)
            elif b[i] == False:
                x = np.array(return_false(self.Na))
                ax.plot(x,i*np.ones(len(x)), color=self.color, linewidth=self.lw, solid_capstyle=self.cs)
            else:
                raise TypeError('Input should be boolean')
                
                
        #verticals:
        for i in range(len(a)):
            if a[i] == True:
                y = np.array(return_true(self.Nb))
                ax.plot(i*np.ones(len(y)), y, color=self.color, linewidth=self.lw, solid_capstyle=self.cs)
            elif a[i] == False:
                y = np.array(return_false(self.Nb))
                ax.plot(i*np.ones(len(y)), y, color=self.color, linewidth=self.lw, solid_capstyle=self.cs)
            else:
                raise TypeError('Input should be boolean')

        ax.set_axis_off()


if __name__ == "__main__":
    a = np.random.rand(25) > 0.5
    b = np.random.rand(25) > 0.5
    
    hz = Hitomizashi(a,b, linewidth=4, color='dodgerblue', capstyle='round')
    hz.draw()
