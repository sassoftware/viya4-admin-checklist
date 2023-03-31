#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# build_all.py
# February 2022
#
# build_all.py finds template files, derives what output file each
# should create from the template filename, and calls
# build_from_template.py for each of them
#
# Usage:
#   You can either run this script directly, like this:
#      build_all.py
#   Or, you can import it into another python script and call its
#   main function, like this:
#      from build_all import build_all
#      build_all()
#
# Change History
#
# 04FEB2022 Creation
#
#
# Copyright © 2022-2023, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

from build_from_template import build_from_template
import sys

def build_all():
    build_from_template('templates/checklist_template.md','checklist.md')
    build_from_template('templates/status_template.md','status.md')
    build_from_template('templates/tasks_by_topic_template.md','tasks_by_topic.md')

if __name__ == '__main__':
    # build_all.py executed directly
    build_all()
    print("build_all.py done")
    sys.exit()