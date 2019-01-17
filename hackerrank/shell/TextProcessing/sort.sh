#!/bin/bash
source ~/.bash_profile
cd `dirname $0`

###############################################
# Sort Command #1 
# Given a text file, order the lines 
# in lexicographical order.
###############################################
# sort

###############################################
# Sort Command #1
# Given a text file, order the lines in reverse 
# lexicographical order (i.e. Z-A instead of A-Z).
###############################################
# sort -r 

###############################################
# sort Command #3
###############################################
# sort -n

###############################################
# sort Command #4
###############################################
# sort -n -r

###############################################
# sort Command #5
###############################################
# sort -t $'\t' -k2,2 -n -r

###############################################
# sort Command #6
###############################################
# sort -t $'\t' -k2,2 -n

###############################################
# sort Command #7
###############################################
# sort -t '|' -k 2,2 -n -r

###############################################
# sort --help
###############################################
# 用法：sort [选项]... [文件]...
# 　或：sort [选项]... --files0-from=F
# Write sorted concatenation of all FILE(s) to standard output.
# 
# Mandatory arguments to long options are mandatory for short options too.
# 排序选项：
# 
#   -b, --ignore-leading-blanks   忽略前导的空白区域
#   -d, --dictionary-order    只考虑空白区域和字母字符
#   -f, --ignore-case     忽略字母大小写
#   -g, --general-numeric-sort  compare according to general numerical value
#   -i, --ignore-nonprinting    consider only printable characters
#   -M, --month-sort            compare (unknown) < 'JAN' < ... < 'DEC'
#   -h, --human-numeric-sort    使用易读性数字(例如： 2K 1G)
#   -n, --numeric-sort        根据字符串数值比较
#   -R, --random-sort     根据随机hash 排序
#       --random-source=文件  从指定文件中获得随机字节
#   -r, --reverse         逆序输出排序结果
#       --sort=WORD       按照WORD 指定的格式排序：
#                     一般数字-g，高可读性-h，月份-M，数字-n，
#                     随机-R，版本-V
#   -V, --version-sort        在文本内进行自然版本排序
# 
# 其他选项：
# 
#       --batch-size=NMERGE   一次最多合并NMERGE 个输入；如果输入更多
#                     则使用临时文件
#   -c, --check, --check=diagnose-first   检查输入是否已排序，若已有序则不进行操作
#   -C, --check=quiet, --check=silent 类似-c，但不报告第一个无序行
#       --compress-program=程序   使用指定程序压缩临时文件；使用该程序
#                     的-d 参数解压缩文件
#       --debug           为用于排序的行添加注释，并将有可能有问题的
#                     用法输出到标准错误输出
#       --files0-from=文件    从指定文件读取以NUL 终止的名称，如果该文件被
#                     指定为"-"则从标准输入读文件名
#   -k, --key=KEYDEF          sort via a key; KEYDEF gives location and type
#   -m, --merge               merge already sorted files; do not sort
#   -o, --output=文件     将结果写入到文件而非标准输出
#   -s, --stable          禁用last-resort 比较以稳定比较算法
#   -S, --buffer-size=大小    指定主内存缓存大小
#   -t, --field-separator=分隔符  使用指定的分隔符代替非空格到空格的转换
#   -T, --temporary-directory=目录    使用指定目录而非$TMPDIR 或/tmp 作为
#                     临时目录，可用多个选项指定多个目录
#       --parallel=N      将同时运行的排序数改变为N
#   -u, --unique      配合-c，严格校验排序；不配合-c，则只输出一次排序结果
#   -z, --zero-terminated     line delimiter is NUL, not newline
#       --help        显示此帮助信息并退出
#       --version     显示版本信息并退出
