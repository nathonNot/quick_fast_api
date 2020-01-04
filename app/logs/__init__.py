# 初始化系统日志
import logging
import os
import sys

import config
import logging.handlers

print("==========初始化系统日志==========")


class Log():
    def __init__(self, name=__name__):
        self.__name = name
        self.__path = config.LOGGING_SETTING.get('filename')
        self.__level = config.LOGGING_SETTING.get('level')
        self.__logger = logging.getLogger('app')
        # self.__logger = logging.getLogger(self.__name)
        self.__logger.setLevel(self.__level)
        if not self.__logger.handlers:
            # 创建一个handler，用于输出到文件
            fh = logging.FileHandler(self.__path, encoding="utf-8")
            fh.setLevel(logging.INFO)

            # 创建一个handler，用于输出到控制台
            ch = logging.StreamHandler(sys.stdout)
            ch.setLevel(logging.DEBUG)

            # 定义handler的输出格式
            formatter = logging.Formatter(fmt=config.LOGGING_SETTING.get('format'),datefmt=config.LOGGING_SETTING.get('datefmt'))
            ch.setFormatter(formatter)
            fh.setFormatter(formatter)

            # 给logger添加handler
            self.__logger.addHandler(fh)
            self.__logger.addHandler(ch)

    def __ini_handler(self):
        """初始化handler"""
        stream_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(self.__path, encoding='utf-8')
        return stream_handler, file_handler

    def __set_handler(self, stream_handler, file_handler, level='DEBUG'):
        """设置handler级别并添加到logger收集器"""
        stream_handler.setLevel(level)
        file_handler.setLevel(level)
        self.__logger.addHandler(stream_handler)
        self.__logger.addHandler(file_handler)

    def __set_formatter(self, stream_handler, file_handler):
        """设置日志输出格式"""
        formatter = logging.Formatter(fmt=config.LOGGING_SETTING.get('format'),
                              datefmt=config.LOGGING_SETTING.get('datefmt'))
        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

    def __close_handler(self, stream_handler, file_handler):
        """关闭handler"""
        stream_handler.close()
        file_handler.close()

    @property
    def Logger(self):
        """构造收集器，返回looger"""
        # stream_handler, file_handler = self.__ini_handler()
        # self.__set_handler(stream_handler, file_handler)
        # self.__set_formatter(stream_handler, file_handler)
        # self.__close_handler(stream_handler, file_handler)
        return self.__logger

    def info(self,message):
        self.Logger.info(message)

    def error(self,message):
        self.Logger.error(message)

    def debug(self,message):
        self.Logger.debug(message)

    def warning(self,message):
        self.Logger.warning(message)
