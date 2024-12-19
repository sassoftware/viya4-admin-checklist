#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# build_from_template.py
# February 2022
#
# build_from_template.py reads in a file passed as the first parameter
# (e.g. templates/checklist_template.md), strips out custom comments,
# and replaces Table of Contents (TOC) placeholders with sorted and
# filtered tables of tasks in Markdown syntax. It then writes out a
# file to a path passed as the second parameter.
#
# Usage:
#   You can either run this script directly, like this:
#      build_from_template.py -t templates/checklist_template.md -o checklist.md
#   Or, you can import it into another python script and call its
#   main function, like this:
#      from build_from_template import build_from_template
#      build_from_template('templates/checklist_template.md','checklist.md')
#
# Change History
#
# 02FEB2022 Creation
# 04FEB2022 Generalize to build any template .md file, also
#           build_from_template.py can now be called as a script or
#           build_from_template() can be run as a function from
#           another Python script.
# 23MAR2023 Added support for optional Frequency, Topic and Essential columns
#
#
# Copyright © 2022-2023, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

# Import Python modules
import argparse
import sys
import contextlib
import os
import datetime
from checklistsharedfunctions import toc, rtfreq
from distutils import util

debug=True

# Define exception handler so that we only output trace info from errors when in debug mode
def exception_handler(exception_type, exception, traceback, debug_hook=sys.excepthook):
    if debug:
        debug_hook(exception_type, exception, traceback)
    else:
        print (exception_type.__name__, exception)

sys.excepthook = exception_handler

def build_from_template(strTemplateFilePathIn,strFilePathOut):
    print("Building "+strFilePathOut+" from "+strTemplateFilePathIn)

    # Find top level directory of this project, based on an ASSUMPTION
    # that this script (whose actual pathname stored in a special variable
    # called __FILE__) is in a directory directly below the top level
    # directory, e.g. /scripts. Put another way, find the parent directory
    # of the directory where this script is. This is independent of the
    # current working directory, which can be found by calling (os.getcwd())
    # strProjectRootPath="/mnt/c/WorkshopGit/checklist/admin-checklist"
    strProjectRootPath, strScriptSubdirectory = os.path.split(os.path.dirname(os.path.realpath(__file__)))
    # print('strProjectRootPath: '+strProjectRootPath)

    # Tasks subdirectory relative to strProjectRootPath. You shouldn't need to modify this.
    strTaskSubdirectory="tasks"

    @contextlib.contextmanager
    def pushd(strNewDir):
        strOldDir = os.getcwd()
        os.chdir(strNewDir)
        try:
            yield
        finally:
            os.chdir(strOldDir)

    # cd to the file root (from wherever we currently are) so that relative file paths work = like pushd in bash
    with pushd(strProjectRootPath):
        # Code must remain indented to still be in the file root (in this with-statement context)
        # When we reach code that is outdented to the same level as the with statement above,
        # we effectively popd.

        # print(os.getcwd()) # strProjectRootPath

        # Delete existing output file
        if os.path.exists(strFilePathOut):
            os.remove(strFilePathOut)

        # Open file reference to the Checklist Template file
        with open(strTemplateFilePathIn) as fileIn:
            with open(strFilePathOut, 'w') as fileOut:
                # Read fileIn line by line
                for line in fileIn:
                    if line.startswith('@_TOC_'):
                        # Table of contents

                        # Default sort and filter
                        strTagFilter="Initial"
                        intSortColumn=0 # 0:SortString, 1:Title, 2:Description, 3:Tags, 4: relative path to task file from fileOut
                        boolReverse=False
                        boolShowTags=False
                        boolShowFreq=False
                        boolShowTopic=False
                        boolShowEssential=False
                        strTopicFilter=""

                        # Parameters passed after the '@_TOC_' can override the default sort and filter
                        strTOCParameters=line[len('@_TOC_ '):].rstrip()
                        lstTOCParameters=strTOCParameters.split(',')
                        # print('Found a TOC placeholder with '+str(len(lstTOCParameters))+' parameters: '+strTOCParameters)
                        for strTOCParameter in lstTOCParameters:
                            lstTOCParameterNameAndValue=strTOCParameter.split('=')
                            strParameterName=lstTOCParameterNameAndValue[0]
                            anyParameterValue=lstTOCParameterNameAndValue[1]
                            # print('Parameter name: '+strParameterName+', Value: '+anyParameterValue)
                            # Validate parameter name and value, set sort and filter if valid
                            if strParameterName == 'strTagFilter':
                                strTagFilter=anyParameterValue # May be several tags separated by semicolons
                                # print('strTagFilter: '+strTagFilter)
                            elif strParameterName == 'intSortColumn' and anyParameterValue.isnumeric():
                                intSortColumn=int(anyParameterValue)
                            elif strParameterName == 'boolReverse' and (anyParameterValue=='True' or anyParameterValue=='False'):
                                boolReverse=bool(util.strtobool(anyParameterValue))
                            elif strParameterName == 'boolShowTags' and (anyParameterValue=='True' or anyParameterValue=='False'):
                                boolShowTags=bool(util.strtobool(anyParameterValue))
                            elif strParameterName == 'boolShowFreq' and (anyParameterValue=='True' or anyParameterValue=='False'):
                                boolShowFreq=bool(util.strtobool(anyParameterValue))
                            elif strParameterName == 'boolShowTopic' and (anyParameterValue=='True' or anyParameterValue=='False'):
                                boolShowTopic=bool(util.strtobool(anyParameterValue))
                            elif strParameterName == 'boolShowEssential' and (anyParameterValue=='True' or anyParameterValue=='False'):
                                boolShowEssential=bool(util.strtobool(anyParameterValue))
                            elif strParameterName == 'strTopicFilter':
                                strTopicFilter=anyParameterValue # May be several tags separated by semicolons
                                # print('strTopicFilter: '+strTopicFilter)

                        # Call the toc function defined in checklistsharedfunctions to actually generate a TOC from the tasks files
                        # print('strTagFilter:'+strTagFilter+', intSortColumn:'+str(intSortColumn)+', boolReverse:'+str(boolReverse)+' and type of boolReverse is '+str(type(boolReverse)))
                        toc(fileOut, strProjectRootPath, strTaskSubdirectory, strTagFilter, intSortColumn, boolReverse, boolShowTags,boolShowFreq, boolShowTopic, boolShowEssential,strTopicFilter)
                    elif line.startswith('@_RTFREQ_'):
                        # Regular task frequency table

                        # Default sort and filter
                        strTagFilter="Regular"
                        intSortColumn=0 # 0:SortString, 1:Title
                        boolReverse=False
                        boolShowEssential=False
                        strTopicFilter=""

                        # Parameters passed after the '@_RTFREQ_' can override the default sort and filter
                        strRTFREQParameters=line[len('@_RTFREQ_ '):].rstrip()
                        lstRTFREQParameters=strRTFREQParameters.split(',')
                        # print('Found a RTFREQ placeholder with '+str(len(lstRTFREQParameters))+' parameters: '+strRTFREQParameters)
                        for strRTFREQParameter in lstRTFREQParameters:
                            lstRTFREQParameterNameAndValue=strRTFREQParameter.split('=')
                            strParameterName=lstRTFREQParameterNameAndValue[0]
                            anyParameterValue=lstRTFREQParameterNameAndValue[1]
                            # print('Parameter name: '+strParameterName+', Value: '+anyParameterValue)
                            # Validate parameter name and value, set sort and filter if valid
                            if strParameterName == 'strTagFilter':
                                strTagFilter=anyParameterValue # May be several tags separated by semicolons
                                # print('strTagFilter: '+strTagFilter)
                            elif strParameterName == 'intSortColumn' and anyParameterValue.isnumeric():
                                intSortColumn=int(anyParameterValue)
                            elif strParameterName == 'boolReverse' and (anyParameterValue=='True' or anyParameterValue=='False'):
                                boolReverse=bool(util.strtobool(anyParameterValue))
                            elif strParameterName == 'boolShowEssential' and (anyParameterValue=='True' or anyParameterValue=='False'):
                                boolShowEssential=bool(util.strtobool(anyParameterValue))
                            elif strParameterName == 'strTopicFilter':
                                strTopicFilter=anyParameterValue # May be several tags separated by semicolons
                                # print('strTopicFilter: '+strTopicFilter)

                        # Call the rtfreq function defined in checklistsharedfunctions to actually generate a Regular Task frequency table from the tasks files
                        # print('strTagFilter:'+strTagFilter+', intSortColumn:'+str(intSortColumn)+', boolReverse:'+str(boolReverse)+' and type of boolReverse is '+str(type(boolReverse)))
                        rtfreq(fileOut,strProjectRootPath,strTaskSubdirectory,strTagFilter,intSortColumn,boolReverse,boolShowEssential,strTopicFilter)
                    elif line.startswith('@_#_'):
                        # This is a comment in the template - do nothing
                        pass
                    else:
                        # Normal template line - write it to fileOut
                        fileOut.write(line)

                # Write modified datetime and close
                fileOut.write('</br>Generated by '+os.path.basename(__file__)+' on: %s.</br>\n' % datetime.datetime.now().strftime('%d %b %Y %H:%M:%S'))
                fileOut.close()
            fileIn.close()

    ## Outdent = return to original directory (strOldDir) = like popd in bash
    # print(os.getcwd()) # "wherever you started"

if __name__ == '__main__':
    # build_from_template.py executed directly
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--template", help="Path to template file, relative to project root e.g. templates/checklist_template.md.",required='True')
    parser.add_argument("-o","--output", help="Path to output file, relative to project root, e.g. checklist.md.",required='True')
    parser.add_argument("-d","--debug", action='store_true', help="Debug")
    args = parser.parse_args()
    # Path to template file and output file relative to strProjectRootPath.
    # strTemplateFilePathIn="templates/checklist_template.md"
    strTemplateFilePathIn=args.template
    # strFilePathOut="checklist.md"
    strFilePathOut=args.output
    debug=args.debug

    build_from_template(strTemplateFilePathIn,strFilePathOut)
    print("build_from_template.py done")
    sys.exit()