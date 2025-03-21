# 研报数据预处理
这个工作主要是将PDF转为MD格式，并对同一公司多份研报进行归纳提取。
其中，我基于MARKER将PDF转MD格式，后通过deepseek大模型提取有效信息。
## 1. 文件功能
**marker_all.sh** 脚本用于将所有文件夹下的pdf文件通过marker工具转为md格式，注意这里的marker用于对一个文件夹下的所有pdf文件进行处理的指令（请查看PDFS_COMPANY的格式），若有单份需求，需要修改。 

**file_out** 脚本用于将marker生成的同一公司的所有研报md文件放在同一级别目录下，因为在实际操作中发现marker之后对于每一个pdf都会创建一个单独的文件夹去存放json文件和md文件，这样处理后方便后续大模型数据读取。

**scritps/data_extraction.py** 用于将数据送给大模型，并生成提取后资料。
## 2. 如何使用
下面是基本使用流程：
1. `./file_out.sh`
2. `./marker_all.sh`
3. `python3 scritps/data_extraction.py`
注意，由于这个是随手写的，并没有做健壮性工作，所以注意路径的正确性以及文件结构的正确性。
