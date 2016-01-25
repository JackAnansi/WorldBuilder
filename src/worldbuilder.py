'''
Created on Jan 18, 2016

This file is deprecated. It is only used as a reference.

@author: Dan
'''
from numpy.random import randn
from numpy import clip
import random

class WorldBuilder(object):
    
    def __init__(self, seed=None):
        random.seed(seed)
        w = clip((randn(100) + 2), 0, 4).astype(int)
        h = clip((randn(100) + 2), 0, 4).astype(int)
        
        # self.universe[(x, y)]
        self.universe = {}
        
        for x in range(0, 5):
            for y in range(0, 5):
                self.universe[(x, y)] = []
                
        for i in range(100):
            # FIXME:
            # Instead of appending a number, append a seed
            # Each seed is a galaxy seed
            self.universe[(w[i], h[i])].append(i)
            
    def draw_2d(self):
        print("Universe map")
        print("Showing the distribution of galaxies")
        
        for x in range(0, 5):
            lengths = [len(self.universe[(x, y)]) for y in range(0, 5)]
            print("{0} - {1} - {2} - {3} - {4}".format(*lengths))
        
if __name__ == "__main__":
    wb = WorldBuilder("616")
    wb.draw_2d()