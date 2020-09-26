from ping3 import ping
from multiprocessing import Pool

time_delay=[]
name_address={}

def ping_host(ip):
    """
    获取节点的延迟的作用
    :param node:
    :return:
    """
    ip_address = ip
    response = ping(ip_address, unit='ms')

    return response


with open('net_address.txt', 'r') as f:
    for line in f:
        total = 0
        times_avg = 0
        print(line.replace('\n',''))
        for i in range(0, 5):
            try:
                # line.strip()
                delay = ping_host(line.replace('\n',''))
                total = delay + total
                times_avg = times_avg + 1
            except TypeError:
                pass
        try:
            time_delay.append(str(round(total/times_avg, 2)))
            name_address[line.replace('\n','')]=str(round(total/times_avg, 2))
            print(str(round(total/times_avg, 2)))
        except ZeroDivisionError:
            time_delay.append('-1')
            name_address[line.replace('\n','')]='-1'

print(time_delay)
print(name_address)
