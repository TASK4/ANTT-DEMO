import re

# Mở tệp log đã tạo
with open('generated_logs.log', 'r') as log_file:
    logs = log_file.readlines()

# Biểu thức chính quy để trích xuất thông tin log
log_pattern = re.compile(r'(?P<timestamp>[\d\-\:\,\s]+)\s-\s(?P<logger_name>\w+)\s-\s(?P<level>\w+)\s-\s(?P<message>.+)')

# Phân tích và hiển thị log
for log in logs:
    match = log_pattern.match(log)
    if match:
        log_details = match.groupdict()
        print(f"Timestamp: {log_details['timestamp']}, Level: {log_details['level']}, Message: {log_details['message']}")