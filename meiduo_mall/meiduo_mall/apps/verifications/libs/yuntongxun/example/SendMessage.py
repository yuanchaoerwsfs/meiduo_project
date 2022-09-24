from yuntongxun.ronglian_sms_sdk import SmsSDK

# accId = '容联云通讯分配的主账号ID'
# accToken = '容联云通讯分配的主账号TOKEN'
# appId = '容联云通讯分配的应用ID'


accId = '8aaf070882ede8b301836dcad7d0187a'
accToken = '3038432ec61146f3b410773b9ac5fcb4'
appId = '8aaf070882ede8b301836dcad8d21881'


def send_message():
    sdk = SmsSDK(accId, accToken, appId)
    tid = '1'
    mobile = '15620955019'
    datas = ('123456',)
    resp = sdk.sendMessage(tid, mobile, datas)
    print(resp)


send_message()
