import os
import random

# 文件夹路径
dataset_path = './Dataset'
dataset_plus_path = './Dataset_plus'
output_path = './DatasetProMax'

# 如果输出文件夹不存在，则创建
if not os.path.exists(output_path):
    os.makedirs(output_path)

# 读取Dataset和Dataset_plus中的数据
dataset_files = sorted(os.listdir(dataset_path))
dataset_plus_files = sorted(os.listdir(dataset_plus_path))

# 存储每个文件的内容
dataset_data = []
dataset_plus_data = []

# 读取Dataset中的txt文件
for filename in dataset_files:
    if filename.endswith('.txt'):
        with open(os.path.join(dataset_path, filename), 'r', encoding='utf-8') as file:
            content = file.read()
            # 提取数据部分 (数据：到 结果：前的内容)
            data_section = content.split('数据：')[1].split('结果：')[0].strip()
            dataset_data.append(data_section)

# 读取Dataset_plus中的txt文件
for filename in dataset_plus_files:
    if filename.endswith('.txt'):
        with open(os.path.join(dataset_plus_path, filename), 'r', encoding='utf-8') as file:
            content = file.read()
            # 提取数据部分 (数据：到 结果：前的内容)
            data_section = content.split('数据：')[1].split('结果：')[0].strip()
            dataset_plus_data.append(data_section)

# 合并数据：将Dataset和Dataset_plus中的数据拼接到一起
combined_data = []
for i in range(len(dataset_data)):
    # 拼接对应的Dataset和Dataset_plus数据
    dataset_data_content = dataset_data[i]
    dataset_plus_data_content = dataset_plus_data[i]
    
    # 拼接后的文本
    combined_data_content = f"{dataset_data_content} {dataset_plus_data_content}"
    
    combined_data.append(combined_data_content)

# Shuffle数据
random.shuffle(combined_data)

# 生成拼接后的txt文件
for i, data_content in enumerate(combined_data, start=1):
    # 从Dataset获取原始任务和结果部分
    with open(os.path.join(dataset_path, f'{i}.txt'), 'r', encoding='utf-8') as file:
        content = file.read()
        task_section = content.split('任务：')[1].split('数据：')[0].strip()  # 获取任务部分
        result_section = content.split('结果：')[1].strip()  # 获取结果部分
        
    # 输出拼接后的txt文件
    output_filename = f'{i}.txt'
    with open(os.path.join(output_path, output_filename), 'w', encoding='utf-8') as file:
        file.write(f'输入：\n任务：{task_section}\n数据：{data_content}\n结果：\n{result_section}\n')

print(f"已成功生成 {output_path} 文件夹，包含 {len(combined_data)} 个文件。")
