import logging
import os.path
import time


class Logger(object):
    # 1 获取一个日志对象（logger）
    # 2 设置此日志输出在什么地方（Handler）
    # 3 输出的地方必须满足某种格式要求，对它进行格式设置（Formatter）
    def __init__(self,logger):#初始化文件
        # 创建一个logger对象
        self.logger=logging.getLogger(logger)

        # 设置日志级别
        self.logger.setLevel(logging.DEBUG)
        #要对日志文件的名字按照一些特定的格式进行设置

        log_path=os.path.dirname(os.path.abspath('.'))+ '/logs/'
        log_name=log_path +'%s.log'%time.strftime('%Y_%m_%d')

        fh=logging.FileHandler(log_name,encoding='utf-8')
        # 为日志设置级别
        fh.setLevel(logging.DEBUG)
        #创建一个Handler，用于输出到控制台
        ch=logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        #定义Formatter，设置时间格式
        formatter=logging.Formatter('%(asctime)s -%(filename)s- %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        #为logger添加一个Handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


    def getlog(self):
        return self.logger
