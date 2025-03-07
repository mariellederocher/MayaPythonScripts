'''
Created on Feb 18, 2023

@author: Ellie
'''
import pymel.core as pm

def makeCtrls():
	'''
	Make controls for joints, format and orient them correctly, parent their joints to them and arrange them in a control group. 
	
	Only creates controls for currently selected joints.
	'''

	dic = {} #for keeping track of objects associated w a joint
	ctrls = []
	sel = pm.ls(sl = True)
	pm.select(cl = True)
	
	for jnt in sel:
		#ignore objects that aren't joints or that are end joints
		if not isinstance(jnt, pm.nodetypes.Joint):
			pm.warning("%s is not a joint: Skipping" %(jnt.nodeName())) 
			continue
		if jnt.nodeName().endswith("_end"):
			continue
		
        #make and orient control shape and offset group
		ctrl = pm.circle(n = jnt.nodeName() + "_ctrl")[0]
		pm.rotate(ctrl, [0, 90, 0])
		pm.makeIdentity(ctrl, a = True)
		oGrp = pm.group(ctrl, n = ctrl.nodeName() + "_offset")
		pm.matchTransform(oGrp, jnt)
		dic[jnt] = [oGrp,ctrl]
	
    #add controls to a control group and constrain them appropriately to each other
    cGrp = pm.group(n = "ctrl_grp", em = True, w = True)
	pm.select(cl = True)
	
    for jnt in dic:
		if dic[jnt][1].nodeName() == "root_ctrl" or dic[jnt][1].nodeName() == "pelvis_ctrl":
			pm.parent(dic[jnt][0], cGrp)
			continue
		parJnt = pm.listRelatives(jnt, p = True)[0]
		parCtrl = dic[parJnt][1]
		pm.parent(dic[jnt][0], parCtrl)
		
	for jnt in dic:
		pm.parentConstraint(dic[jnt][1], jnt)
		
makeCtrls()