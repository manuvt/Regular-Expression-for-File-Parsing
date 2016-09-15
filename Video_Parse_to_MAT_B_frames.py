# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 12:44:35 2016
Programme to parse the file and extract the values of I, P and SKIP from B and P frames
to store as a MAT file.
@author: manu
"""

import numpy as np
import scipy.io as sio
import re
############# Regular Expressions #############################################
slice_b_or_p        = re.compile('Slice:[B]')
mframe_value        = re.compile('mframe=\s*\d*')
i_p_skip_values     = re.compile('I:\d*[\s]*P:\d*[\s]*SKIP:\d*')
numerical_value     = re.compile('\d*')
b_or_p_frametype    = re.compile('Slice:\w*')
############Opening the file to be parsed######################################
f1 = open('frame_MB.txt','r')
f2 = open('frame_MB.txt','r')
f3 = open('frame_MB.txt','r')
###########Counting the number of lines in the file############################
line_list       =   list(f1)
count1          =   0
len_line_list   =   len(line_list)
###############################################################################
for line1 in f2.readlines():
        if slice_b_or_p.findall(line1):
            count1 = count1+1
###########Initialize the mat file object######################################            
obj_arry = np.zeros((count1,4,), dtype=np.object)
###############################################################################

count =0

###############################################################################
for line in f3.readlines():
        if slice_b_or_p.findall(line):
            
            print("Processing %d th line" %count)
            #store mframe_value in obj_arry[count][1]###########################                      
            line1               =   mframe_value.findall(line)
            str1                =   ''.join(str(e) for e in line1)
            str2                =   numerical_value.findall(str1) 
            obj_arry[count][0]  =   str2 #mframe value
            #store values of I, P and SKIP in line3############################     
            line2   = i_p_skip_values.findall(line)
            str2    = ''.join(str(f) for f in line2)
            line3   = numerical_value.findall(str2)
            
            nonzeroind = np.nonzero(line3)[0]

            i       =   line3[nonzeroind[0]] #value of I
            p       =   line3[nonzeroind[1]] #value of P
            skip    =   line3[nonzeroind[2]] #value of SKIP

            obj_arry[count][1]   =  i
            obj_arry[count][2]   =  p
            obj_arry[count][3]   =  skip
            
            count= count + 1
            
            sio.savemat('video_parse_B_frames.mat', {'obj_arry':obj_arry}) 
###############################################################################
f1.close();
f2.close();
f3.close();		



