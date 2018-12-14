#!/bin/bash
source ~/.bash_profile
cd `dirname $0`

#%%============================================================================
# The search should not be sensitive to case. 
# Display only those lines of an input file, which contain the required words.
# the that then those 
#==============================================================================
grep -i -w -e "the" -e "that" -e "then" -e "those"

