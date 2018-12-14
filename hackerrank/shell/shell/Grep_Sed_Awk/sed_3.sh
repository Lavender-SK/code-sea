#!/bin/bash
source ~/.bash_profile
cd `dirname $0`

#%%============================================================================
# Given an input file, in each line, highlight all the occurrences of 'thy' by 
# wrapping them up in brace brackets. The search should be case-insensitive.
#==============================================================================
sed -e 's/thy/{&}/gi'



