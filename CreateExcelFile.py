import os
import pandas as pd

# 指定Dataset和Dataset_plus文件夹路径
dataset_path = './Dataset'
dataset_plus_path = './Dataset_plus'

# 初始化列名
columns = [
    'Dataset', 'DatasetAnswer', 'DatasetPlus', 'DatasetPlusAnswer',
    'GPTAnswerforDataset', 'GPTAnswerDatasetScore', 'GPTAnswerforDatasetPlus', 'GPTAnswerDatasetPlusScore',
    'KimiAnswerforDataset', 'KimiAnswerDatasetScore', 'KimiAnswerforDatasetPlus', 'KimiAnswerDatasetPlusScore',
    'QwenAnswerforDataset', 'QwenAnswerDatasetScore', 'QwenAnswerforDatasetPlus', 'QwenAnswerDatasetPlusScore'
]

# 创建一个DataFrame
data = pd.DataFrame(columns=columns)

# 读取Dataset文件夹中的txt文件
for filename in sorted(os.listdir(dataset_path)):
    if filename.endswith('.txt'):
        with open(os.path.join(dataset_path, filename), 'r', encoding='utf-8') as file:
            content = file.read()
            # 分割输入和结果
            input_text = content.split('输入：')[1].split('结果：')[0].strip()
            result_text = content.split('结果：')[1].strip()
            # 添加到DataFrame
            data = pd.concat([data, pd.DataFrame([[input_text, result_text, None, None] + [None] * 12], columns=columns)], ignore_index=True)

# 读取Dataset_plus文件夹中的txt文件
for idx, filename in enumerate(sorted(os.listdir(dataset_plus_path))):
    if filename.endswith('.txt'):
        with open(os.path.join(dataset_plus_path, filename), 'r', encoding='utf-8') as file:
            content = file.read()
            # 分割输入和结果
            input_text = content.split('输入：')[1].split('结果：')[0].strip()
            result_text = content.split('结果：')[1].strip()
            # 更新DataFrame的DatasetPlus和DatasetPlusAnswer列
            data.loc[idx, 'DatasetPlus'] = input_text
            data.loc[idx, 'DatasetPlusAnswer'] = result_text

# 保存为Excel文件
output_file = 'DatasetExcel.xlsx'
data.to_excel(output_file, index=False)

print(f'数据已成功整理并保存到 {output_file}')
