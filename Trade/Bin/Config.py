# 自动重连配置
re_time = 30  # 单位s，有些极端情况，没有断线，但是却没有行情。所以我们为了保险起见，设定了重连时间，建议30s

# 假期，以北京时间为准,避免重启导致资源浪费或者被封号
weekday = ['6', '7']  # 每周六和周日
day_time = ['05:00:00->05:59:58']  # 每日的05:00:00->05:59:58休市
holiday = []  # 节假日，比如"2020-12-31 23:59:59->2021-01-01 23:59:59"

# ESunny配置
es_account = ''  # 账号
es_password = ''  # 密码
es_ip = ''  # ip
es_port = ''  # port
es_auth_code = ''  # 授权码，默认为空
es_ver_code = ''  # 二次验证手机号
es_publish_way = 1