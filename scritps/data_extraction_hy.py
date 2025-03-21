import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')
PROMPT = "你需要从给出的文本中提取关于这个公司市场情况和研究员对公司的介绍的信息，并过滤掉风险提示，分析师介绍，声明，与公司有关的内容包括分析师对公司的分析需要保留并不做太大删减，保留所写出的表格数据，例如市盈率，财务信息"
PROMPT += "返回的文本需要有严格的逻辑结构，学习输入文本的结构。"

base_dir = "/home/gao/LLM/result_hangye"
extracted_dir = os.path.join(base_dir, "extracted")

def LLM_extraction():
    # 初始化OpenAI客户端
    client = OpenAI(
        api_key=os.getenv("API_KEY"),
        base_url="https://ark.cn-beijing.volces.com/api/v3",
    )
    if not os.path.exists(extracted_dir):
        os.makedirs(extracted_dir, exist_ok=True)  # 创建 /merged 目录   
    for file in os.listdir(base_dir):
        input_file = os.path.join(base_dir, file)
        output_file = os.path.join(extracted_dir, file)
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
        print(f"Extracted information from {file} into {output_file}")

if __name__ == "__main__":
    LLM_extraction()
    print("All done!")