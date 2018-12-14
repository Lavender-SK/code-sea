#!/bin/bash
source ~/.bash_profile
cd `dirname $0`

#%%============================================================================
# Display an element of an array
#==============================================================================
countries_list=(`cat`)
echo ${countries_list[3]}



