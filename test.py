import pandas as pd

# 读取CSV数据
df = pd.read_csv('your_data.csv')

# 定义序列长度和步长
sequence_length = 30
step_size = sequence_length // 2

# 存储所有序列的列表
all_sequences = []

# 按code_type分组
grouped = df.groupby('code_type')

# 对每个分组生成序列
for code_type, group in grouped:
    # 按current_time排序
    group_sorted = group.sort_values(by='current_time')
    
    # 生成序列
    for start in range(0, len(group_sorted) - sequence_length + 1, step_size):
        end = start + sequence_length
        sequence = group_sorted['item_id'].iloc[start:end].tolist()
        all_sequences.append((code_type, sequence))

# 打印或处理序列
for i, (code_type, seq) in enumerate(all_sequences):
    print(f"Code Type: {code_type}, Sequence {i+1}: {seq}")