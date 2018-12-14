#!/bin/bash
source ~/.bash_profile
cd `dirname $0`

###################################################
# 'Uniq' Command #1
# Given a text file, remove the consecutive 
# repetitions of any line.
###################################################
# uniq

###################################################
# 'Uniq' Command #1
# splay the space separated count and line, respectively.
# 
###################################################
# uniq -c | sed "s/^[[:space:]]*//g"

###################################################
# 'Uniq' command #3
###################################################
# uniq -c -i | sed "s/^[[:space:]]*//g"

###################################################
# 'Uniq' command #4
# Given a text file, display only those lines which 
# are not followed or preceded by identical replications. 
###################################################
# uniq -u

###################################################
# uniq --help
###################################################

# 用法：uniq [选项]... [文件]
# Filter adjacent matching lines from INPUT (or standard input),
# writing to OUTPUT (or standard output).
# 
# With no options, matching lines are merged to the first occurrence.
# 
# Mandatory arguments to long options are mandatory for short options too.
#   -c, --count           prefix lines by the number of occurrences
#   -d, --repeated        only print duplicate lines, one for each group
#   -D, --all-repeated[=METHOD]  print all duplicate lines
#                           groups can be delimited with an empty line
#                           METHOD={none(default),prepend,separate}
#   -f, --skip-fields=N   avoid comparing the first N fields
#       --group[=METHOD]  show all items, separating groups with an empty line
#                           METHOD={separate(default),prepend,append,both}
#   -i, --ignore-case     ignore differences in case when comparing
#   -s, --skip-chars=N    avoid comparing the first N characters
#   -u, --unique          only print unique lines
#   -z, --zero-terminated     line delimiter is NUL, not newline
#   -w, --check-chars=N   对每行第N 个字符以后的内容不作对照
#       --help        显示此帮助信息并退出
#       --version     显示版本信息并退出
# 
