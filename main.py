#!/bin/env python
# -*- coding: utf8 -*-
# this can copy source folder newest "one" file to target folder :D
# made by Mics
# file name: main.py

from os import listdir
from os.path import isdir, isfile, join, getmtime, exists
from shutil import copyfile

SOURCE_FOLDER = "/Users/Mics/test/source"
TARGET_FOLDER = "/Users/Mics/test/target"
DEBUG = True

def debugmsg(string):
    if DEBUG: print string
    
if __name__ == '__main__':
    if not isdir(SOURCE_FOLDER):
        print "資料夾設定錯誤"
        exit()
    if not isdir(TARGET_FOLDER):
        print "資料夾設定錯誤"
        exit()

    files = [ f for f in listdir(SOURCE_FOLDER) \
            if isfile(join(SOURCE_FOLDER,f)) ]
    debugmsg("files: %s" % files)

    newest_f = files.pop()
    debugmsg("first var newest_f is : %s" % newest_f)

    for f in files:
        if getmtime(join(SOURCE_FOLDER, f)) > \
            getmtime(join(SOURCE_FOLDER, newest_f)):
            newest_f=f
            debugmsg("newest_f is changed, name is : %s" % newest_f)
    debugmsg("last newest_f is : %s" % newest_f)
    target_file = join(TARGET_FOLDER,newest_f)
    source_file = join(SOURCE_FOLDER,newest_f)

    if exists(target_file):
        print "target file is exists, copy cancel. (file name: %s)" % \
                target_file
        exit()
    
    copyfile( source_file , target_file)
    print "file copied"

