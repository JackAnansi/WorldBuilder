'''
Created on Jan 24, 2016

@author: Dan
'''

from weakref import proxy
import random
import solar

class Galaxy(object):
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
        
        self.solars = []
        
        self.create_solars()
        
    def get_num_solars(self):
        rng = random.Random(self.seed)
        return rng.randint(1, 100)
        
    def create_solars(self):
        rng = random.Random(self.seed)
        for _ in range(self.get_num_solars()):
            new_seed = str(self.seed) + str(rng.randint(0, 10000)) + "createsolar"
            s = solar.Solar(new_seed, self)
            self.solars.append(s)
            
if __name__ == "__main__":
    gal = Galaxy("616")
    print(len(gal.solars))
    print(gal.solars[0].planets[0].seed)