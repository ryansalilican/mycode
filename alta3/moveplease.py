#!/usr/bin/env python3
import shutil
import os
os.chdir("/home/student/alta3research-python-cert/coding.lessons/")
shutil.move('raynor.obj', 'ceph_storage/')
xname = input('What is the new name for the kerrigan.obj? ')
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

