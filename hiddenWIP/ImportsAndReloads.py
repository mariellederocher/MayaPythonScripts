import pymel.core as pm
import maya.cmds as cmds
import importlib as imp

import mayapybook
import hierarchyconvertermaya

import MayaDev.pymelui

import time
try:
	checkTime
except NameError:
	checkTime = time.time()
else:
	#if there's been a change
	hcmpath = os.path.abspath(hierarchyconvertermaya.__file__)
	hcgpath  = os.path.abspath(hierarchyconvertermaya.__file__)
	if checkTime < os.path.getmtime(hcmpath) or checkTime < os.path.getmtime(hcgpath):
		if hierarchyconvertermaya._eventId:
			OpenMaya.MMessage.removeCallback(hierarchyconvertermaya._eventId)
		imp.reload(hierarchyconvertermaya)
		print("updated hierarchyconvertermaya")
	checkTime = time.time()

hierarchyconvertermaya.show()