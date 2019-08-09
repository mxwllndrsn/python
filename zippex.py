#!/usr/bin/env python

import zipfile
import os

cwd = os.getcwd()
unzips = os.path.join(cwd, "unzips")

for zips in os.listdir(cwd):
    try:
        with zipfile.ZipFile(zips, "r") as zipref:
            zipref.extractall(unzips)
    except:
        break

