import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_ip = "127.0.0.1"
server_port = 9090
server_socket.bind((server_ip, server_port))
server_socket.listen(5)
print(f"[+] Server listening on {server_ip}:{server_port}")

try:
    while True:
        conn, addr = server_socket.accept()
        print(f"[+] Connected by {addr}")
        try:
            # gửi trước để client biết connect thành công
            conn.send(b"Hello, Client\n")
            data = conn.recv(1024)
            if data:
                print(f"[<] Received from {addr}: {data.decode(errors='ignore')}")
        except Exception as e:
            print("[!] Error handling client:", e)
        finally:
            conn.close()
            print(f"[-] Closed connection {addr}")

except KeyboardInterrupt:
    print("\n[!] Server stopping (KeyboardInterrupt)")

finally:
    server_socket.close()