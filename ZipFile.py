import zipfile
from os import walk
import sys
from PIL import Image

# This script will create a thumbnail for one zip archive.  Will do the alphabetical first image in the archive.
# File created will be the script target.thumbnail.

print "Usage: Run with target as zip file of images."
print "Script will pull out and resize thumbnail."

if(len(sys.argv) < 1):
  print "Must provide target file in current directory."
  sys.exit(1)

zipName = sys.argv[1]

if not zipfile.is_zipfile(zipName):
  print "Invalid zip file designated: ", zipName
  sus.exit(1)

#Filename processing should be done at display instead of backend.
#Will make it easier to pull tags off of ex.


currentZip = zipfile.ZipFile(zipName, 'r')

nameList = (currentZip.namelist())
nameListPruned = []
for name in nameList:
    if (name.endswith(('.gif', '.jpg', '.jpeg', '.png', '.bmp'))):
        if((name[0]!='_') and (name[0]!='.')):
            nameListPruned.append(name)


#print nameListPruned
nameListPruned.sort()
firstItemName = nameListPruned[0]
#print firstItemName
currentZip.extract(firstItemName)  #Extraction directory can be changed.  Can the extraction name?

size = 128, 128

thumbName = zipName+".thumbnail"
#print thumbName
try:
    img = Image.open(firstItemName)
    img.thumbnail(size)
    img.save(thumbName, "JPEG")
except IOError:
        print "Error creating thumbnail for", firstItemName
