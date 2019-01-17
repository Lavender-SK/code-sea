#!/bin/bash
source ~/.bash_profile
cd `dirname $0`

#%%============================================================================
# 1434 5678 9101 1234, transform it to 1234 9101 5678 1434.
#==============================================================================
sed -r 's/(.+ )(.+ )(.+ )(....)/\4 \3\2\1/'

