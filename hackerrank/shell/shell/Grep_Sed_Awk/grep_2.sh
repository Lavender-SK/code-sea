#!/bin/bash
source ~/.bash_profile
cd `dirname $0`

#%%============================================================================
# Output only those lines that contain the word 'the'. 
# The search should NOT be case sensitive.
#==============================================================================
grep -w -i 'the'

