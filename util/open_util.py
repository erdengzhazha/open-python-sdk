import requests
import time
import hashlib
import logging
import threading
from logging import handlers
from urllib import parse
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.schedulers.blocking import BlockingScheduler

cond = threading.Condition()  # 线程条件变量

"""日志工具类"""
class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }  # 日志级别关系映射

    # 初始化日志配置
    def __init__(self, filename, level='info', when='d', backCount=3,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        # 设置日志格式
        format_str = logging.Formatter(fmt)
        # 设置日志级别
        self.logger.setLevel(self.level_relations.get(level))
        # 往屏幕上输出
        sh = logging.StreamHandler()
        # 设置屏幕上显示的格式
        sh.setFormatter(format_str)
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,
                                               encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)  # 设置文件里写入的格式
        self.logger.addHandler(sh)  # 把对象加到logger里
        self.logger.addHandler(th)

log = Logger('../error.log', level='error').logger

"""开放接口工具"""
class OpenPlatform():

    #applicationkey = ''
    #authenticator = ''
    sign_dict = {}
    #初始化参数
    def __init__(self):
        self.url = "http://cloudapi.ovopark.com/m.api"
        #sign字典
        self.sign_dict = {
            '_aid': 'S107',
            '_akey': '',
            '_requestMode': 'POST',
            '_sm': 'md5',
            #'_timestamp': '',
            # '_timestamp': time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
            #'_version': version,
            # '_mt': mt
        }
        self.asecret = ''
        self.headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                         'authenticator':''
                        }
    # 生成签名
    def createSign(self, params):
        log.error(self.sign_dict)
        # 拼接
        sign_dict = {**self.sign_dict, **params}
        # 对键进行排序
        d = dict(sorted(sign_dict.items(), key=lambda x: x[0]))
        # 连接参数名与参数值,并在首尾加上secret
        sb = ''
        sb += self.asecret
        for key in d:
            sb += key
            sb += str(d[key])
        sb += self.asecret
        #print('字符串'+sb)
        # md5加密
        sign = hashlib.md5(sb.encode(encoding='UTF-8')).hexdigest()
        # 转大写
        d['_sig'] = str(sign).upper()
        # 将加密后的url记录到d
        self.d = d
        log.error(sign)
        return sign

    def httpRequest(self):
        log.error(self.d)
        para = parse.urlencode(self.d)
        # 解决[WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败
        requests.adapters.DEFAULT_RETRIES = 5
        s = requests.session()
        s.keep_alive = False
        try:
            resp = s.post(url=self.url, data=para, headers=self.headers, stream=False, timeout=30)
            print(resp)
        except requests.exceptions.ConnectionError:
            log.error("Connection refused")
        log.info(resp.json())
        #print(resp.json())
        return str(resp.json())


# def push_ticket():
#     # time.sleep(0.01)
#     # 请求参数
#     params = {
#
#     }
#     url = 'http://openapi.ovopark.com/m.api'
#     akey = 'S107-00000183'
#     asecret = 'fa763b15729b35320270d326ee170bb8'
#     # version = 'v2'# 默认值 v1
#     mt = 'open.shopweb.role.getRoleListByGroup'
#
#     # open = openPlatform(url=url, akey=akey, mt=mt, version=version)
#     open = OpenPlatform(url=url, akey=akey, mt=mt)
#     open.createSign(params, asecret)
#     open.httpRequest()


# def main():
#     log.error("----------------------定时任务----------------------")
#     # 上推票
#     push_ticket()


# 主入口
# if __name__ == "__main__":

    # main()
    # 定时任务
    # scheduler = BlockingScheduler()
    # trigger = IntervalTrigger(minutes=60)
    # scheduler.add_job(main, trigger)
    # # 定时任务设置
    # try:
    #     scheduler.start()
    #     # 定时任务开启
    # except (KeyboardInterrupt, SystemExit):
    #     pass
