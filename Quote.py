import platform

if platform.system() == "Windows":
    from Code.ESAPI import ESAPI, on_subscribe
else:
    from Code.ESAPILinux import ESAPI, on_subscribe


@on_subscribe
def on_subscribe_func(data):
    # 这些里写处理行情的函数，该函数为回调函数
    print('自定义函数接收到信息', data)


def test_api():
    # 登录并订阅
    api = ESAPI(on_subscribe_func)
    auth = 'B112F916FE7D27BCE7B97EB620206457946CED32E26C1EAC946CED32E26C1EAC946CED32E26C1EAC946CED32E26C1EAC5211AF9FEE541DDE9D6F622F72E25D5DEF7F47AA93A738EF5A51B81D8526AB6A9D19E65B41F59D6A946CED32E26C1EACCAF8D4C61E28E2B1ABD9B8F170E14F8847D3EA0BF4E191F5DCB1B791E63DC196D1576DEAF5EC563CA3E560313C0C3411B45076795F550EB050A62C4F74D5892D2D14892E812723FAC858DEBD8D4AF9410729FB849D5D8D6EA48A1B8DC67E037381A279CE9426070929D5DA085659772E24A6F5EA52CF92A4D403F9E46083F27B19A88AD99812DADA44100324759F9FD1964EBD4F2F0FB50B51CD31C0B02BB437'
    api.login(auth=auth,
              ip='61.163.243.173',
              port=7171,
              username='ES',
              password='123456')
    # api.login(auth=auth,
    #           ip='211.144.194.243',
    #           port=55019,
    #           username='JR921019',
    #           password='qs123876')
    api.subscribe(0, 'COMEX', 'F', 'GC', '2106')  # 可以订阅多个


if __name__ == '__main__':
    test_api()
