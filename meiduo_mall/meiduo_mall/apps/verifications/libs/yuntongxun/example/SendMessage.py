from yuntongxun.ronglian_sms_sdk import SmsSDK
import json

# accId = '容联云通讯分配的主账号ID'
# accToken = '容联云通讯分配的主账号TOKEN'
# appId = '容联云通讯分配的应用ID'

#
# def send_message():
#     sdk = SmsSDK(accId, accToken, appId)
#     tid = '1'
#     mobile = '15620955019'
#     datas = ('123456',)
#     resp = sdk.sendMessage(tid, mobile, datas)
#     print(resp)
#
#
# send_message()

accId = '8aaf070882ede8b301836dcad7d0187a'
accToken = '3038432ec61146f3b410773b9ac5fcb4'
appId = '8aaf070882ede8b301836dcad8d21881'
tid = '1'
mobile = '15620955019'
datas = ('555555', 5)


class CCP(object):
    def __new__(cls, *args, **kwargs):
        # 判断单例是否存在：_instance属性中存储的就是单例
        if not hasattr(cls, '_instance'):
            # 如果单例不存在，初始化单例
            cls._instance = super(CCP, cls).__new__(cls, *args, **kwargs)
            print(cls._instance)
            # 初始化REST SDK
            cls._instance.sdk = SmsSDK(accId, accToken, appId)
            print(cls._instance.sdk)

        return cls._instance

    def send_template_sms(self, tid, mobile, datas):
        """
        发送短信验证码单例方法
        :param tid: 模板ID
        :param mobile: 手机号
        :param datas: 内容数据

        :return: 成功：0 失败：-1
        """
        print(self.sdk)
        result = json.loads(self.sdk.sendMessage(tid, mobile, datas))   #将长得和字典一样的json文件转换为字典
        print(type(result))
        if result.get('statusCode') == '000000':
            return 0
        else:
            return -1


if __name__ == '__main__':
    ret = CCP()
    ret.send_template_sms(tid, mobile, datas)
