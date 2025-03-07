'''
Created on February 20, 2023

@author: Ellie
'''
import maya.cmds as cmds
import pymel.core as pm

# Freeze all transformations
def freezeTransforms():
	pm.makeIdentity(a = True)

# Select only joints
def selectJnts():
	pm.select(pm.listRelatives(typ = "joint", ad=True, f = True))

# Select only constraints
def selectConstr():
	pm.select(pm.listRelatives(typ = "constraint", ad=True, f = True))

# Unlock Controls
def unlockCtrls():
	selList = pm.ls(sl=1, ap=1, tr=1) #sl=1 means check for selection, ap=1 means return full path names (not essential), tr=1 means return only transforms (no shape nodes)

	for sel in selList:
		pm.setAttr((sel + ".tx"), k=1, l=0) #k=1 means make the attributes keyable, 1=0 unlocks attributes
		pm.setAttr((sel + ".ty"), k=1, l=0)
		pm.setAttr((sel + ".tz"), k=1, l=0)
		
		pm.setAttr((sel + ".rx"), k=1, l=0)
		pm.setAttr((sel + ".ry"), k=1, l=0)
		pm.setAttr((sel + ".rz"), k=1, l=0)

# Used to assign all selected ctrls as parents of their respective joints	
def parentJntsToCtrls():
	for sel in pm.ls(sl=True):
		jnt = pm.ls(sel.name()[:-5])
		pm.parentConstraint(sel,jnt)
	
# turns off local axis display on all selected objects (may error if constraints, etc are selected)
def turnOffLocalAxis():
	for sel in pm.ls(sl=True):
		sel.displayLocalAxis.set(0)
	
# add suffix to selected objects
def addSuffix(suf):
	if not suf:
		pm.error("!!! No suffix input")
	for sel in pm.ls(sl=True):
		if sel.nodeName().endswith(suf):
			print("Skipping %s : already has %s suffix" %(sel.nodeName(), suf))
			continue
		pm.rename(sel, sel.nodeName() + suf)
		
	