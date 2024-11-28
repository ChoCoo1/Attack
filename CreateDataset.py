import random
import os

# 随机生成学生数据
def generate_random_student_data(num_students=10):
    # 学号列表，范围是60到70
    student_ids = list(range(60, 70))
    random.shuffle(student_ids)  # 打乱学号

    # 学生姓名列表
    student_names = [f"学生{i}" for i in range(60, 70)]  # 生成学生1到学生10
    random.shuffle(student_names)  # 打乱姓名

    students_data = []
    for i in range(num_students):
        student_id = student_ids[i]  # 从打乱后的学号列表中取学号
        student_name = student_names[i]  # 从打乱后的姓名列表中取学生姓名

        # 随机生成成绩
        grades = {
            "数学成绩": random.randint(60, 70),
            "英语成绩": random.randint(60, 70),
            "语文成绩": random.randint(60, 70)
        }

        student_info = {
            "学生姓名": student_name,
            "学号": student_id,
            **grades
        }

        students_data.append(student_info)

    return students_data


# 保存为txt文件（Dataset版本）
def save_to_txt_dataset(students_data, file_name):
    sentences = []
    for student in students_data:
        sentences.append(f"{student['学生姓名']}的学号是{student['学号']}。")
        sentences.append(f"{student['学生姓名']}的数学成绩是{student['数学成绩']}。")
        sentences.append(f"{student['学生姓名']}的英语成绩是{student['英语成绩']}。")
        sentences.append(f"{student['学生姓名']}的语文成绩是{student['语文成绩']}。")

    # 打乱句子顺序
    random.shuffle(sentences)
    text = "".join(sentences)

    # 写入文件
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("输入：\n")
        f.write("任务：将这些数据整理成表格，注意是csv格式，并且学生姓名都是学生XX，列名顺序为学生姓名,学号,数学成绩,英语成绩,语文成绩\n")
        f.write(f"数据：{text}\n")
        f.write("结果：\n")
        f.write("学生姓名,学号,数学成绩,英语成绩,语文成绩\n")

        # 格式化并保存为CSV风格
        for student in students_data:
            f.write(f"{student['学生姓名']},{student['学号']},{student['数学成绩']},{student['英语成绩']},{student['语文成绩']}\n")


# 保存为txt文件（Dataset改进版版本）
def save_to_txt_improved(students_data, file_name):
    sentences = []
    for student in students_data:
        sentences.append(f"{student['学生姓名']}的学号是{student['学号']}。")
        sentences.append(f"学号{student['学号']}的数学成绩是{student['数学成绩']}。")
        sentences.append(f"学号{student['学号']}的英语成绩是{student['英语成绩']}。")
        sentences.append(f"学号{student['学号']}的语文成绩是{student['语文成绩']}。")

    # 打乱句子顺序
    random.shuffle(sentences)
    text = "".join(sentences)

    # 写入文件
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("输入：\n")
        f.write("任务：将这些数据整理成表格，注意是csv格式，并且学生姓名都是学生XX，列名顺序为学生姓名,学号,数学成绩,英语成绩,语文成绩\n")
        f.write(f"数据：{text}\n")
        f.write("结果：\n")
        f.write("学生姓名,学号,数学成绩,英语成绩,语文成绩\n")

        # 格式化并保存为CSV风格
        for student in students_data:
            f.write(f"{student['学生姓名']},{student['学号']},{student['数学成绩']},{student['英语成绩']},{student['语文成绩']}\n")


# 生成50个txt文件到Dataset和Dataset改进版文件夹
def generate_multiple_txt_files(num_files=50):
    dataset_dir = './Dataset'
    improved_dir = './Dataset_plus'

    # 如果文件夹不存在则创建
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)
    if not os.path.exists(improved_dir):
        os.makedirs(improved_dir)

    for i in range(1, num_files + 1):
        students_data = generate_random_student_data()

        # 保存到Dataset文件夹
        dataset_file_name = f"{dataset_dir}/{i}.txt"
        save_to_txt_dataset(students_data, dataset_file_name)

        # 保存到Dataset改进版文件夹
        improved_file_name = f"{improved_dir}/{i}.txt"
        save_to_txt_improved(students_data, improved_file_name)

        print(f"文件 {dataset_file_name} 和 {improved_file_name} 已生成")


# 生成50个txt文件
generate_multiple_txt_files(50)
