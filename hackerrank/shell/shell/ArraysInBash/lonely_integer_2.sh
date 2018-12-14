#!/bin/bash
source ~/.bash_profile
cd `dirname $0`

#%%============================================================================
# Lonely Integer - Bash!
#==============================================================================
read
arr=($(cat))
arr=${arr[*]}
echo $((${arr// /^}))


# read -> statement at start is just to read the size of array, which we don't need eventually in this code
# arr=($(cat)) -> reads in the array
# arr=${arr[*]} -> render a new variable of type string from the merging of the array arr delimited by space, i.e., from [1,2,2,2,1] to "1 2 2 2 1"
# ${arr// /^} -> replaces all spaces ' ' in the string variable with ^ (bitwise-XOR operator),i.e., we get "1^2^2^2^1"
# $((exp)) -> evaluates the expression "exp" by performing arithmetic operations, here "exp" => ${arr// /^}. Thus ^ is treated as arithmetic operator and the string is evaluated sequentially form left to right.
# We get, 1^2^2^2^1 = 3^2^2^1 = 1^2^1 = 3^1 = 2 (Lonely Integer)



