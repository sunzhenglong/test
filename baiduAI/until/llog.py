import logging
import datetime
LOG_DIR = "F:\\baiduAI\\log\\"
a = LOG_DIR + str(datetime.datetime.now().date())+".txt"
formatter = logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',datefmt='%d-%m-%Y:%H:%M:%S'

)
print(formatter)
c = logging.StreamHandler()
c.setFormatter(formatter)
w = logging.FileHandler(a,encoding="utf-8")
w.setFormatter(formatter)
def get_logger(filename):
    l = logging.getLogger(filename)
    l.addHandler(c)
    l.addHandler(w)
    l.setLevel(logging.INFO)
    return l