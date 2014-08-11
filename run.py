#!/bin/env python
# -*- coding: utf8 -*-
# this can copy source folder newest "one" file to target folder :D
# made by Mics

import os.path

SOURCE_FOLDER = "/Users/Mics/test/source"
TARGET_FOLDER = "/Users/Mics/test/target"

if __name__ == '__main__':
    if not os.path.isdir(SOURCE_FOLDER):
        print "資料夾設定錯誤"
        exit()
    if not os.path.isdir(TARGET_FOLDER):
        print "資料夾設定錯誤"
        exit()
