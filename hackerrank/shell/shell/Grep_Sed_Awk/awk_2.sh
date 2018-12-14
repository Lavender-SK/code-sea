#!/bin/bash
source ~/.bash_profile
cd `dirname $0`

#%%============================================================================
# Depending on the scores, display the following for each student:
# [Identifier] : [Pass] 
# or 
# [Identifier] : [Fail]
#==============================================================================

awk '{
    if ( $2 < 50 || $3 < 50 || $4 < 50 )
        print $1, ": Fail"
    else
        print $1, ": Pass"
}'



