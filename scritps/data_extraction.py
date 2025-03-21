import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')
PROMPT = "你需要从给出的文本中提取关于这个公司市场情况和研究员对公司的介绍的信息，并过滤掉风险提示，分析师介绍，声明，与公司有关的内容包括分析师对公司的分析需要保留并不做太大删减，保留所写出的表格数据，例如市盈率，财务信息"
PROMPT += "返回的文本需要有严格的逻辑结构，学习输入文本的结构。"

base_dir = "/home/gao/LLM/result"
merged_dir = os.path.join(base_dir, "merged")
extracted_dir = os.path.join(base_dir, "extracted")

def merge_md_files(input_dir, output_file):
    with open(output_file, 'w+') as outfile:
        for root, dirs, files in os.walk(input_dir):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as infile:
                        outfile.write(infile.read())
                        outfile.write("\n\n")  # 添加换行符分隔不同文件的内容

def merge_all_md_files():
    company_names = []
    
    if not os.path.exists(merged_dir):
        os.makedirs(merged_dir, exist_ok=True)  # 创建 /merged 目录

    for subdir in os.listdir(base_dir):
        subdir_path = os.path.join(base_dir, subdir)
        if os.path.isdir(subdir_path):
            company_names.append(subdir)
            output_file = os.path.join(merged_dir, f"{subdir}_merged.md")
            merge_md_files(subdir_path, output_file)
            print(f"Merged files in {subdir_path} into {output_file}")
    return company_names

def LLM_extraction(company_names):
    # 初始化OpenAI客户端
    client = OpenAI(
        api_key=os.getenv("API_KEY"),
        base_url="https://ark.cn-beijing.volces.com/api/v3",
    )   
    for company_name in company_names:
        print(f"Extracting information from {company_name}")
        
        if not os.path.exists(extracted_dir):
            os.makedirs(merged_dir, exist_ok=True)  # 创建 /merged 目录
        input_file = f"{merged_dir}/{company_name}_merged.md"
        output_file = f"{extracted_dir}/{company_name}_extracted.md"
        with open(input_file, 'r') as infile:
            input_text = infile.read()
        # 测试API调用
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": PROMPT},
                {"role": "user", "content": input_text}
            ],
            model=os.getenv("MODEL_ID")
        )
        with open(output_file, 'w') as outfile:
            outfile.write(chat_completion.choices[0].message.content)
        print(f"Extracted information from {input_file} into {output_file}")

if __name__ == "__main__":
    company_names = merge_all_md_files()
    LLM_extraction(company_names)
    print("All done!")