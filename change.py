import pandas as pd


# 读取 CSV 文件并排序
def load_and_sort_csv(file_path):
    # 读取CSV文件
    df = pd.read_csv(file_path)
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

    return error_rate, error_count, total_cells


# 比较两个 CSV 文件并计算错误数据占比
def compare_csv(file1, file2):
    # 加载并排序CSV文件
    df1 = load_and_sort_csv(file1)
    df2 = load_and_sort_csv(file2)

    # 检查两个文件的内容是否一致
    if df1.equals(df2):
        print("两个文件内容一致！")
        return

    # 计算错误数据占比
    error_rate, error_count, total_cells = calculate_error_rate(df1, df2)

    print(f"两个文件内容存在差异！")
    print(f"错误数据占比: {error_rate:.4f} ({error_count}/{total_cells})")


# 使用示例
file1 = './student_data.csv'  # 第一个 CSV 文件路径
file2 = './answer.csv'  # 第二个 CSV 文件路径

compare_csv(file1, file2)
