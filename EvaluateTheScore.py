import pandas as pd
import io

# 读取CSV文件并排序
def load_and_sort_csv_from_text(csv_text):
    # 使用io.StringIO将CSV文本转换为DataFrame
    df = pd.read_csv(io.StringIO(csv_text))
    # 去除重复行
    df_unique = df.drop_duplicates()
    # 按学号降序排列
    df_sorted = df_unique.sort_values(by='学号', ascending=False)  # 按学号降序排列
    # 重置索引并去掉原来的索引列
    df_sorted = df_sorted.reset_index(drop=True)
    return df_sorted

# 计算错误数据占比
def calculate_error_rate(df1, df2):
    # 比较两个数据框的形状
    if df1.shape != df2.shape:
        raise ValueError("两个数据框的形状不一致，无法比较！")

    # 计算不同的单元格数量
    error_count = (df1 != df2).sum().sum()  # 按列比较，按行再比较，计算所有不相等的单元格数

    # 计算总单元格数量
    total_cells = df1.size  # 数据框的总单元格数

    # 计算错误占比
    error_rate = error_count / total_cells

    # # 计算得分（1 - 错误占比），并保留5位小数
    score = round( error_rate, 5)  # 转换为百分制并保留5位小数
    return score

# 比较并计算得分的函数
def compare_and_score(dataset_answer_csv, gpt_answer_csv, kimi_answer_csv):
    # 将CSV文本转换为DataFrame
    dataset_answer_df = load_and_sort_csv_from_text(dataset_answer_csv)
    gpt_answer_df = load_and_sort_csv_from_text(gpt_answer_csv)
    kimi_answer_df = load_and_sort_csv_from_text(kimi_answer_csv)

    # 计算GPT和Kimi的得分
    gpt_score = calculate_error_rate(dataset_answer_df, gpt_answer_df)
    kimi_score = calculate_error_rate(dataset_answer_df, kimi_answer_df)

    return gpt_score, kimi_score

# 处理Excel文件并生成分数
def process_and_generate_scores(input_file):
    # 读取Excel文件
    df = pd.read_excel(input_file)

    # 比较DatasetAnswer与GPTAnswerforDataset
    df['GPTAnswerDatasetScore'], df['KimiAnswerDatasetScore'] = zip(*df.apply(lambda row: compare_and_score(
        row['DatasetAnswer'], row['GPTAnswerforDataset'], row['KimiAnswerforDataset']), axis=1))

    # 比较DatasetPlusAnswer与GPTAnswerforDatasetPlus
    df['GPTAnswerDatasetPlusScore'], df['KimiAnswerDatasetPlusScore'] = zip(*df.apply(lambda row: compare_and_score(
        row['DatasetPlusAnswer'], row['GPTAnswerforDatasetPlus'], row['KimiAnswerforDatasetPlus']), axis=1))

    # 比较DatasetProMaxAnswer与GPTAnswerforDatasetProMax
    df['GPTAnswerDatasetProMaxScore'], df['KimiAnswerDatasetProMaxScore'] = zip(*df.apply(lambda row: compare_and_score(
        row['DatasetProMaxAnswer'], row['GPTAnswerforDatasetProMax'], row['KimiAnswerforDatasetProMax']), axis=1))

    # 输出结果到新的Excel文件
    df.to_excel('output_scores.xlsx', index=False)

    print("得分已成功生成并保存到 output_scores.xlsx 文件。")

# 运行处理函数
input_file = 'OutputAll.xlsx'  # 请替换为实际的输入Excel文件路径
process_and_generate_scores(input_file)
