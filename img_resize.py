#!/usr/bin/env python
from PIL import Image
import os
import sys

"""Resizes images to desired height in px, output to new directory [input]-[image height]
    takes 2 arguments - input directory and image height  """

#prevent max image size issues
Image.MAX_IMAGE_PIXELS = None

inDir, maxHeight = sys.argv[1], int(sys.argv[2])

#paths
cwd = os.getcwd()
outDir = inDir + '-' + str(maxHeight)
inDir = os.path.join(cwd, inDir)
files = os.listdir(inDir)
os.mkdir(os.path.join(cwd, outDir))
outDir = os.path.join(cwd, outDir)

print('\nOutput Directory is: ' + outDir +'\n')

i = 1

for file in files:
    imgPath = os.path.join(inDir, file)

    if os.path.isfile(imgPath):
        im = Image.open(imgPath)
    else:
        print(' Not an image, skipping...')
        continue

    #resize
    ratio = (maxHeight/im.size[1])
    width = int((ratio * im.size[0]))
    im = im.resize((width, maxHeight), Image.ANTIALIAS)

    #export
    imgName = (file[:-4] + '-' + str(maxHeight) + file[-4:])
    imgOut = os.path.join(outDir, imgName)
    im.save(imgOut)

    print(' ' + imgName)
    i += 1

print('\n{0} images total'.format(i))
print('resize complete')