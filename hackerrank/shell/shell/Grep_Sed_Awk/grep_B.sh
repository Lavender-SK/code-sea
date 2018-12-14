#!/bin/bash
source ~/.bash_profile
cd `dirname $0`

#%%============================================================================
# Display the required lines after filtering with grep, 
# without any changes to their relative ordering in the input file.
#==============================================================================
grep '\([0-9]\) *\1'

