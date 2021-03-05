import time
import socket
import random


IP_ADDR = '222.140.20.165'
PORT = 54205
smsg = 'led 12t 0 40 16 '
smsg2 = 'led 12t 0 40 32 '
smsg3 = 'led 12t 0 64 46 '
factory = '长葛市威美达卫生洁具厂'
pollution = 'tsp'

def send_socket_led(ipaddr, port, msg):
    """
    建立tcp连接
    """
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    tcp_socket.connect((ipaddr, port))
    tcp_socket.send('LED_Client\n'.encode('gb2312'))
    tcp_socket.send(msg.encode('gb2312'))
    # tcp_socket.send('Heartbeat'.encode('gb2312'))
    time.sleep(3)
    # tcp_socket.send('led clearall'.encode('gb2312'))
    tcp_socket.close()

def random_data(port):
    # 废气
    pdata1 = smsg + str(round((random.uniform(1, 100)), 2))
    print(pdata1)
    send_socket_led(IP_ADDR, port, pdata1)

    # 流速
    pdata2 = smsg2 + str(round((random.uniform(2, 1000)), 2))
    print(pdata2)
    send_socket_led(IP_ADDR, port, pdata2)

    # 烟尘
    pdata3 = smsg3 + str(round((random.uniform(0, 2)), 2))
    print(pdata3)
    send_socket_led(IP_ADDR, port, pdata3)


if __name__ == "__main__":
    factory_port = [54201, 54205]
    for port in factory_port:
        random_data(port)