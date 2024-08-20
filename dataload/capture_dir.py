
fnames = ['train_files.txt']
for f in fnames:
    with open(f, 'r') as file:
        lines = file.readlines()
    # 提取每行的第一部分（目录）并存储到一个集合中以避免重复
    directories = set()
    for line in lines:
        directory = line.split()[0]  # 假设目录是每行的第一部分，以'/'分割
        directories.add(directory)

# 将结果写入到新的文本文件中
with open('unique_directories.txt', 'w') as output_file:
    for directory in sorted(directories):  # 排序输出
        output_file.write(directory + '\n')

print("目录列表已写入到 'unique_directories.txt'")