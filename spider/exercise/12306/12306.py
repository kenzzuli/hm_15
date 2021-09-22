import re
import time
import json
from pprint import pprint

from utils.parse_date import parseDate
from utils.stations_dict import stations_dict
from utils.parse_passenger import parsePassenger
from utils.parse_seat_type import seat_type_dict
from utils.parse_trains_infos import parseTrainsInfos

from DecryptLogin import login

redis_timeout = 180  # redis中cookies_dict的过期时间 单位秒


class Funk12306:
    def __init__(self, username, password):
        lg = login.Login()
        infos_return, self.s = lg.zt12306(username, password)

    def buy_ticket(self):

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
            'Host': 'kyfw.12306.cn',
            'X-Requested-With': 'XMLHttpRequest', }

        url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
        res = self.s.post(url)
        print(res.content.decode())

        # 获取城市(车站)编码
        # from_station = input('输入出发城市或车站:')
        from_station = "上海虹桥"
        # to_station = input('输入到达城市或车站:')
        to_station = "郑州东"
        # train_date = input('输入出行日期,格式为2018-12-03:')
        train_date = "2021-09-24"
        from_station_code = stations_dict.get(from_station, '')
        to_station_code = stations_dict.get(to_station, '')

        # 查询车量具体信息query
        url = 'https://kyfw.12306.cn/otn/leftTicket/queryO?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' % (
            train_date, from_station_code, to_station_code)
        response = self.s.get(url)
        print(response.text)

        # 解析获取trains_list
        trains_list = parseTrainsInfos(json.loads(response.content)['data']['result'])
        print('查询的列车信息如下：')
        pprint(trains_list)
        # 获取选择的列车
        # train_info_dict = trains_list[int(input('请输入选中车次的下标：'))]
        train_info_dict = trains_list[1]
        print('选中了列车信息为：')
        pprint(train_info_dict)
        # 列车信息
        secretStr = train_info_dict['secretStr']
        leftTicket = train_info_dict['leftTicket']
        train_location = train_info_dict['train_location']

        # 检查用户是否保持登录成功
        self.s.headers['Referer'] = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
        url = 'https://kyfw.12306.cn/otn/login/checkUser'
        data = {'_json_att': ''}
        resp = self.s.post(url, data=data, headers=self.headers, verify=False)
        print(json.loads(resp.text))

        # 点击预定
        self.s.headers['Referer'] = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
        url = 'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest'
        data = {
            'secretStr': secretStr,
            'train_date': train_date,
            'back_train_date': train_date,
            'tour_flag': 'dc',  # dc 单程 wf 往返
            'purpose_codes': 'ADULT',  # 成人
            'query_from_station_name': from_station,
            'query_to_station_name': to_station,
            'undefined': ''
        }
        resp = self.s.post(url, data=data)
        # print(resp.text)

        # 订单初始化 获取REPEAT_SUBMIT_TOKEN key_check_isChange
        self.s.headers['Referer'] = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
        url = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'
        data = {'_json_att': ''}
        response = self.s.post(url, data=data)
        print("_" * 50)
        print(response.content.decode())
        repeat_submit_token = re.search(r"var globalRepeatSubmitToken = '([a-z0-9]+)';",
                                        response.content.decode()).group(1)
        key_check_isChange = re.search("'key_check_isChange':'([A-Z0-9]+)'", response.content.decode()).group(1)

        # 获取用户信息
        # 需要 REPEAT_SUBMIT_TOKEN
        url = 'https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs'
        data = {'_json_att': '',
                'REPEAT_SUBMIT_TOKEN': repeat_submit_token}
        response = self.s.post(url, data=data)

        # 解析并构造乘客信息列表
        passenger_list = parsePassenger(json.loads(response.content))
        print('获取乘客信息有：')
        pprint(passenger_list)
        passenger_info_dict = passenger_list[int(input('输入要购票的乘车人的下标'))]

        # 坐席类型
        try:
            seat_type = seat_type_dict[input('请输入要购买的坐席类型的拼音，如果输入错误，将强行购买无座，能回家就行了，还要tm什么自行车！：')]
        except:
            seat_type = seat_type_dict['wuzuo']

        # 构造乘客信息
        passengerTicketStr = '%s,0,1,%s,%s,%s,%s,N' % (
            seat_type, passenger_info_dict['passenger_name'],
            passenger_info_dict['passenger_id_type_code'],
            passenger_info_dict['passenger_id_no'],
            passenger_info_dict['passenger_mobile_no'])
        oldPassengerStr = '%s,%s,%s,1_' % (
            passenger_info_dict['passenger_name'],
            passenger_info_dict['passenger_id_type_code'],
            passenger_info_dict['passenger_id_no'])

        # 检查选票人信息
        url = 'https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo'
        data = {
            'cancel_flag': '2',  # 未知
            'bed_level_order_num': '000000000000000000000000000000',  # 未知
            'passengerTicketStr': passengerTicketStr.encode('utf-8'),  # O,0,1,靳文强,1,142303199512240614,18335456020,N
            'oldPassengerStr': oldPassengerStr.encode('utf-8'),  # 靳文强,1,142303199512240614,1_
            'tour_flag': 'dc',  # 单程
            'randCode': '',
            'whatsSelect': '1',
            '_json_att': '',
            'REPEAT_SUBMIT_TOKEN': repeat_submit_token
        }
        resp = self.s.post(url, data=data)
        print(resp.text)

        # 提交订单,并获取排队人数,和车票的真实余数
        url = 'https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount'
        data = {
            'train_date': parseDate(train_date),  # Fri Nov 24 2017 00:00:00 GMT+0800 (中国标准时间)
            'train_no': train_info_dict['train_no'],  # 6c0000G31205
            'stationTrainCode': train_info_dict['stationTrainCode'],  # G312
            'seatType': seat_type,  # 席别
            'fromStationTelecode': train_info_dict['from_station'],  # one_train[6]
            'toStationTelecode': train_info_dict['to_station'],  # ? one_train[7]
            'leftTicket': train_info_dict['leftTicket'],  # one_train[12]
            'purpose_codes': '00',
            'train_location': train_info_dict['train_location'],  # one_train[15]
            '_json_att': '',
            'REPEAT_SUBMIT_TOKEN': repeat_submit_token
        }
        resp = self.s.post(url, data=data)
        print(resp.text)
        print('此时排队买票的人数为：{}'.format(json.loads(resp.text)['data']['count']))
        ticket = json.loads(resp.text)['data']['ticket']
        print('此时该车次的余票数量为：{}'.format(ticket))
        if ticket == '0':
            print('没有余票，购票失败')
            return '没有余票，购票失败'

        # 确认订单,进行扣票 需要 key_check_isChange
        url = 'https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue'
        data = {
            'passengerTicketStr': passengerTicketStr.encode('utf-8'),
            'oldPassengerStr': oldPassengerStr.encode('utf-8'),
            'randCode': '',
            'purpose_codes': '00',
            'key_check_isChange': key_check_isChange,
            'leftTicketStr': leftTicket,
            'train_location': train_location,  # one_train[15]
            'choose_seats': '',  # 选择坐席 ABCDEF 上中下铺 默认为空不选
            'seatDetailType': '000',
            'whatsSelect': '1',
            'roomType': '00',
            'dwAll': 'N',  # ?
            '_json_att': '',
            'REPEAT_SUBMIT_TOKEN': repeat_submit_token
        }
        resp = self.s.post(url, data=data)
        print(json.loads(resp.text))
        if json.loads(resp.text)['status'] == False or json.loads(resp.text)['data']['submitStatus'] == False:
            print('扣票失败')
            return '扣票失败'

        # 排队等待 返回waittime  获取 requestID 和 orderID
        timestamp = str(int(time.time() * 1000))  # str(time.time() * 1000)[:-4]
        url = 'https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime?random=%s&tourFlag=dc&_json_att=&REPEAT_SUBMIT_TOKEN=%s' % (
            timestamp, repeat_submit_token)
        resp = self.s.get(url)
        print(resp.text)
        try:
            orderID = json.loads(resp.text)['data']['orderId']
        except:
            # 排队等待 返回waittime  获取 requestID 和 orderID
            timestamp = str(int(time.time() * 1000))  # str(time.time() * 1000)[:-4]
            url = 'https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime?random=%s&tourFlag=dc&_json_att=&REPEAT_SUBMIT_TOKEN=%s' % (
                timestamp, repeat_submit_token)
            resp = self.s.get(url)
            print(resp.text)
            try:
                orderID = json.loads(resp.text)['data']['orderId']
            except:
                return '购票失败'

        # 订单结果
        url = 'https://kyfw.12306.cn/otn/confirmPassenger/resultOrderForDcQueue'
        data = {
            'orderSequence_no': orderID,
            '_json_att': '',
            'REPEAT_SUBMIT_TOKEN': repeat_submit_token
        }
        resp = self.s.post(url, data=data)
        print(resp.text)

    def run(self):
        # 买票
        self.buy_ticket()


if __name__ == '__main__':
    username = 'jiaofeibuli'
    password = 'liulei123'
    funk = Funk12306(username, password)
    funk.run()
