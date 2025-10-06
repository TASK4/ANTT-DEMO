import pandas as pd
import matplotlib.pyplot as plt

# Tải log vào DataFrame
log_data = pd.read_csv('generated_logs.log', sep=' - ',
                       names=['timestamp', 'logger', 'level', 'message'])

# Đếm số lượng theo cấp độ log
log_summary = log_data['level'].value_counts()

print("Log Level Summary:")
print(log_summary)

# Lọc log có cấp độ ERROR
error_logs = log_data[log_data['level'] == 'ERROR']

print("\nError Logs:")
print(error_logs)

# Vẽ biểu đồ phân bố cấp độ log
log_summary.plot(kind='bar')
plt.title('Log Level Distribution')
plt.xlabel('Log Levels')
plt.ylabel('Frequency')
plt.show()