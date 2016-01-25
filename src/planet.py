'''
Created on Jan 24, 2016

@author: Dan
'''

from weakref import proxy

class Planet(object):
    '''
    Represents a planet
    '''


    def __init__(self, seed=None, parent=None):
        '''
        Constructor
        '''
        self.seed = seed
        if (parent):
            self.parent = proxy(parent) #weak reference to parent
        else:
            self.parent = None