#!/bin/bash
source ~/.bash_profile
cd `dirname $0`

#%%============================================================================
# Concatenate an array with itself
#==============================================================================
countries_list=(`cat`)

result_list=( "${countries_list[@]}" "${countries_list[@]}" "${countries_list[@]}" )

echo ${result_list[@]}


