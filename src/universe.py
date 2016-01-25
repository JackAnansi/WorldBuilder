'''
Created on Jan 24, 2016

@author: Dan
'''

import random
import galaxy

class Universe(object):
    '''
    classdocs
    '''


    def __init__(self, seed=None):
        '''
        Constructor
        '''
        self.seed = seed
        
        self.galaxies = []
        
        self.create_galaxies()
        
    def get_num_galaxies(self):
        rng = random.Random(self.seed)
        return rng.randint(1, 1000)
        
    def create_galaxies(self):
        rng = random.Random(self.seed)
        for _ in range(self.get_num_galaxies()):
            new_seed = str(self.seed) + str(rng.randint(0, 10000)) + "creategalaxy"
            g = galaxy.Galaxy(new_seed, self)
            self.galaxies.append(g)
            
if __name__ == "__main__":
    uni = Universe("616")
    print(len(uni.galaxies))
    print(uni.galaxies[0].solars[0].planets[0].seed)
    
    # Test weakref
    print(uni.galaxies[0].solars[0].seed)
    print(uni.galaxies[0].solars[0].planets[0].parent.seed)