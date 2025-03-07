'''
Created on Sep 27, 2022

@author: Ellie
'''

class Skeleton(object):
    '''
    classdocs
    '''


    def __init__(self, root):
        '''
        Constructor
        '''
        self.root = root
        self.hierarchy = (['root', root]
                          ['spine_1', None]
                          ['spine_2', None]
                          ['spine_3', None]
                          ['neck_1', None]
                          ['neck_2', None]
                          ['head', None]
                          ['left_clav', None]
                          ['left_uparm', None]
                          ['left_lowarm', None]
                          ['left_hand', None]
                          ['right_clav', None]
                          ['right_uparm', None]
                          ['right_lowarm', None]
                          ['right_hand', None]
                          ['left_upleg', None]
                          ['left_lowleg', None]
                          ['left_foot', None]
                          ['left_toe', None]
                          ['right_upleg', None]
                          ['right_lowleg', None]
                          ['right_foot', None]
                          ['right_toe', None])
        
    @classmethod
    def construct_skeleton(self, root):
        def nextjoint(jnt):
            #get list of children
            pass
        for jnt in self.hierarchy:
            #search for name of joint in hierarchy and assign to key
            pass
        pass
    
    def make_biped_ctrls(self, root):
        pass