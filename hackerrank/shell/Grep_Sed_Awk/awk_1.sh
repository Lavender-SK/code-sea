#!/bin/bash
source ~/.bash_profile
cd `dirname $0`

#%%============================================================================
# For each student, if one or more of the three scores is missing, display:
# Not all scores are available for [Identifier] 
#==============================================================================
awk '{
    if ( $2 == "" || $3 == "" || $4 == ""  )
        print "Not all scores are available for", $1
}
'



