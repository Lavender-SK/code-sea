#! /bin/bash

###########################################################
# cut #1
# For each line of input, print 3th character on a new line
###########################################################
#cut -c3 /dev/stdin


###########################################################
# cut #2
# Display the 2nd and 7th character from each line of text. 
###########################################################
#cut -c 2,7 /dev/stdin

###########################################################
# cut #3
# Display a range of characters starting at the 2nd position 
# of a string and ending at the 7th position 
# (both positions included).
###########################################################
#cut -c 2-7 /dev/stdin

###########################################################
# cut #4
# Display the first four characters from each line of text. 
###########################################################
#cut -c 1-4 /dev/stdin

###########################################################
# cut #5
# Given a tab delimited file with several columns 
# (tsv format) print the first three fields.
###########################################################
#cut -f 1-3 /dev/stdin

###########################################################
# cut #6
# Print the characters from thirteenth position to the end.
###########################################################
#cut -c 13- /dev/stdin

###########################################################
# cut #7
# Given a sentence, identify and display its fourth word. 
# Assume that the space (' ') is the only delimiter between words.
###########################################################
#cut -d ' ' -f 4 /dev/stdin

###########################################################
# cut #8
# Given a sentence, identify and display its first three words. 
# Assume that the space (' ') is the only delimiter between words. 
###########################################################
#cut -d ' ' -f 1-3 /dev/stdin

###########################################################
# cut #9
# Given a tab delimited file with several columns (tsv format) 
# print the fields from second fields to last field.
###########################################################
cut  -f 2- /dev/stdin
