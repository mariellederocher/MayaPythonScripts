'''
Created on Sep 20, 2022

@author: Ellie

Requires the user to select the parent joint and then the corresponding block before running. Renames the block based on the joint, sets block origin at joint's position, and parent constrains block to joint.
-read user selection into a list
-check if the objects selected are a joint and a block
--increase usability by not having it be restricted to that... so maybe just any number of maya objects, with the parent first (or restrict the parent to a joint)
-rename child by removing "jnt" suffix from parent and setting that as the name + "blk"
--if I'm allowing for multiple types, perhaps sense the type of object and name accordingly, or ask user for suffix? 
-set child origin to parent's
-parent constrain
-perhaps create anims?
["body_C0",
"spine_C0_ik0",
"spine_C0_ik1",
"spine_C0_fk0",
"spine_C0_fk1",
"spine_C0_fk2",
"arm_L0_fk0",
"arm_L0_fk1",
"arm_L0_fk2",
"shoulder_L0",
"neck_C0_fk0",
"neck_C0_fk1,",
"neck_C0_head",
"leg_L0_upv",
"leg_L0_ik",
"foot_L0_tip",
"leg_L0_fk0",
"leg_L0_fk1",
"leg_L0_fk2",
"arm_L0_upv",
"arm_L0_ik"]
'''
from pymel.core import *
import types
from pymel.core.runtime import FreezeTransformations
from pymel.core.animation import parentConstraint

def orientblock():
	blk, jnt = ls(sl = True)[0], ls(sl = True)[1]
	par = blk.getParent()
	matchTransform(blk, jnt, piv = True)
	parent(blk, jnt)
	FreezeTransformations(blk)
	parent(blk, par)

def buildAmtr(comp):
	print(1)
	agrp = ls("|anim_grp")[0]
	def getbase(n):
		if n.endswith("_anim"): base = n[0,-5] 
		else: base = n
		return base
	for i in comp:
		if isinstance(i, str):
			base = getbase(i)
			ctl = ls(base + "_ctl")[0]
			if objExists("|anim_grp|" + i):
				anim = ls("|anim_grp|" + i)[0]
			else:
				anim = circle(n = i)[0]
				rotate(anim, [0,0,90])
				makeIdentity(anim)
				matchTransform(anim, ctl)
		else:
			anim = i 
			base = getbase(i.name().split("|")[-1])
			ctl = ls(base + "_ctl")[0]
		rename(anim, base + "_anim")
		makeIdentity(anim, s=True)
		ngrp = group(p=anim, n = i + "_null", em = True)
		parent(ngrp, agrp)
		mgrp = group(p=ngrp, n = i + "_manip", em = True)
		parent(anim, mgrp)
		makeIdentity(anim)
		try: 
			parentConstraint(anim, ctl, mo = True)
		except RuntimeError:
			try:
				pointConstraint(anim, ctl, mo = True)
			except RuntimeError:
				orientConstraint(anim, ctl, mo = True)

def getselect(exc = '', testsel = [], lf = False):
	if testsel:
		sel = testsel
	else:
		sel = ls(sl=True, dag = True, lf = lf)
	if not sel:
		raise Exception('No objects selected. ' + exc)
	return sel

def reattach():
	sel = getselect(lf = True)
	for i in sel:
		if not "_block" in i.name():
			print("%s is not a block or is named incorrectly. Skipping." % i.name())
			continue
		print(i)
		delparentconst(inp = i)
		jntname = i.name().split("_block")[0] + "_jnt"
		print("Look for " + jntname)
		jnt = ls(jntname, typ = "joint")
		if not jnt:
			print("%s has no corresponding joint. Skipping." % i.name())
			continue
		if len(jnt) > 1:
			print("%s has multiple corresponding joints. Skipping." % i.name())
			continue
		parentConstraint(jnt[0], i, mo = True)
		
def delparentconst(inp = []):
	sel = inp
	if not sel:
		sel = getselect(lf = True)
	for i in sel:
		for j in i.connections(t = "constraint"):
			delete(j)

def attach(testSel = None):
	sel = getselect(exc='Select 1 joint and at least 1 other object')
	_is_valid(sel)
	jnt = sel.pop(0)
	nameFromJoint(jnt, sel)
	orientToJoint(jnt, sel)
	parentToJoint(jnt, sel)
	print("success!")
	

#rename objs in list based on parent joint's name
def nameFromJoint(jnt, childs):
	baseName = jnt.name()
	if baseName[-4:] == "_jnt":
		baseName = baseName[0:-4]
	if len(childs) == 1:
		childs[0].rename(baseName + "_block")
		print("block is named " + childs[0].name())
	else:
	    for i in childs:
	    	i.rename(baseName + "_block_#")
	    	print("block is named " + i.name())
	    	
def orientToJoint(jnt, childs):
	"""
	Just modify>match transformations>match pivots 
	"""
	for i in childs:
		matchTransform(i, jnt, piv = True)
		FreezeTransformations(i)
	pass

def parentToJoint(jnt, childs):
	for i in childs:
		parentConstraint(jnt, i, mo = True)
	    	
def _is_valid(sel):
	if len(sel) < 2:
		raise Exception('Select 1 joint and at least 1 other object')
	if not isinstance(sel[0], nodetypes.Joint):
		raise Exception('Select joint first')
		

def test():
	JOINT = joint(name = "spine_1")
	BLOCK = polySphere()[0]
	BLOCK1 = polySphere()[0]
	BLOCK2 = polySphere()[0]
	#OTHER = camera(name = "cam")
	try:
		SEL = [JOINT, BLOCK]
		attach(testSel = SEL)
	finally:
		delete(JOINT)
		delete(BLOCK)
		delete(BLOCK1)
		delete(BLOCK2)
	
        
'''


def getSelectionV1(selection): #get user
    #selection = ls(selection=True)
    if selection.len == 2:
        if isinstance(selection[0], pmc.nodetypes.Joint) and isinstance(selection[1], pmc.nodetypes.Mesh):
            renameBlock(selection[0], selection[1])
            setOriginToJoint(selection[0], selection[1])
            constrainToJoint(selection[0], selection[1])
            return
    print("Need to select 1 joint and 1 block")
    return
def renameBlock(joint, block):
    return
def setOriginToJoint(joint, block):
    return
def constrainToJoint(joint, block):
    return
'''


'''
	sel = ls(sl=True, assemblies = True)
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
			makeIdentity(c, a = True)'''
		
		#attachBlocksToJoints.buildAmtr(["body_C0","spine_C0_ik0","spine_C0_ik1","spine_C0_fk0","spine_C0_fk1","spine_C0_fk2","arm_L0_fk0","arm_L0_fk1","arm_L0_fk2","shoulder_L0","neck_C0_fk0","neck_C0_fk1","neck_C0_head","leg_L0_upv","leg_L0_ik","foot_L0_tip","leg_L0_fk0","leg_L0_fk1","leg_L0_fk2","arm_L0_upv","arm_L0_ik"])
	#attachBlocksToJoints.buildAmtr(ls(sl = True)) 
'''
	for i in ls(sl=True):
		par = i.getParent(1)
		parname = par.name()
		newpar = i.getParent(2)
		sib = i.getSiblings()
		parent(sib[0], sib[1], i, newpar)
		delete(par)
		rename(i, parname)
		rename(sib[0], parname[0:-4] + sib[0].name()[0:6])
		rename(sib[1], parname[0:-4] + sib[1].name()[0:5])
		hide(sib)'''