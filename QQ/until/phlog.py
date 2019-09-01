import logging
import datetime

# 日志文件夹\目录
LOG_DIR = "F:\\QQ\\logger\\"    #大写变量名一般表示不变动的变量

# 日期.txt   创建日志文件名字
a = LOG_DIR + str(datetime.datetime.now().date())+".txt"
# logging----> python定义日志的库

# 定义日志输出的格式
formatter = logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',datefmt='%d-%m-%Y:%H:%M:%S'

)
print(formatter)
# logging的两种输出方式
# 1.输出到pycharm控制台
c = logging.StreamHandler()
# 添加日志的样式
c.setFormatter(formatter)
# 2.输出到文本
w = logging.FileHandler(a,encoding="utf-8")
# 添加日志样式
w.setFormatter(formatter)

def get_logger(filename):
    # 获取执行日志的脚本名字
    l = logging.getLogger(filename)
    # 添加输出内容到控制台
    l.addHandler(c)
    # 添加内容到文本
    l.addHandler(w)
    # 定义日志等级  INFO-->最低等级
    l.setLevel(logging.INFO)
    return l
# log = get_logger()
# log.info("tttttttttttttttttttttttttttt")
# log.error("eeeeeeerrrrrrr")
