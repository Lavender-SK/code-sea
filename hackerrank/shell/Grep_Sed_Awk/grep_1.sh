#!/bin/bash
source ~/.bash_profile
cd `dirname $0`

#%%============================================================================
# Display only those lines of the input file that contain the word 'the'.
#==============================================================================
grep -w 'the'

