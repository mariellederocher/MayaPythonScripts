'''
Created on Jan 24, 2023

@author: Ellie

Functions for automatically making roll joints
'''
import pymel.core as pm

def makeRollJoints(isArm = True, isLeg=False):
	selList = pm.ls(sl = True)
	
	print(selList)
	upJnt = selList[0]
	midJnt = selList[1]
	lowJnt = selList[2]
	side = upJnt.name()[0] 
	if isArm:
		mult = pm.createNode('multiplyDivide', n = side + "_arm_roll_multiply")
		makeBicepRoll(upJnt, midJnt, side, mult)
		makeWristRoll(midJnt, lowJnt, side, mult)
	if isLeg:
		#todo
		pass

def makeBicepRoll(uparmJnt, lowarmJnt, side, mult):
	'''
	Makes roll joint for a bicep. 
	'''
	pm.select(uparmJnt)
	uparmRoll = pm.joint(n = uparmJnt.name() + "_roll") # create joint
	bicepRoll = pm.joint(n = side + "_bicep_roll",
		p = lowarmJnt.getTranslation()/2, r = True)
	pm.Attribute.set(mult.input2X, .5)
	pm.Attribute.connect(lowarmJnt.rotateX, mult.input1X)
	pm.Attribute.connect(mult.outputX, bicepRoll.rotateX)
	uparmAim = pm.spaceLocator(n = side + "_upperarm_roll_aim")
	temp = pm.parentConstraint(uparmJnt, uparmAim)
	uparmAim.translateBy((0, 0, 20))
	pm.delete(temp)
	pm.aimConstraint(lowarmJnt, uparmRoll, u = (0, 0, -1), wut = 'object', wuo = uparmAim.name())
	pm.select(uparmJnt)
	uparmFollow = pm.joint(n = side + "_upperarm_follow")
	bicepFollow = pm.joint(n = side + "_bicep_follow", p = bicepRoll.getTranslation(), r = True)
	uparmFollow.translateZ.set(-10)
	pm.parent(uparmFollow, w = True)
	pm.parent(uparmAim, uparmFollow)
	uparmRollIK = pm.animation.ikHandle(n = side + "_upperarm_roll_ik", sj = uparmFollow, ee = bicepFollow, sol = 'ikSCsolver', shf = False)[0]
	pm.matchTransform(uparmRollIK, lowarmJnt)
	pm.parent(uparmRollIK, lowarmJnt)
    
def makeWristRoll(lowarmJnt, wristJnt, side, mult):
	'''
	Makes roll joint for a wrist
	'''
	pm.select(lowarmJnt)
	forearmRoll = pm.joint(n = side + "_forearm_roll",
		p = wristJnt.getTranslation()/2, r = True) 
	pm.select(lowarmJnt)
	wristRoll = pm.joint(n = side + "_wrist_roll",
		p = wristJnt.getTranslation(), r = True)
	pm.Attribute.set(mult.input2Y, .5)
	pm.Attribute.connect(wristRoll.rotateX, mult.input1Y)
	pm.Attribute.connect(mult.outputY, forearmRoll.rotateX)
	wristAim = pm.spaceLocator(n = side + "_wrist_roll_aim")
	pm.matchTransform(wristAim, wristJnt)
	pm.parent(wristAim,wristJnt)
	wristAim.translateBy((0, 0, -20))
	pm.aimConstraint(lowarmJnt, wristRoll, aim = (-1, 0, 0),  u = (0, 0, -1), wut = 'object', wuo = wristAim.name())

		
'''
to do:
for arm:
create 4 joints - upper arm, bicep, forearm, wrist
put bicep in between translate of upper and lower arm joints and set axis to match upper arm, then freeze rotation
duplicate upper arm and bicep roll joints and put them a little behind
make locator at upper arm position and push back a little further than the duplicate follow joints 
aim constrain upper arm roll to locator
parent locator to follow joint
create rotate plane solver ik handle for follow joints and snap and parent the handle to the lower arm joint

Possible functions:
place in between two points and orient to first joint and freeze
place at joint and freeze
make ik handle and put it somewhere
'''
