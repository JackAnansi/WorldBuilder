'''
Created on Jan 24, 2016

@author: Dan
'''

from weakref import proxy
import random
import planet

class Solar(object):
    '''
    classdocs
    '''


    def __init__(self, seed=None, parent=None):
        '''
        Constructor
        '''
        self.seed = seed
        if (parent):
            self.parent = proxy(parent) # weakref to parent
        else:
            self.parent = None
        
        self.planets = []
        
        self.create_planets()
        
    def get_num_planets(self):
        rng = random.Random(self.seed)
        return rng.randint(1, 10)
        
    def create_planets(self):
        rng = random.Random(self.seed)
        for _ in range(self.get_num_planets()):
            new_seed = str(self.seed) + str(rng.randint(0, 10000)) + "createplanet"
            p = planet.Planet(new_seed, self)
            self.planets.append(p)
            
if __name__ == "__main__":
    sol = Solar("616")
    print(len(sol.planets))
    print(sol.planets[1].seed)