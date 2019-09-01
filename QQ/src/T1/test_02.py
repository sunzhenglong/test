from time import sleep
from until.phlog import get_logger
log = get_logger(filename="test_01.py")
from until.ciliu import hd
def test_4(cl):
        el,dr = cl
        s = dr.find_element_by_id("android:id/tabs").find_elements_by_class_name("android.widget.FrameLayout")
        for i in s:
            i.click()
            break
        log.info("hdhdhdhdhdhdhdhdh")
        sleep(4)
        hd(dr,t=500)

