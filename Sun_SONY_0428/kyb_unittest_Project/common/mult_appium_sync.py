from time import ctime
import subprocess
import multiprocessing

appium_host = ['127.0.0.1']

def appium_start(host, port):
    '''启动appium'''

    bootstrap_port = str(port + 1)
    cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)
    #  参数                  默认值                含义
    # -U,  --udid              null                 连接物理设备的唯一设备标识符
    # -a,  --address          0.0.0.0               监听appium的 ip 地址
    # -p,  --port              4723                 监听appium端口
    # -bp, --bootstrap-port    4724                 连接Android设备的端口号(Android-only)
    # -g, --log                null                 将日志输出到指定文件
    # --no-reset              false                 session 之间不重置应用状态
    # --session-override      false                  允许 session 被覆盖 (冲突的话)
    # --app-activity          null                   打开Android应用时，启动的 Activity(Android-only) 的名字
    # --app                   null                    本地绝对路径_或_远程 http URL 所指向的一个安装包
    print('%s at %s' % (cmd, ctime()))
    subprocess.Popen(cmd, shell=True, stdout=open('../logs/' + str(port) + '.log', 'a'), stderr=subprocess.STDOUT)


# 构建进程组
appium_process = []

# 加载desired进程
for i in range(2):
    port = 4723 + 2 * i
    appium = multiprocessing.Process(target=appium_start, args=(appium_host[0], port))
    appium_process.append(appium)

if __name__ == '__main__':
    for desired in appium_process:
        desired.start()
    for desired in appium_process:
        desired.join()
