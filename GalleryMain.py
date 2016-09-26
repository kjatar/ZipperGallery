import sys
import os
import zipfile
import rarfile
from PIL import Image

#Call in a directory to create thumbnails of all zip/rar galleries in a directory.

def rarProcess ( rarName ):
    "Process rar archive for thumbnail"

    returnVal = 0

    rarfile.UNRAR_TOOL = '/usr/local/bin/unrar'
    rarfile.PATH_SEP = '/'

    currentRar = rarfile.RarFile(rarName, 'r')

    nameList = (currentRar.namelist())
    nameListPruned = []
    #print nameList
    for name in nameList:
        if ((name.lower()).endswith(('.gif', '.jpg', '.jpeg', '.png', '.bmp'))):
            if((name[0]!='_') and (name[0]!='.')):
                nameListPruned.append(name)


    #print nameListPruned
    nameListPruned.sort()
    firstItemName = nameListPruned[0]
    #print firstItemName
    currentRar.extract(firstItemName)  #Extraction directory can be changed.  Can the extraction name?

    size = 128, 128

    thumbName = rarName+".thumbnail"
    print thumbName
    try:
        img = Image.open(firstItemName)
        img.thumbnail(size)
        img.save(thumbName, "JPEG")
    except IOError:
            print "Error creating thumbnail for", firstItemName
            returnVal = -1

    os.remove(firstItemName)

    return returnVal

def zipProcess( zipName ):
    "Process zip archive for thumbnail"

    returnVal = 0

    currentZip = zipfile.ZipFile(zipName, 'r')

    nameList = (currentZip.namelist())
    nameListPruned = []
    for name in nameList:
        if ((name.lower()).endswith(('.gif', '.jpg', '.jpeg', '.png', '.bmp'))):
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
            returnVal = -1

    os.remove(firstItemName)

    return returnVal




CALL_DIR = u"./TestGallery"

files = os.listdir(CALL_DIR)

files.sort()

for item in files:
    print item
    if os.path.isfile(os.path.join(CALL_DIR, item)):
        if zipfile.is_zipfile(os.path.join(CALL_DIR, item)):
            print "Zip found, calling thumbnail operation on ", item
            if zipProcess(os.path.join(CALL_DIR, item)) == 0:
                print "Thumbnail processed."
            else:
                print "Error creating thumbnail for: ", item
        elif rarfile.is_rarfile(os.path.join(CALL_DIR, item)):
            print "Rar found, calling thumbnail operation on ", item
            if rarProcess(os.path.join(CALL_DIR, item)) == 0:
                print "Thumbnail processed."
            else:
                print "Error creating thumbnail for: ", item
        elif item.endswith(".thumbnail"):
            print "Thumbnail found, printing for troubleshooting: ", item
        else:
            print "Other filetype found: ", item
