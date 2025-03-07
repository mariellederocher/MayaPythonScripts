'''
Created on Sep 25, 2022

@author: Ellie
'''
#from MayaDev import attachBlocksToJoints 
#from MayaDev import walkSkel 
import importlib
from pymel.core import *

if __name__ == '__main__':
	'''sel = ls(sl=True, assemblies = True)
	jnt = sel.pop(0)
	importlib.reload(walkSkel)
	walkSkel.walk()

	importlib.reload(attachBlocksToJoints)
	attachBlocksToJoints.attach()
	
	def getselect(exc = '', testsel = [], lf = False):
		if testsel:
			sel = testsel
		else:
			sel = ls(sl=True, dag = True, lf = lf, typ = "constraint")
		if not sel:
			raise Exception('No objects selected. ' + exc)
		return sel
		
	def reattach():
		delparentconst()
		sel = getselect(lf = True)
		print(sel)
		for i in sel:
			if not "_block" in i.name():
				print("%s is not a block or is named incorrectly. Skipping." % i.name())
				continue
				
	def delparentconst(inp = []):
		sel = inp
		if not sel:
			sel = getselect(lf = True)
		for i in sel:
			if i.connections(t = "constraint"):
				delete(i, )
	
	reattach()'''
	
	'''parentConstraint(sel, nur[0], mo = False)
	
	makeIdentity(sel, a = True)
	sel = ls(sl = True)
	delete(sel[0], cn=True)
	sell = ls("finger_L0_fk0")
	sel = sell[0]
	delete(sell[0], cn=True)'''
	'''
	
	a = 0
	b = 1
	for i in range(4):
		for j in range(3):
			sell = ls("finger_L%d_fk%d" % (i, j))
			sel = sell[0]
			print("grp " + sel)
			if a == 0 :
				nur = ls("basecv", "tipcv", "loftedSurface%d" % b)
			else :
				nur = ls("basecv%d" % a, "tipcv%d" % a, "loftedSurface%d" % b)
			a+=1 ; b+=1
			print("nur " + ''.join(e.name() + " " for e in nur))
			parentConstraint(nur[0], sel, mo = False)
			delete(sel.name() + "_parentConstraint1")
			makeIdentity(sel, a = True, t = True)
			parent(nur[0], nur[1], nur[2], sel)
			for c in nur:
				makeIdentity(c, a = True)
				
				
				
				
body_C0_ctl
spine_C0_ik0_ctl
spine_C0_fk0_ctl
spine_C0_fk1_ctl
spine_C0_fk2_ctl
spine_C0_ik1_ctl
arm_L0_fk0_ctl
arm_L0_fk1_ctl
arm_L0_fk2_ctl
shoulder_L0_ctl
neck_C0_fk0_ctl
neck_C0_fk1_ctl
neck_C0_head_ctl
leg_L0_upv_ctl
leg_L0_ik_ctl
foot_L0_tip_ctl
leg_L0_fk0_ctl
leg_L0_fk1_ctl
leg_L0_fk2_ctl
arm_L0_upv_ctl
arm_L0_ik_ctl
'''
	
#I used this to reorientfinger controls after mirror them
sel = ls(sl=True)[0]
pickWalk(d='down')
pos = ls(sl=True)[0]
pickWalk(d='down')
ctrl = ls(sl=True)[0]
parent(ctrl, w=True)
pickWalk(d='down')
pickWalk(d='left')
nex = ls(sl=True)[0]
parent(nex, w=True)
jnt = ls(sel.name()[:-12])
matchTransform(sel, jnt)
matchTransform(ctrl, sel, pos=True)
parent(ctrl, pos)
makeIdentity(ctrl, a=True)
parent(nex, ctrl)
sel=nex
'''pickWalk(d='down')
pos = ls(sl=True)[0]
pickWalk(d='down')
ctrl = ls(sl=True)[0]
parent(ctrl, w=True)
pickWalk(d='down')
pickWalk(d='left')
nex = ls(sl=True)[0]
parent(nex, w=True)
jnt = ls(sel.name()[:-12])
matchTransform(sel, jnt)
matchTransform(ctrl, sel, pos=True)
parent(ctrl, pos)
makeIdentity(ctrl, a=True)
parent(nex, ctrl)
sel=nex'''
pickWalk(d='down')
pos = ls(sl=True)[0]
pickWalk(d='down')
ctrl = ls(sl=True)[0]
parent(ctrl, w=True)
jnt = ls(sel.name()[:-12])
matchTransform(sel, jnt)
matchTransform(ctrl, sel, pos=True)
parent(ctrl, pos)
makeIdentity(ctrl, a=True)

		
		
'''#has options for what kinds of joints may be identified and therefore what suffixes to look for - add more for extended usability
#right now I'm passing a string, should I instead be passing an object?
def getRootName(name, isJoint = True):
	if (isJoint=True and name.endswith('_jnt'):
		rootName = name[:-4]'''
	
		 
	
	a = 12
	b = 13
	for j in range(3):
		sell = ls("thumb_L0_fk%d" % j)
		sel = sell[0]
		print("grp " + sel)
		if a == 0 :
			nur = ls("basecv", "tipcv", "loftedSurface%d" % b)
		else :
			nur = ls("basecv%d" % a, "tipcv%d" % a, "loftedSurface%d" % b)
		a+=1 ; b+=1
		print("nur " + ''.join(e.name() + " " for e in nur))
		parentConstraint(nur[0], sel, mo = False)
		delete(sel.name() + "_parentConstraint1")
		makeIdentity(sel, a = True, t = True)
		parent(nur[0], nur[1], nur[2], sel)
		for c in nur:
			makeIdentity(c, a = True)