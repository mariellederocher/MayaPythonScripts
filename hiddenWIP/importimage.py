'''
Created on Nov 14, 2022

@author: Ellie
'''

#pymel.core.system.importFile 
#https://help.autodesk.com/cloudhelp/2018/JPN/Maya-Tech-Docs/PyMel/generated/functions/pymel.core.system/pymel.core.system.importFile.html?highlight=import#pymel.core.system.importFile
#pymel.core.nodetypes.ImagePlane
#https://help.autodesk.com/cloudhelp/2018/JPN/Maya-Tech-Docs/PyMel/generated/classes/pymel.core.nodetypes/pymel.core.nodetypes.ImagePlane.html?highlight=image%20plane

#find images (file browser prompt?)
#import images to list
#create image planes
#assign images to planes
#group planes
#need input: images, group name

import pymel.core as pmc
import pymel.core.system as sys
import pymel.core.nodetypes as nt

IMGS = []
DIRECTORY = "C:/Users/Ellie/OneDrive/Creative Projects/3D Models and Rigs/armature"

def import_image_main(grpname):
    imgnodes = getimg(IMGS, DIRECTORY)
    planes = []
    for i in imgnodes:
        planes.append(makeplane(i))
    pmc.group(planes, n = grpname)

def getimg(imgs, path):
    imgnode = []
    for i in imgs:
        img = sys.importFile(path + "/" + i, returnNewNodes = True)
        imgnode.append(img)
    return imgnode

def makeplane(img):
    ip = nt.ImagePlane(img)
    return ip
    