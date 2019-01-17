#!/bin/bash
source ~/.bash_profile
cd `dirname $0`

#%%============================================================================
# Count the number of elements in an Array 
#==============================================================================
countries_list=(`cat`)
echo ${#countries_list[@]}




