#!/bin/bash
source ~/.bash_profile
cd `dirname $0`

#%%============================================================================
# For each line in a given input file, transform the first occurrence 
# of the word 'the' with 'this'. 
#==============================================================================
sed 's/ the / this /1'





