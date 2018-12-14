#!/bin/bash
source ~/.bash_profile
cd `dirname $0`

#%%============================================================================
# Remove the First Capital Letter from Each Element
#==============================================================================
countries_list=(`cat`)
echo ${countries_list[@]/[A-Z]/.}




