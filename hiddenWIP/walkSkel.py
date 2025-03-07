'''
Created on Sep 27, 2022

@author: Ellie
'''
from pymel.core import ls

def walk():
    jnt = getSel()
    for i in ls(jnt, type='joint', dag=True):
        print(i)
    
def getSel(testSel = None):
    sel = []
    if testSel == None:
        sel = ls(sl=True, type='joint')
        print(sel)
    else:
        sel = testSel
    if not len(sel) == 1:
        raise Exception('Select 1 joint')
    return sel[0]
