import json

# Mở tệp log JSON
with open('json_logs.json', 'r') as log_file:
    logs = json.load(log_file)

# Phân tích và hiển thị log
for log in logs:
    print(f"Timestamp: {log['timestamp']}, Level: {log['level']}, Message: {log['message']}")