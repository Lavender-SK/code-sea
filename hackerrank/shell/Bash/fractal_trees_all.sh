#!/bin/bash
source ~/.bash_profile
cd `dirname $0`

#%%============================================================================
# 堆栈
#==============================================================================
declare -A stack
declare pointer=0

pop() {
    pointer=$((${pointer}-1))

    value_a=${stack[${pointer},0]}
    value_b=${stack[${pointer},1]}
    value_c=${stack[${pointer},2]}
    value_d=${stack[${pointer},3]}
}

push() {
    stack[${pointer},0]=$1
    stack[${pointer},1]=$2
    stack[${pointer},2]=$3
    stack[${pointer},3]=$4

    pointer=$((${pointer}+1))
}


#%%============================================================================
# 递归函数
# 参数
# tree_deep : 树的深度
# draw_pos  : 树根的位置
#
# 返回
# children_tree_deep
# left_tree_draw_pos
# right_tree_draw_pos
#==============================================================================
draw_tree() {
    # echo "pointer=${pointer}"
    # 接收参数
    present_tree=$1
    draw_pos_x=$2
    draw_pos_y=$3
    
    # 判断停止
    if [ ${present_tree} -gt ${tree_deep} ]; then
        return 0 
    fi

    # 计算画图的行数
    row_num=$((2 ** (5 - ${present_tree}))) 
    echo "row_num:" ${row_num}
    # 画树的枝干
    for ((i=1;i<=row_num;i++)) do
		matrix[${draw_pos_x},${draw_pos_y}]='1'
		draw_pos_x=$((${draw_pos_x}-1))
	done

    # 画树的叶子
	left_pos_y=$((${draw_pos_y}-1))
	right_pos_y=$((${draw_pos_y}+1))

	for ((i=1;i<=row_num;i++)) do
		matrix[${draw_pos_x},${left_pos_y}]='1'
		matrix[${draw_pos_x},${right_pos_y}]='1'

		draw_pos_x=$((${draw_pos_x}-1))
		left_pos_y=$((${left_pos_y}-1))
		right_pos_y=$((${right_pos_y}+1))
	done

	# 画树的孩子树
    present_tree=$((${present_tree}+1))
    left_pos_y=$((${left_pos_y}+1))
    right_pos_y=$((${right_pos_y}-1))

    # echo "push:" ${present_tree} ${draw_pos_x} ${left_pos_y} ${right_pos_y}
    push ${present_tree} ${draw_pos_x} ${left_pos_y} ${right_pos_y}

	draw_tree ${present_tree} ${draw_pos_x} ${left_pos_y}

    pop 
    present_tree=${value_a}
    draw_pos_x=${value_b}
    left_pos_y=${value_c}
    right_pos_y=${value_d}
    
    # echo "pop:" ${present_tree} ${draw_pos_x} ${right_pos_y}

	draw_tree ${present_tree} ${draw_pos_x} ${right_pos_y}
}


#%%============================================================================
# 主流程
#==============================================================================

# 声明变量
declare -A matrix
num_rows=63
num_columns=100

# 初始化 matrix
for ((i=1;i<=num_rows;i++)) do
    for ((j=1;j<=num_columns;j++)) do
        matrix[$i,$j]='_'
    done
done

# 接收输入
read tree_deep

# 改变matrix
draw_pos_x=63
draw_pos_y=50
present_tree=1

# 递归画图
draw_tree ${present_tree} ${draw_pos_x} ${draw_pos_y}

# print the matrix
for ((i=1;i<=num_rows;i++)) do
    for ((j=1;j<=num_columns;j++)) do
        printf ${matrix[$i,$j]}
    done
    printf "\n"
done
