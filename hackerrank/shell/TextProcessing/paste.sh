#!/bin/bash
source ~/.bash_profile
cd `dirname $0`

#%%============================================================================
# Paste - 1
# Replace the newlines in the input file with semicolons as demonstrated in the
# sample. 
#==============================================================================
# paste -d ";" -s

#%%============================================================================
# Paste - 2
# Restructure the file so that three consecutive rows are folded into one line 
# and are separated by semicolons. 
#==============================================================================
# paste -d';' - - -


#%%============================================================================
# Paste - 3
# Replace the newlines in the input with tabs as demonstrated in the sample. 
#==============================================================================
# paste -d "\t" -s

#%%============================================================================
# Paste - 4
# Restructure the file in such a way, that every group of three consecutive 
# rows are folded into one, and separated by tab. 
#==============================================================================
# paste -d "\t" - - -

#%%============================================================================
# paste --help 
#==============================================================================
# 用法：paste [选项]... [文件]...
# Write lines consisting of the sequentially corresponding lines from
# each FILE, separated by TABs, to standard output.
# With no FILE, or when FILE is -, read standard input.
# 
# Mandatory arguments to long options are mandatory for short options too.
#   -d, --delimiters=列表 改用指定列表里的字符替代制表分隔符
#   -s, --serial      不使用平行的行目输出模式，而是每个文件占用一行
#       --help        显示此帮助信息并退出
#       --version     显示版本信息并退出
# 
