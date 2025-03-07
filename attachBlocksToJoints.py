'''
Created on Feb 20, 2023

@author: Ellie
'''
import pymel.core as pm

def attachBlockstoJoints():
	'''
	Attach blocks to joints with a corresponding names.

	Requires selection of block group first, and then first joint in hierarchy (root joint). 
	'''
	if len(pm.ls(sl=True)) != 2:
		pm.error("!!! Select only block group and joint hierarchy")
	elif not isinstance(pm.ls(sl = True)[1], pm.nodetypes.Joint):
		pm.error("!!! Select joint hierarchy second")
		
	blks = pm.ls(sl = True)[0].listRelatives(ad = True, typ = "transform")
	jnts = pm.ls(sl = True)[1].longName()
	pm.select(cl = True)
	
	for blk in blks:
		#ignores objects without _blk suffix and objects without a single corresponding joint
		if not blk.nodeName().endswith("_blk"):
			print("Skipping %s : not a block (does not end w _blk)" %(blk.nodeName()))
			continue
		checkJnt = pm.ls(typ = "joint", regex = (jnts.replace("|", "\\|") + "\|.*\|" + blk.nodeName()[:-4]))
		if not checkJnt:
			print("Skipping %s : has no matching joint" %(blk.nodeName()))
			continue
		elif len(checkJnt) != 1:
			print("Skipping %s : has multiple matching joints" %(blk.nodeName()))
			continue
		jnt = checkJnt[0]
		
        #delete any prior constraints on block and apply parent constraint
        if pm.ls(blk, dag = True, typ = "constraint", tl = 1):
			print("Deleting current constraints from %s" %(blk.nodeName()))
			pm.delete(pm.ls(blk, dag = True, typ = "constraint", tl = 1))
		pm.parentConstraint(jnt, blk, mo = True)
		
attachBlockstoJoints()