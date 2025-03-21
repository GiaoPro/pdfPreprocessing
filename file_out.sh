#!/bin/bash

IFS=$'\n'


# # 公司文件夹
# OUT_UPPER_PATH="/home/gao/LLM/result"
# for OUT_PATH in $(ls $OUT_UPPER_PATH); do
#     echo "Processing $OUT_PATH"
#     for DIR in $(ls $OUT_UPPER_PATH/$OUT_PATH); do
#         mv $OUT_UPPER_PATH/$OUT_PATH/$DIR/*.md $OUT_UPPER_PATH/$OUT_PATH
#         rm -r $OUT_UPPER_PATH/$OUT_PATH/$DIR
#     done
# done



# 行业文件夹
OUT_UPPER_PATH="/home/gao/LLM/result_hy/result_hangye"
# which mv
# echo "Processing $OUT_UPPER_PATH"
for OUT_PATH in $(ls $OUT_UPPER_PATH); do
    #echo "Processing $OUT_UPPER_PATH/$PATH"
    mv $OUT_UPPER_PATH/$OUT_PATH/*.md $OUT_UPPER_PATH
    rm -r $OUT_UPPER_PATH/$OUT_PATH
done
