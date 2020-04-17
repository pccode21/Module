"""
IPv4是32位的，而8位可以表示1个字节，也就是说，IPv4地址可以表示为4字节的数据，刚好可以表示为一个无符号int类型的数据。
那么字符串形式的IP地址如何转换为整数数值呢？
因为点分十进制的IP中，每个被点分隔的数据占用1字节，可以表示的范围是0~255，所以可以认为这是一个256进制的数
比如"1.2.3.4"就是 1*2^8^3+2*2^8^2+3*2^8^1+4*2^8^0
1.将字符串形式的点分十进制IP地址转换为数值，首先使用split将IP地址进行分离，比如"10.1.1.47".split(".")，
这样各个点之间的数据就分离了，得到列表["10","1","1","47"]，随后将列表中的元素从字符串转换为int，并乘以相应的系数后累加
2.将数值IP转换为字符串，这里通过位运算中的“与操作”以及“移位操作”实现。
例如IP地址17.34.51.68对应的数值形式为0x11223344（16进制），那么0x11223344&0xFF000000得到0x11000000，
再向右移动24位就可以得到0x11，即10进制的17。
"""
def ip_str2int(ip):
    tmp = ip.split('.')
    a1 = int(tmp[0])*256*256*256
    a2 = int(tmp[1])*256*256
    a3 = int(tmp[2])*256
    a4 = int(tmp[3])
    ip = a1 + a2 + a3 + a4
    return ip


def ip_int2str(ip):
    a1 = (ip & 0xFF000000) >> 24
    a2 = (ip & 0x00FF0000) >> 16
    a3 = (ip & 0x0000FF00) >> 8
    a4 = ip & 0x000000FF
    ip = '%d.%d.%d.%d' % (a1, a2, a3, a4)
    return ip


if __name__ == '__main__':
    ip = '61.135.169.125'
    int_ip = ip_str2int(ip)
    print(int_ip)
    str_ip = ip_int2str(int_ip)
    print(str_ip)
    # 利用lambda表达式，非常简洁
    ip_to_int = lambda x: sum([256 ** j * int(i) for j, i in enumerate(x.split('.')[::-1])])
    print(ip_to_int(ip))
    int_to_ip = lambda x: '.'.join([str(x / (256**i) % 256) for i in range(3, -1, -1)])
    print(int_to_ip(ip_to_int(ip)))
