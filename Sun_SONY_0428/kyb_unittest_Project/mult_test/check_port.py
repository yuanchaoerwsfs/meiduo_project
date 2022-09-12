import socket, os


def check_port(host, port):
    '''检测端口是否被占用'''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.shutdown(2)
    except OSError as msg:
        print('port %s is available!' % port)
        print(msg)
        return True
    else:
        print('port %s already be in use !' % port)
        return False


def release_port(port):
    '''释放指定的端口'''
    # 查找对应端口的PID
    cmd_find = 'netstat -aon | findstr %s' % port
    print(cmd_find)

    # 返回命令的执行结果
    relsult = os.popen(cmd_find).read()
    print(relsult)

    if str(port) and 'LISTENING' in relsult:
        # 获取端口对应的PID进程
        i = relsult.index('LISTENING')
        start = i + len('LISTENING') + 7
        end = relsult.index('\n')
        pid = relsult[start:end]

        # 关闭被占用端口的PID
        cmd_kill = 'taskkill -f -pid %s' % pid
        print(cmd_kill)
        os.popen(cmd_kill)
    else:
        print('port %s is available! ' % port)


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 4723
    # check_port(host, port)
    release_port(port)
