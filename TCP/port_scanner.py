import socket

def port_scanner(target, ports) :
    print(f"Đang quét {target}...")
    for port in ports :
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Cổng {port} đang mở")
            else:
                print(f"Cổng {port} đóng")

target_ip = "127.0.0.1"
ports_to_scan = [22, 80, 43, 8080, 9090]
port_scanner(target_ip, ports_to_scan)