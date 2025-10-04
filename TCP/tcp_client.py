import socket

#Tạo socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Kết nối máy chủ từ xa
server_ip = "127.0.0.1"
server_port = 9090

try:
    client_socket.connect((server_ip, server_port))
    print(f"Đã kết nối tới {server_ip} tại cổng {server_port}")
    
    client_socket.send(b"Hello, Server")
    response = client_socket.recv(1024)
    print(f"Phản hồi từ Server: {response.decode()}")
    
except socket.error as e:
    print (f"Lỗi kết nối: {e}")
finally:
    client_socket.close()

    