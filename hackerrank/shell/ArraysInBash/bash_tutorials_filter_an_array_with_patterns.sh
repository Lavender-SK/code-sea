#!/bin/bash
source ~/.bash_profile
cd `dirname $0`

#%%============================================================================
# Filter an Array with Patterns
#==============================================================================
countries_list=(`cat`)
result_list=( ${countries_list[@]/*[a,A]*/} )
echo ${result_list[@]}
