import logging
import os.path
import time

class Logger(object):
    def __init__(self,logger):#初始化文件
        # 创建一个logger对象
        self.logger=logging.getLogger(logger)
        # 设置日志级别
        self.logger.setLevel(logging.DEBUG)

        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        log_path=os.path.dirname(os.path.abspath('.'))+ '/logs/'
        log_name=log_path + rq + '.log'

        fh=logging.FileHandler(log_name)
        fh.setLevel(logging.DEBUG)
        ch=logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    def getlog(self):
        return self.logger