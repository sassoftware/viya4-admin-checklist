#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# checklistsharedfunctions.py
# February 2022 to December 2024
#
# checklistsharedfunctions.py defines Python3 utility functions for the gelviyaadm_checklist project.
#
# Change History
#
# 03FEB2022 Creation
# 20MAR2023 Added support for optional Frequency, Topic and Essential columns
# 20DEC2024 Added rtfreq function to create regular task frequency table
#
# Copyright © 2022-2023, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

from os import listdir
from os.path import isfile, join
strBlockCharacter="◎"

def toc(fileOut,strProjectRootPath,strTaskSubdirectory,strTagFilter,intSortColumn,boolReverse,boolShowTags,boolShowFreq,boolShowTopic,boolShowEssential,strTopicFilter):

    lstTOC = []

    #fileOut.write("Table of contents here, should list "+strTagFilter+" tasks in "+strDirectoryPath+".</br>")
    strDirectoryPath=join(strProjectRootPath, strTaskSubdirectory)
    lstStrFiles = [f for f in listdir(strDirectoryPath) if isfile(join(strDirectoryPath, f))]
    for strTaskFile in lstStrFiles:
        #fileOut.write('Reading file: '+join(strDirectoryPath, strTaskFile)+'</br>\n')
        # Open file the task file for reading
        with open(join(strDirectoryPath, strTaskFile)) as fileTask:
            # Initialize vars
            strSortString="Not found"
            strTaskTitle="Not found"
            strTaskDescription="Not found"
            strTaskTags="Not found"
            strTaskFreq=""
            strTopic="Not Found"
            strEssential="No"
            # Read fileInTask line by line
            for lineInTaskFile in fileTask:
                # Look through the file for a SortString, title, description and tags
                if lineInTaskFile.startswith('SortString: '):
                    # SortString
                    strSortString=lineInTaskFile[len('SortString: '):].rstrip()
                elif lineInTaskFile.startswith('# '):
                    # Title
                    strTaskTitle=lineInTaskFile[2:].rstrip() # Strip off first two characters
                elif lineInTaskFile.startswith('Description: '):
                    # Description
                    strTaskDescription=lineInTaskFile[len('Description: '):].rstrip()
                elif lineInTaskFile.startswith('Tags: '):
                    # Tags
                    strTaskTags=lineInTaskFile[len('Tags: '):].rstrip()
                elif lineInTaskFile.startswith('Frequency: '):
                    # Frequency
                    strTaskFreq=lineInTaskFile[len('Frequency: '):].rstrip()
                elif lineInTaskFile.startswith('Topic: '):
                    # Topic
                    strTopic=lineInTaskFile[len('Topic: '):].rstrip()
                elif lineInTaskFile.startswith('Essential: '):
                    # Essential (if not, task is optional)
                    strEssential=lineInTaskFile[len('Essential: '):].rstrip()
                else:
                    # Ordinary line in task file - do nothing
                    pass

            fileTask.close()

            # Filter to just the tasks which have ALL the filter tags and whose topic matches the topic filter string (if any)
            boolInclude = True # If a table has no filter tags and no topic filter, include all tasks
            boolAtLeastOneFilterTagNotInTaskTags = False # If even one filter tag is not in the task's tags, we won't include this task
            lstTaskTags=strTaskTags.split(',')
            # print('strTaskTags: '+strTaskTags+', lstTaskTags contains '+str(len(lstTaskTags))+' items: ')
            # print(*lstTaskTags, sep=",")
            lstFilterTags=strTagFilter.split(';')
            # print('strTagFilter: '+strTagFilter+', lstFilterTagscontains '+str(len(lstFilterTags))+' items: ')
            # print(*lstFilterTags, sep=",")
            # Loop through the filter tags - if there are any, each of them must be found in the task tags to include that task
            for strFilterTag in lstFilterTags:
                boolThisFilterTagNotInTaskTags = True # Until we find a specific filter tag in the task's tags, we didn't yet find it
                # Loop through the task's tags
                for strTaskTag in lstTaskTags:
                    # ALL filter tags must match to include the task
                    if strFilterTag==strTaskTag:
                        boolThisFilterTagNotInTaskTags = False # We found it! (It is no longer 'Not in task tags')
                if boolThisFilterTagNotInTaskTags:
                    # We did not find this filter tag in any the task tags
                    boolAtLeastOneFilterTagNotInTaskTags = True
            # Now we have looked through the rest of the tags, can we include this task?
            if boolAtLeastOneFilterTagNotInTaskTags:
                boolInclude=False #Exclude this task from the table because we could not find at least one of the filter tags among its task tags

            # We would include this task based on the tag filter. But what about the topic filter?
            if boolInclude:
                boolTopicMatchFound=False
                if strTopicFilter!="":
                    lstTaskTopics=strTopic.split(',')
                    lstTopicFilters=strTopicFilter.split(';')
                    for strThisTopic in lstTaskTopics:
                         # If ANY of the tasks topics matches ANY of the topic filters, include the task
                         for strThisTopicFilter in lstTopicFilters:
                              if strThisTopic==strThisTopicFilter:
                                   boolTopicMatchFound=True
                    # Did any of the task's topics match any of the topic filters?
                    if boolTopicMatchFound==False:
                        boolInclude=False
                # else:
                    # No topic filter
            if boolInclude:
                # fileOut.write('Title: '+strTaskTitle+', Description: '+strTaskDescription+', Tags: '+strTaskTags+', Frequency: '+strTaskFreq+', Topic: '+strTopic+', Essential: '+strEssential+'</br>\n')
                strTaskFileRelativePath = join(strTaskSubdirectory, strTaskFile)
                # Ensure this comment matches similar comment below!
                # lstTOCLine[0] = SortString
                # lstTOCLine[1] = Title
                # lstTOCLine[2] = Description
                # lstTOCLine[3] = Tags
                # lstTOCLine[4] = relative path to task file from fileOut
                # lstTOCLine[5] = Frequency
                lstTOCLine=[strSortString,strTaskTitle,strTaskDescription,strTaskTags,strTaskFileRelativePath,strTaskFreq,strTopic,strEssential]
                lstTOC.append(lstTOCLine)

    # Sort the TOC list by the column indicated by the inintSortColumn parameter passed in
    lstTOCSorted=sorted(lstTOC, key=lambda lstTOCLine: lstTOCLine[intSortColumn], reverse=boolReverse)

    # Prepare a string containing a sort direction arrow in the appropriate direction
    if boolReverse:
        strSortDirection=' ▾' # UTF-8 9662	25BE	 	BLACK DOWN-POINTING SMALL TRIANGLE
    else:
        strSortDirection=' ▴' # UTF-8 9652	25B4	 	BLACK UP-POINTING SMALL TRIANGLE

    # Set column headings and add sort direction arrow to the column we sorted the TOC by
    strCol0Heading = '#'
    if intSortColumn == 0:
        strCol0Heading=strCol0Heading+strSortDirection
    strCol1Heading = 'Title'
    if intSortColumn == 1:
        strCol1Heading=strCol1Heading+strSortDirection
    strCol2Heading = 'Description'
    if intSortColumn == 2:
        strCol2Heading=strCol2Heading+strSortDirection
    strCol3Heading = 'Tags'
    if intSortColumn == 3:
        strCol3Heading=strCol3Heading+strSortDirection
    strCol4Heading = 'Frequency'
    if intSortColumn == 4:
        strCol4Heading=strCol4Heading+strSortDirection
    strCol5Heading = 'Topic'
    if intSortColumn == 5:
        strCol5Heading=strCol5Heading+strSortDirection
    strCol6Heading = 'Essential'
    if intSortColumn == 6:
        strCol6Heading=strCol6Heading+strSortDirection

    # Write a rowcount
    if strTopicFilter!="":
        fileOut.write('> *'+str(len(lstTOCSorted))+' tasks in topic '+strTopicFilter+'*\n\n')
    else:
        fileOut.write('> *'+str(len(lstTOCSorted))+' tasks tagged as '+strTagFilter+'*\n\n')

    # Write a Markdown table header row
    fileOut.write('| '+strCol0Heading+' | '+strCol1Heading+' | '+strCol2Heading+' |')
    if boolShowTags:
            fileOut.write(' '+strCol3Heading+' |')
    if boolShowFreq:
            fileOut.write(' '+strCol4Heading+' |')
    if boolShowTopic:
            fileOut.write(' '+strCol5Heading+' |')
    if boolShowEssential:
            fileOut.write(' '+strCol6Heading+' |')
    fileOut.write('\n')
    fileOut.write('|---|---|---|')
    if boolShowTags:
            fileOut.write('---|')
    if boolShowFreq:
            fileOut.write('---|')
    if boolShowTopic:
            fileOut.write('---|')
    if boolShowEssential:
            fileOut.write('---|')
    fileOut.write('\n')

    # Iterate through lstTOCSorted to write task rows to the Markdown table
    for lstTOCLine in lstTOCSorted:
        # Ensure this comment matches similar comment above!
        # lstTOCLine[0] = SortString
        # lstTOCLine[1] = Title
        # lstTOCLine[2] = Description
        # lstTOCLine[3] = Tags
        # lstTOCLine[4] = relative path to task file from fileOut
        # lstTOCLine[5] = Frequency
        # lstTOCLine[6] = Topic
        # lstTOCLine[7] = Essential
        fileOut.write('| '+lstTOCLine[0]+' | ['+lstTOCLine[1]+']('+lstTOCLine[4]+') | '+lstTOCLine[2]+' |')
        if boolShowTags:
                fileOut.write(' '+lstTOCLine[3]+' |')
        if boolShowFreq:
                fileOut.write(' '+lstTOCLine[5]+' |')
        if boolShowTopic:
                fileOut.write(' '+lstTOCLine[6]+' |')
        if boolShowEssential:
                fileOut.write(' '+lstTOCLine[7]+' |')
        fileOut.write('\n')

    # return "Return string - this does nothing"

def rtfreq(fileOut,strProjectRootPath,strTaskSubdirectory,strTagFilter,intSortColumn,boolReverse,boolShowEssential,strTopicFilter):
    # Only supports sorting by column 0 (sortString) or column 1 (Title).
    # Sorting by other columns would not make sense.

    lstRTFREQ = []

    #fileOut.write("Regular task frequency table here, should list "+strTagFilter+" tasks in "+strDirectoryPath+".</br>")
    strDirectoryPath=join(strProjectRootPath, strTaskSubdirectory)
    lstStrFiles = [f for f in listdir(strDirectoryPath) if isfile(join(strDirectoryPath, f))]
    for strTaskFile in lstStrFiles:
        #fileOut.write('Reading file: '+join(strDirectoryPath, strTaskFile)+'</br>\n')
        # Open file the task file for reading
        with open(join(strDirectoryPath, strTaskFile)) as fileTask:
            # Initialize vars
            strSortString="Not found"
            strTaskTitle="Not found"
            # strTaskDescription="Not found"
            strTaskTags="Not found"
            strTaskFreq=""
            strTopic="Not Found"
            strEssential="No"
            # Read fileInTask line by line
            for lineInTaskFile in fileTask:
                # Look through the file for a SortString, title, description and tags
                if lineInTaskFile.startswith('SortString: '):
                    # SortString
                    strSortString=lineInTaskFile[len('SortString: '):].rstrip()
                elif lineInTaskFile.startswith('# '):
                    # Title
                    strTaskTitle=lineInTaskFile[2:].rstrip() # Strip off first two characters
                # elif lineInTaskFile.startswith('Description: '):
                    ## Description
                    # strTaskDescription=lineInTaskFile[len('Description: '):].rstrip()
                elif lineInTaskFile.startswith('Tags: '):
                    # Tags
                    strTaskTags=lineInTaskFile[len('Tags: '):].rstrip()
                elif lineInTaskFile.startswith('Frequency: '):
                    # Frequency
                    strTaskFreq=lineInTaskFile[len('Frequency: '):].rstrip()
                elif lineInTaskFile.startswith('Topic: '):
                    # Topic
                    strTopic=lineInTaskFile[len('Topic: '):].rstrip()
                elif lineInTaskFile.startswith('Essential: '):
                    # Essential (if not, task is optional)
                    strEssential=lineInTaskFile[len('Essential: '):].rstrip()
                else:
                    # Ordinary line in task file - do nothing
                    pass

            fileTask.close()

            # Filter to just the tasks which have ALL the filter tags and whose topic matches the topic filter string (if any)
            boolInclude = True # If a table has no filter tags and no topic filter, include all tasks
            boolAtLeastOneFilterTagNotInTaskTags = False # If even one filter tag is not in the task's tags, we won't include this task
            lstTaskTags=strTaskTags.split(',')
            # print('strTaskTags: '+strTaskTags+', lstTaskTags contains '+str(len(lstTaskTags))+' items: ')
            # print(*lstTaskTags, sep=",")
            lstFilterTags=strTagFilter.split(';')
            # print('strTagFilter: '+strTagFilter+', lstFilterTagscontains '+str(len(lstFilterTags))+' items: ')
            # print(*lstFilterTags, sep=",")
            # Loop through the filter tags - if there are any, each of them must be found in the task tags to include that task
            for strFilterTag in lstFilterTags:
                boolThisFilterTagNotInTaskTags = True # Until we find a specific filter tag in the task's tags, we didn't yet find it
                # Loop through the task's tags
                for strTaskTag in lstTaskTags:
                    # ALL filter tags must match to include the task
                    if strFilterTag==strTaskTag:
                        boolThisFilterTagNotInTaskTags = False # We found it! (It is no longer 'Not in task tags')
                if boolThisFilterTagNotInTaskTags:
                    # We did not find this filter tag in any the task tags
                    boolAtLeastOneFilterTagNotInTaskTags = True
            # Now we have looked through the rest of the tags, can we include this task?
            if boolAtLeastOneFilterTagNotInTaskTags:
                boolInclude=False #Exclude this task from the table because we could not find at least one of the filter tags among its task tags

            if boolInclude:
                # We would include this task based on the tag filter. But what about the topic filter?
                boolTopicMatchFound=False
                if strTopicFilter!="":
                    lstTaskTopics=strTopic.split(',')
                    lstTopicFilters=strTopicFilter.split(';')
                    for strThisTopic in lstTaskTopics:
                         # If ANY of the tasks topics matches ANY of the topic filters, include the task
                         for strThisTopicFilter in lstTopicFilters:
                              if strThisTopic==strThisTopicFilter:
                                   boolTopicMatchFound=True
                    # Did any of the task's topics match any of the topic filters?
                    if boolTopicMatchFound==False:
                        boolInclude=False
                # else:
                    # No topic filter
            if boolInclude:
                # fileOut.write('Title: '+strTaskTitle+', Description: '+strTaskDescription+', Tags: '+strTaskTags+', Frequency: '+strTaskFreq+', Topic: '+strTopic+', Essential: '+strEssential+'</br>\n')
                strTaskFileRelativePath = join(strTaskSubdirectory, strTaskFile)
                # Ensure this comment matches similar comment below!
                # lstRTFREQLine[0] = SortString
                # lstRTFREQLine[1] = Title
                # lstRTFREQLine[2] = Tags
                # lstRTFREQLine[3] = relative path to task file from fileOut
                # lstRTFREQLine[4] = Frequency
                # lstRTFREQLine[5] = Topic
                # lstRTFREQLine[6] = Essential
                lstRTFREQLine=[strSortString,strTaskTitle,strTaskTags,strTaskFileRelativePath,strTaskFreq,strTopic,strEssential]
                lstRTFREQ.append(lstRTFREQLine)

    # Sort the RTFREQ list by the column indicated by the inintSortColumn parameter passed in
    lstRTFREQSorted=sorted(lstRTFREQ, key=lambda lstRTFREQLine: lstRTFREQLine[intSortColumn], reverse=boolReverse)

    # Prepare a string containing a sort direction arrow in the appropriate direction
    if boolReverse:
        strSortDirection=' ▾' # UTF-8 9662	25BE	 	BLACK DOWN-POINTING SMALL TRIANGLE
    else:
        strSortDirection=' ▴' # UTF-8 9652	25B4	 	BLACK UP-POINTING SMALL TRIANGLE

    # Set column headings and add sort direction arrow to the column we sorted the RTFREQ list by
    strCol0Heading = '#'
    if intSortColumn == 0:
        strCol0Heading=strCol0Heading+strSortDirection
    strCol1Heading = 'Title'
    if intSortColumn == 1:
        strCol1Heading=strCol1Heading+strSortDirection
    strCol2Heading = 'Annually'
    strCol3Heading = 'Quarterly'
    strCol4Heading = 'Monthly'
    strCol5Heading = 'Weekly'
    strCol6Heading = 'Daily'
    strCol7Heading = 'Other'
    strCol8Heading = 'Essential'

    # Write a rowcount
    if strTopicFilter!="":
        fileOut.write('> *'+str(len(lstRTFREQSorted))+' tasks in topic '+strTopicFilter+'*\n\n')
    else:
        fileOut.write('> *'+str(len(lstRTFREQSorted))+' tasks tagged as '+strTagFilter+'*\n\n')

    # Write a Markdown table header row
    fileOut.write('| '+strCol0Heading+' | '+strCol1Heading+' | '+strCol2Heading+' | '+strCol3Heading+' | '+strCol4Heading+' | '+strCol5Heading+' | '+strCol6Heading+' | '+strCol7Heading+' |')
    if boolShowEssential:
        fileOut.write(' '+strCol8Heading+' |')
    fileOut.write('\n')
    fileOut.write('|---|---|:-:|:-:|:-:|:-:|:-:|---|') # --- = Default align, :-: = Center align
    if boolShowEssential:
        fileOut.write('---|')
    fileOut.write('\n')

    # Iterate through lstRTFREQSorted to write task rows to the Markdown table
    for lstRTFREQLine in lstRTFREQSorted:
        # Ensure this comment matches similar comment above!
        # lstRTFREQLine[0] = SortString
        # lstRTFREQLine[1] = Title
        # lstRTFREQLine[2] = Tags
        # lstRTFREQLine[3] = relative path to task file from fileOut
        # lstRTFREQLine[4] = Frequency
        # lstRTFREQLine[5] = Topic
        # lstRTFREQLine[6] = Essential
        strCol2Value = ''
        strCol3Value = ''
        strCol4Value = ''
        strCol5Value = ''
        strCol6Value = ''
        strCol7Value = ''
        if lstRTFREQLine[4]=='Annually':
            strCol2Value = strBlockCharacter
        elif lstRTFREQLine[4]=='Quarterly':
            strCol3Value = strBlockCharacter
        elif lstRTFREQLine[4]=='Monthly':
            strCol4Value = strBlockCharacter
        elif lstRTFREQLine[4]=='Weekly':
            strCol5Value = strBlockCharacter
        elif lstRTFREQLine[4]=='Daily':
            strCol6Value = strBlockCharacter
        else:
          # Other - show the entire task Frequency string, not just an asterisk
          strCol7Value = lstRTFREQLine[4]

        fileOut.write('| '+lstRTFREQLine[0]+' | ['+lstRTFREQLine[1]+']('+lstRTFREQLine[3]+') | '+strCol2Value+' | '+strCol3Value+' | '+strCol4Value+' | '+strCol5Value+' | '+strCol6Value+' | '+strCol7Value+' |')
        if boolShowEssential:
                fileOut.write(' '+lstRTFREQLine[6]+' |')
        fileOut.write('\n')

    # return "Return string - this does nothing"
